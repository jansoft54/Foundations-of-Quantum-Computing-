import itertools
import numpy as np
import random
n = 3
data = np.arange(0,n)
x = np.array([random.choice([-1, 1]) for _ in range(n)])

comb = [list(itertools.combinations(data,i)) for i in range(1,n+1)]
comb = [list(i) for v in comb for i in v]
print("Indices: ",comb)
psi = [1] + [np.prod(x[i]) for i in comb]
print("X: ",x)
print("PSI: ",psi)

