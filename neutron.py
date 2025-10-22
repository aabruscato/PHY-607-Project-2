"""
neutron.py

Defines a Neutron class for Monte Carlo neutron transport simulations.

Includes:
- Position and direction tracking
- Movement based on sampled free paths
- Scattering using angular distributions
"""

import numpy as np
from sampling import sample_cos_theta
from scipy.integrate import solve_ivp


class Neutron:
    def __init__(self, position=None, velocity=None, mass=1.0, alive=True):
        """
        Initialize a neutron with position, velocity, mass, and alive status.
        If position or velocity are not provided, defaults are used.
        """
        self.position = np.array(
            position if position is not None else [0.0, 0.0, 0.0], dtype=float
        )
        self.velocity = (
            np.array(velocity, dtype=float)
            if velocity is not None
            else self.random_direction()
        )
        self.mass = mass
        self.alive = alive

    def random_direction(self):
        """
        Generate a random isotropic unit vector.
        Uses uniform sampling over the sphere.
        """
        theta = np.arccos(2 * np.random.random() - 1)  # polar angle
        phi = 2 * np.pi * np.random.random()  # azimuthal angle
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        return np.array([x, y, z])

    def acceleration(self, t):
        """
        Define acceleration as force/mass. Override for different forces.
        """
        # No external forces - neutrons travel in straight lines
        return np.array([0.0, 0.0, 0.0])

    def move_ode(self, t_span):
        """
        Move the neutron using 2nd-order ODE integration over time t_span.
        t_span: tuple (t_start, t_end)
        """

        def ode(t, y):
            pos = y[:3]
            vel = y[3:]
            dydt = np.zeros(6)
            dydt[:3] = vel
            dydt[3:] = self.acceleration(t)
            return dydt

        y0 = np.concatenate([self.position, self.velocity])
        sol = solve_ivp(ode, t_span, y0, method="RK45", max_step=0.01)
        self.position = sol.y[:3, -1]
        self.velocity = sol.y[3:, -1]

    def scatter(self):
        """
        Scatter the neutron using a cos(theta) angular distribution.
        Updates the direction vector accordingly.
        """
        theta = sample_cos_theta()[0]  # returns a single sample
        phi = 2 * np.pi * np.random.random()  # uniform azimuthal angle

        # Get current speed to maintain it after scattering
        speed = np.linalg.norm(self.velocity)

        # Convert to Cartesian coordinates
        new_direction = np.array(
            [
                np.sin(theta) * np.cos(phi),
                np.sin(theta) * np.sin(phi),
                np.cos(theta),
            ]
        )

        # Update velocity with new direction, preserving speed
        self.velocity = speed * new_direction
