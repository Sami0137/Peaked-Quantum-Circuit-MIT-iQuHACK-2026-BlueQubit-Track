# Peaked-Quantum-Circuit-MIT-iQuHACK-2026-BlueQubit-Track

Welcome to my project repository! This space contains my work, code, and solutions for the Peaked Circuits Challenge.

## 📖 Challenge Overview

In this challenge, I am working with special quantum circuits—known as **Peaked Circuits**—provided in `.qasm` format. Each circuit is uniquely designed to set up a specific quantum state. Hidden within that state is a single bitstring engineered to appear with a very high probability.

**Objective :** To successfully parse these circuits, analyze the quantum states, and find the hidden highest probable bitstrings!


## 📂 Repository Structure

* **`circuits/`** - Contains the `.qasm` files I received for the challenge.
* **`src/`** - My source code and scripts used to analyze the circuits and extract the bitstrings.
* **`results/`** - The identified bitstrings, output logs, and any performance metrics.

## 🛠️ Tech Stack & Dependencies

This project is built using Python and industry-standard quantum computing libraries to simulate and analyze quantum states.

### Core Technologies
* **Language:** Python (v3.8+)
* **Quantum Framework:** [Qiskit](https://www.ibm.com/quantum/qiskit) — For parsing, structuring, and manipulating OpenQASM (`.qasm`) circuits.
* **Simulation Engine:** [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) — Specifically utilizing the high-performance `statevector_simulator` to compute exact probability amplitudes.
* **Numerical Processing:** [NumPy](https://numpy.org/) — For handling statevector arrays and performing fast vectorized array operations (`np.abs`, `np.argmax`).


## 💡 Design Choice: Why Statevector Simulation?
I intentionally chose to use the `statevector_simulator` for this challenge because it avoids the statistical noise inherent in shot-based execution (such as running a circuit 1024 times and counting the results). By using exact quantum state simulation rather than relying on hardware sampling approximations, I can mathematically pinpoint the exact peak probability.



## A great Source to learn more about this
https://app.bluequbit.io/tutorial/variational-quantum-classifier
