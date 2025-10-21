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

class Neutron:
    def __init__(self, position = None, direction = None, alive = True):
        """
        Initialize a neutron with position, direction, and alive status.
        If position or direction are not provided, defaults are used.
        """
        self.position = np.array(position if position is not None else [0.0, 0.0, 0.0], dtype = float)
        self.direction = np.array(direction, dtype = float) if direction is not None else self.random_direction()
        self.alive = alive

    def random_direction(self):
        """
        Generate a random isotropic unit vector.
        Uses uniform sampling over the sphere.
        """
        theta = np.arccos(2 * np.random.random() - 1)  # polar angle
        phi = 2 * np.pi * np.random.random()             # azimuthal angle
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        return np.array([x, y, z])

    def move(self, distance):
        """
        Move the neutron along its current direction by a given distance.
        """
        self.position += distance * self.direction

    def scatter(self):
        """
        Scatter the neutron using a cos(theta) angular distribution.
        Updates the direction vector accordingly.
        """
        theta = sample_cos_theta()[0]  # returns a single sample
        phi = 2 * np.pi * np.random.random()  # uniform azimuthal angle

        # Convert to Cartesian coordinates
        self.direction = np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta)
        ])
