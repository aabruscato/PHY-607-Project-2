""""
main.py

Entry point for the Monte Carlo neutron transport simulation.
Runs the Simulation class and visualizes results.
"""

import matplotlib.pyplot as plt
from transport import Simulation


def plot_path_lengths(paths):
    """
    Plot a histogram of neutron path lengths.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(paths, bins = 50, density = True, alpha = 0.7, color = "skyblue")
    plt.xlabel("Path Length")
    plt.ylabel("Probability Density")
    plt.title("Neutron Free Path Distribution")
    plt.grid(True)
    plt.show()


def main():
    # Create and run a simulation instance
    sim = Simulation(
        num_neutrons = 1000,
        scatter_prob = 0.7,
        absorb_prob = 0.3,
    )

    print("Running simulation...")
    paths = sim.run()

    print(f"Simulated {len(paths)} neutron collisions.")
    print(f"Average path length: {sum(paths) / len(paths):.3f}")

    # Plot results
    plot_path_lengths(paths)


if __name__ == "__main__":
    main()
