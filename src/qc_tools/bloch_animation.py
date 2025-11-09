from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli
from qiskit.visualization.bloch import Bloch
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import os

# Create a simple 1-qubit circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)

# Get the final statevector
state = Statevector.from_instruction(qc)

# Compute Bloch vector for 1-qubit state using Pauli operators
bloch_vec = [
    np.real(state.expectation_value(Pauli('X'))),
    np.real(state.expectation_value(Pauli('Y'))),
    np.real(state.expectation_value(Pauli('Z')))
]

# Prepare figure
fig = plt.figure()
bloch = Bloch(fig=fig)
bloch.vector_color = ['r']

# Animation: rotate Bloch vector around Z
angles = np.linspace(0, 2*np.pi, 30)  # 30 frames

def update(frame):
    bloch.clear()
    # Rotate vector around Z axis
    x, y, z = bloch_vec
    x_rot = x * np.cos(frame) - y * np.sin(frame)
    y_rot = x * np.sin(frame) + y * np.cos(frame)
    bloch.add_vectors([ [x_rot, y_rot, z] ])
    bloch.render()

ani = animation.FuncAnimation(fig, update, frames=angles, interval=100, repeat=True)

# Create output directory if it doesn't exist
output_dir = os.path.join('.', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'bloch_sphere.gif')

# Save GIF
ani.save(output_path, writer='pillow', fps=10)
print(f"Bloch sphere animation saved to {output_path}")



# from qiskit import QuantumCircuit
# from qiskit.quantum_info import Statevector
# from qiskit.visualization import plot_bloch_multivector
# import matplotlib.pyplot as plt

# qc = QuantumCircuit(1)
# qc.h(0)
# qc.t(0)

# state = Statevector.from_instruction(qc)

# # Plot and save as PNG
# plot_bloch_multivector(state)
# import os
# output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'bloch_sphere.png')
# plt.savefig(output_path, dpi=300)
# print(f"Bloch sphere image saved to {output_path}")
