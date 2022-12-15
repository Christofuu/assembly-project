# This code uses the Quantum Fourier Transform (QFT) to implement Schor's algorithm, which is a quantum algorithm for factoring large numbers. 
# It takes a number n as input and returns one of the factors of n if it exists. Otherwise, it returns 0.
# Import the necessary modules from Qiskit
import qiskit
from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.algorithms import Shor

backend = Aer.get_backend("qasm_simulator")

factors = Shor(execute(backend, shots = 100, skip_qobj_validation=False))

n = int(input("Enter a number to be factored"))
a = int(input("Enter a guess smaller than target number"))

result_dict = factors.factor(N=n, a=a)
result = result_dict.factors

print(result)