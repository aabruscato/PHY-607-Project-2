"""
sampling.py

Random sampling distributions for the Monte Carlo neutron transport simulation.

Includes:
- Inverse CDF distribution for exponential free-path lengths.
- Rejection sampling for angular scattering distributions.
"""

import numpy as np

def sample_exponential(mean_free_path, size = 1, rng = None):
    """
    Generates an array of distances that the neutron will travel before
    it collides with a uranium atom using the inverse CDF method.
    """
    rng = rng or np.random.default_rng()
    u = rng.random(size)
    return -mean_free_path * np.log(1.0 - u)


def sample_cos_theta(size = 1, rng = None):
    """
    Generates random scattering angles (theta) for neutrons using
    rejection sampling from a distribution proportional to cos(theta).
    """
    rng = rng or np.random.default_rng()
    samples = []
    M = 1.0  # max value of cos(theta)
    while len(samples) < size:
        theta = rng.random() * (np.pi / 2)
        u = rng.random() * M
        if u <= np.cos(theta):
            samples.append(theta)
    return np.array(samples)

