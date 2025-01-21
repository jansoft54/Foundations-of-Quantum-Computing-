import numpy as np

# re-use definitions from 6.1
from task_6_1 import *

phi_plus = (CNOT(1, 2) @ np.kron(matH, matI)) @ np.kron(ket0, ket0)
phi_minus = (CNOT(1, 2) @ np.kron(matH, matI)) @ np.kron(ket1, ket0)
psi_plus = (CNOT(1, 2) @ np.kron(matH, matI)) @ np.kron(ket0, ket1)
psi_minus = (CNOT(1, 2) @ np.kron(matH, matI)) @ np.kron(ket1, ket1)

print(f"phi_plus:  {qr2str(phi_plus)}")
print(f"phi_minus: {qr2str(phi_minus)}")
print(f"psi_plus:  {qr2str(psi_plus)}")
print(f"psi_minus: {qr2str(psi_minus)}")
