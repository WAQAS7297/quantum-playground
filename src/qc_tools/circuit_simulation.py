

import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

# Ensure the assets folder exists
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(script_dir))
assets_dir = os.path.join(root_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

# Example 3-qubit circuit
qc = QuantumCircuit(3, 3)
qc.h([0, 1])
qc.cx(0, 2)
qc.measure([0, 1, 2], [0, 1, 2])

# Save circuit image
output_file = os.path.join(assets_dir, 'quantum_circuit_simulation.png')
circuit_drawer(qc, output='mpl', filename=output_file, scale=2)

print(f"Quantum circuit image saved to {os.path.relpath(output_file, root_dir)}")
