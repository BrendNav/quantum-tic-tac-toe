from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
qc.h(0)              # Apply Hadamard gate
qc.measure(0, 0)     # Measure qubit 0 into classical bit 0

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the simulator
job = execute(qc, backend=simulator, shots=1024)
result = job.result()

# Print the result counts
counts = result.get_counts(qc)
print("Measurement results:", counts)
