from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization.bloch import Bloch  
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import os

# Create a circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)

# Get the final statevector
state = Statevector.from_instruction(qc)

# Create a Bloch sphere object
bloch = Bloch()
bloch.vector_color = ['r']

# Extract the Bloch vector
bloch_vec = state.data.real[:3] if state.num_qubits == 1 else state.expectation_value([1,0,0])

# Prepare figure for animation
fig = plt.figure()

# For simplicity, let's animate the rotation around Z
angles = np.linspace(0, np.pi/2, 20)  # 20 frames

def update(frame):
    plt.clf()
    bloch.clear()
    # Rotate around Z
    bloch.add_vectors([np.cos(frame), np.sin(frame), 0])
    bloch.render()

ani = animation.FuncAnimation(fig, update, frames=angles, repeat=True)

# Save as GIF
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'bloch_sphere.gif')
ani.save(output_path, writer='pillow', fps=5)
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
