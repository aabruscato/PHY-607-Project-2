"""
transport.py

Monte Carlo neutron transport simulation using ODE-based motion.

Each neutron evolves under a force using scipy.integrate.solve_ivp,
and probabilistic scattering/absorption events determine its fate.
"""

import numpy as np
from neutron import Neutron
from sampling import sample_exponential


class Simulation:
    """
    Simulates neutron transport through a material using ODE motion.
    """

    def __init__(
        self,
        num_neutrons=1000,
        scatter_prob=0.7,
        absorb_prob=0.3,
        mean_free_path=1.0,
    ):
        self.num_neutrons = num_neutrons
        self.scatter_prob = scatter_prob
        self.absorb_prob = absorb_prob
        self.mean_free_path = mean_free_path
        self.path_lengths = []
        self.total_distances = []
        self.collision_counts = []

    def step(self, neutron):
        """
        Advance one neutron's motion via ODE integration and determine its fate.
        """
        # Sample distance to next collision using exponential distribution
        collision_distance = sample_exponential(self.mean_free_path)[0]

        # Calculate time needed to travel this distance
        speed = np.linalg.norm(neutron.velocity)
        if speed > 0:
            time_to_collision = collision_distance / speed
        else:
            time_to_collision = 0.1  # fallback for zero velocity

        # Evolve position and velocity using ODE
        initial_position = neutron.position.copy()
        neutron.move_ode((0, time_to_collision))

        # Measure actual path length for this ODE segment
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
        Returns dictionary with path lengths, total distances, and collisions.
        """
        neutrons = [Neutron() for _ in range(self.num_neutrons)]

        for neutron in neutrons:
            initial_position = neutron.position.copy()
            collision_count = 0

            while neutron.alive:
                self.step(neutron)
                collision_count += 1

            # Calculate total distance traveled by this neutron
            total_distance = np.linalg.norm(neutron.position - initial_position)
            self.total_distances.append(total_distance)
            self.collision_counts.append(collision_count)

        return {
            "path_lengths": np.array(self.path_lengths),
            "total_distances": np.array(self.total_distances),
            "collision_counts": np.array(self.collision_counts),
        }
