import numpy as np
import pandas as pd

XT = np.array(
    [
        [+1, +1, +1],
        [+1, +1, -1],
        [+1, -1, +1],
        [+1, -1, -1],
        [-1, +1, +1],
        [-1, +1, -1],
        [-1, -1, +1],
        [-1, -1, -1],
    ]
)
y_rule_110 = np.array([+1, -1, -1, -1, +1, -1, -1, +1])
y_rule_126 = np.array([+1, -1, -1, -1, -1, -1, -1, +1])


def map_to_psi(x):
    x1, x2, x3 = x
    return np.array([1, x1, x2, x3, x1 * x2, x1 * x3, x2 * x3, x1 * x2 * x3])


def solve_least_squares(XT_psi, y_rule):
    w_star, _, _, _ = np.linalg.lstsq(XT_psi, y_rule, rcond=None)
    y_hat = XT_psi @ w_star
    return pd.DataFrame({"Original y": y_rule, "Predicted y_hat": y_hat})


# solve the lsq for XT
print("# Solving LSQ for XT using rule 110 and 126")
print(f"XT=\n{XT}")
print(f"rule=110\n {solve_least_squares(XT, y_rule_110)}")
print(f"rule=126\n {solve_least_squares(XT, y_rule_126)}")

# map XT to psi representation
XT_psi = np.array([map_to_psi(row) for row in XT])

# solve the lsq for XT_psi
print("\n# Solving LSQ for XT_psi using rule 110 and 126")
print(f"XT_psi=\n{XT_psi}")
print(f"rule=110\n {solve_least_squares(XT_psi, y_rule_110)}")
print(f"rule=126\n {solve_least_squares(XT_psi, y_rule_126)}")
