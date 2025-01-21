import numpy as np

ket0 = np.array([1, 0])
ket1 = np.array([0, 1])
matI = np.array([[1, 0], [0, 1]])
matX = np.array([[0, 1], [1, 0]])
matH = np.array([[+1, +1], [+1, -1]]) / np.sqrt(2)


def CNOT(ctrl=1, trgt=2):
    if ctrl == 2 and trgt == 1:
        matC = np.kron(matI, np.outer(ket0, ket0))
        matT = np.kron(matX, np.outer(ket1, ket1))
    else:
        matC = np.kron(np.outer(ket0, ket0), matI)
        matT = np.kron(np.outer(ket1, ket1), matX)
    return matC + matT


def qr2str(qr):
    num2ketstr = {0: "|00>", 1: "|01>", 2: "|10>", 3: "|11>"}
    numbrs = np.where(qr != 0)[0]
    coeffs = qr[numbrs]
    k_strs = [num2ketstr[n] for n in numbrs]
    c_strs = ["" if c == 1 else "%f " % np.abs(c) for c in coeffs]
    s_strs = [" + " if c > 0 else " - " for c in coeffs]

    if s_strs[0] == " + ":
        s_strs[0] = ""

    return "".join([s + c + k for (s, c, k) in zip(s_strs, c_strs, k_strs)])


# ----- actual solution starts here -----


def test_cnot_gate(matCNOT):
    for x1 in [ket0, ket1]:
        for x2 in [ket0, ket1]:
            x = np.kron(x1, x2)
            y = matCNOT @ x
            print(qr2str(x), qr2str(y))


matCNOT12 = CNOT(1, 2)
matCNOT21 = CNOT(2, 1)

print("# CNOT 1->2")
print(f"matrix:\n{matCNOT12}")
print("truth table:")
test_cnot_gate(matCNOT12)

print("\n# CNOT 2->1")
print(f"matrix:\n{matCNOT21}")
print("truth table:")
test_cnot_gate(matCNOT21)
