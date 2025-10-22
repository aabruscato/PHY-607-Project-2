"""
main.py

Entry point for the Monte Carlo neutron transport simulation.
Runs the Simulation class and visualizes results.
"""

import matplotlib.pyplot as plt
import numpy as np
from transport import Simulation
from sampling import sample_exponential


def plot_path_lengths(paths):
    """
    Plot a histogram of neutron path lengths.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(paths, bins=50, density=True, alpha=0.7, color="skyblue")
    plt.xlabel("Path Length")
    plt.ylabel("Probability Density")
    plt.title("Neutron Free Path Distribution")
    plt.grid(True)
    plt.show()


def validate_exponential_distribution(paths, mean_free_path):
    """
    Validate that path lengths follow expected exponential distribution.
    """
    print("\n=== Physical Validation ===")
    measured_mean = np.mean(paths)
    theoretical_mean = mean_free_path
    percent_error = abs(measured_mean - theoretical_mean) / theoretical_mean * 100

    print(f"Expected mean free path: {theoretical_mean:.3f}")
    print(f"Measured mean free path: {measured_mean:.3f}")
    print(f"Percent error: {percent_error:.2f}%")

    if percent_error < 10:
        print("✓ Statistical validation: PASSED")
    else:
        print("✗ Statistical validation: Large deviation detected")

    # Test exponential fit
    measured_std = np.std(paths)
    theoretical_std = mean_free_path  # std = mean for exponential
    std_error = abs(measured_std - theoretical_std) / theoretical_std * 100
    print(f"\nExpected std deviation: {theoretical_std:.3f}")
    print(f"Measured std deviation: {measured_std:.3f}")
    print(f"Percent error: {std_error:.2f}%")


def main():
    # Create and run a simulation instance
    mean_free_path = 1.0
    sim = Simulation(
        num_neutrons=1000,
        scatter_prob=0.7,
        absorb_prob=0.3,
        mean_free_path=mean_free_path,
    )

    print("Running simulation...")
    results = sim.run()

    paths = results["path_lengths"]
    total_distances = results["total_distances"]
    collision_counts = results["collision_counts"]

    print(f"\nSimulated {len(paths)} neutron collisions.")
    print(f"Average path length per collision: {np.mean(paths):.3f}")
    print(f"Average total distance per neutron: {np.mean(total_distances):.3f}")
    print(f"Average collisions per neutron: {np.mean(collision_counts):.1f}")

    # Validate physical properties
    validate_exponential_distribution(paths, mean_free_path)

    # Plot results
    plot_path_lengths(paths)


if __name__ == "__main__":
    main()
