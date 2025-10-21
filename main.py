"""
main.py

Main driver for Monte Carlo neutron transport simulation.

- Runs the neutron transport simulation
- Collects path lengths
- Plots results to visualize distributions
"""

import numpy as np
import matplotlib.pyplot as plt
from transport import run_transport

def plot_path_lengths(paths):
    """
    Plot a histogram of neutron path lengths.
    """
    plt.hist(paths, bins = 50, density = True, alpha = 0.7, color = "skyblue")
    plt.xlabel("Path length")
    plt.ylabel("Probability density")
    plt.title("Neutron Free Path Distribution")
    plt.grid(True)
    plt.show()

def main():
    # Simulation parameters
    num_neutrons = 5000
    mean_free_path = 1.0
    scatter_prob = 0.7
    absorb_prob = 0.3

    # Run simulation
    paths = run_transport(num_neutrons, mean_free_path, scatter_prob, absorb_prob)
    print(f"Simulated {len(paths)} neutron collisions.")
    print(f"Average path length: {np.mean(paths):.3f}")

    # Plot results
    plot_path_lengths(paths)

if __name__ == "__main__":
    main()
