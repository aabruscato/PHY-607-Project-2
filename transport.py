"""
transport.py

Monte Carlo neutron transport simulation using ODE-based motion.

Each neutron evolves under a force using scipy.integrate.solve_ivp,
and probabilistic scattering/absorption events determine its fate.
"""

import numpy as np
from neutron import Neutron

class Simulation:
    """
    Simulates neutron transport through a material using ODE motion.
    """

    def __init__(self, num_neutrons = 1000, scatter_prob = 0.7, absorb_prob = 0.3):
        self.num_neutrons = num_neutrons
        self.scatter_prob = scatter_prob
        self.absorb_prob = absorb_prob
        self.path_lengths = []

    def step(self, neutron):
        """
        Advance one neutron’s motion via ODE integration and determine its fate.
        """
        # Evolve position and velocity using ODE
        initial_position = neutron.position.copy()
        neutron.move_ode((0, 0.1))  # evolve over short time span

        # Measure path length for this ODE segment
        step_distance = np.linalg.norm(neutron.position - initial_position)
        self.path_lengths.append(step_distance)

        # Probabilistic scattering or absorption
        fate = np.random.random()
        if fate < self.scatter_prob:
            neutron.scatter()
        elif fate < self.scatter_prob + self.absorb_prob:
            neutron.alive = False
        else:
            neutron.scatter()

    def run(self):
        """
        Run the ODE-based simulation for all neutrons until they are absorbed.
        Returns all path lengths.
        """
        neutrons = [Neutron() for _ in range(self.num_neutrons)]

        for neutron in neutrons:
            while neutron.alive:
                self.step(neutron)

        return np.array(self.path_lengths)
