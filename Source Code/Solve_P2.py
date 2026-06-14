from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np

# Loading the circuit
qc = QuantumCircuit.from_qasm_file("")  # Add the .qasm file path for Problem 2.
print("Circuit loaded with", qc.num_qubits, "qubits")

# Running full statevector simulation
backend = Aer.get_backend("statevector_simulator")
result = backend.run(qc).result()
statevector = np.array(result.get_statevector())

# Finding peak amplitude
idx = np.argmax(np.abs(statevector))
bitstring = format(idx, f"0{qc.num_qubits}b")

print("\n🎯 PEAK BITSTRING FOUND")
print("Bitstring:", bitstring)
print("Probability:", abs(statevector[idx])**2)
print("(Reverse also accepted):", bitstring[::-1])
