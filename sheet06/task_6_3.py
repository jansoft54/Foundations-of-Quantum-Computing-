from sympy.physics.quantum import qapply
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.gate import CNOT as gateCNOT

wireX1 = 1
wireX2 = 0

qcCNOT12 = gateCNOT(wireX1, wireX2)
qcCNOT21 = gateCNOT(wireX2, wireX1)

print("CNOT 1->2")
for cbX1 in [0, 1]:
    for cbX2 in [0, 1]:
        qrX = Qubit(cbX1, cbX2)
        qrY = qapply(qcCNOT12 * qrX)
        print(qrX, " -> ", qrY)


# ----- actual solution starts here -----

print("CNOT 2->1")
for cbX1 in [0, 1]:
    for cbX2 in [0, 1]:
        qrX = Qubit(cbX1, cbX2)
        qrY = qapply(qcCNOT21 * qrX)
        print(qrX, " -> ", qrY)
