from sympy.physics.quantum import qapply
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.gate import H as gateH
from sympy.physics.quantum.gate import CNOT as gateCNOT
from sympy.physics.quantum.gate import IdentityGate as gateI


def bell_state(qr: Qubit):
    return (gateCNOT(1, 0) * (gateH(1) * gateI(0))) * qr


print("# without qapply")
for cbX2 in [0, 1]:
    for cbX1 in [0, 1]:
        qrX = Qubit(cbX1, cbX2)
        print(f"input={qrX}  ->  output={bell_state(qrX)}")


print("\n# with qapply")
for cbX2 in [0, 1]:
    for cbX1 in [0, 1]:
        qrX = Qubit(cbX1, cbX2)
        print(f"input={qrX}  ->  output={qapply(bell_state(qrX))}")
