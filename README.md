# Monte Carlo Neutron Transport Simulation

This project simulates neutron motion and scattering in a material using a Monte Carlo approach combined with ODE-based trajectory evolution. It is designed as a Python package that can be installed and run easily.

---

## Features

- Monte Carlo simulation of neutrons moving through a material
- Probabilistic interactions: scattering and absorption
- Exponential free-path sampling (Inverse CDF method)
- Angular scattering using rejection sampling
- Continuous motion under forces using 2nd-order ODE integration
- Histogram visualization of both individual collision distances and total travel distances

---

## Installation

1. Clone the repository:
```bash
git clone <git@github.com:aabruscato/PHY-607-Project-2.git>
cd PHY-607-Project-2

