from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)

state = Statevector.from_instruction(qc)

# Plot and save as PNG
plot_bloch_multivector(state)
import os
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'bloch_sphere.png')
plt.savefig(output_path, dpi=300)
print(f"Bloch sphere image saved to {output_path}")
