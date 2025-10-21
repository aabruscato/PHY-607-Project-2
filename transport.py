"""
transport.py

Monte Carlo neutron transport simulation using the Neutron class.

Includes:
- Generating neutrons
- Tracking their movement and collisions
- Scattering and absorption
- Collecting basic statistics
"""

import numpy as np
from neutron import Neutron
from sampling import sample_exponential

def run_transport(num_neutrons = 1000, mean_free_path = 1.0, scatter_prob = 0.7, absorb_prob = 0.3):
    """
    Simulate a batch of neutrons moving through a material and return
    a list of distances traveled by all neutrons.
    """
    neutrons = [Neutron() for _ in range(num_neutrons)]
    path_lengths = []

    for neutron in neutrons:
        while neutron.alive:
            # Sample distance to next collision
            distance = sample_exponential(mean_free_path)
            neutron.move(distance)
            path_lengths.append(distance)

            # Decide neutron fate
            fate = np.random.random()
            if fate < scatter_prob:
                neutron.scatter()
            elif fate < scatter_prob + absorb_prob:
                neutron.alive = False  # absorbed
            else:
                # Remaining probability treated as scatter
                neutron.scatter()

    return path_lengths
