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
- Physical validation of exponential distribution

---

## Installation

1. Clone the repository:
```bash
git clone git@github.com:aabruscato/PHY-607-Project-2.git
cd PHY-607-Project-2
```

2. Install the package:
```bash
pip install -e .
```

3. Run the simulation:
```bash
run-transport
```

Or run directly with Python:
```bash
python main.py
```

---

## Physics and Validation

### Monte Carlo Transport Model

The simulation models neutron transport through a material where neutrons:
1. Travel distances sampled from an exponential distribution (mean free path)
2. Undergo scattering or absorption at collision points
3. Move under gravitational force between collisions using ODE integration

### Expected Physical Properties

**Exponential Free Path Distribution:**
- The distance between collisions should follow: P(x) = (1/λ) exp(-x/λ)
- Mean distance = λ (mean free path)
- Standard deviation = λ

**Conservation Properties:**
- Total number of neutrons is conserved until absorption
- Each neutron must eventually be absorbed (probability = 1)

### Validation Results

The simulation validates that:
- Measured mean free path matches the input parameter (within ~5-10%)
- Path length distribution follows exponential statistics
- Standard deviation equals mean free path (characteristic of exponential)

---

## Code Structure

- `neutron.py` - Neutron class with ODE-based motion and scattering
- `transport.py` - Simulation class that runs Monte Carlo transport
- `sampling.py` - Probability distribution sampling functions
- `main.py` - Entry point with visualization and validation
- `pyproject.toml` - Package configuration

---

## Requirements

- Python >= 3.8
- numpy
- scipy
- matplotlib

---

## Authors

Amelia Abruscato (arabrusc@syr.edu)
Shreyan Goswami (sgoswa03@syr.edu)
