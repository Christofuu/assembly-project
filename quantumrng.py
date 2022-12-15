import qiskit
from qiskit import *
import numpy as np

# Example of a typical psuedo random number generator today
# may appear truly random, actually psuedo random
def classical_dice():

    return np.random.randint(1,7)

print("psuedo random rng example using numpy")
for _ in range(10):
    print(classical_dice())


# Example of true RNG using quantum circuits
# initalize number of qubits
num_qubits = 3
# initialize quantum circuit with 3 qubits
circ = QuantumCircuit(num_qubits, num_qubits)
# apply a Hadmard gate to put the qubits in a superposition state
circ.h(range(num_qubits))
# measure the qubits to make them equally likely to be either 0 or 1
circ.measure(range(num_qubits), range(num_qubits))

# intializing backend simulator to execute circuit on
backend_sim = Aer.get_backend('qasm_simulator')

# run the simulation 512 times
sim = execute(circ, backend_sim, shots=512)
results_sim = sim.result()
counts = results_sim.get_counts(circ)

# the simulated quantum computer includes noise so the results won't be all equal probability
print(counts)

# histogram of the distribution of each number as the program runs
from qiskit.visualization import plot_histogram
plot_histogram(counts)