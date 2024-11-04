import numpy as np
import numpy as np
from numpy.linalg import inv
n = 3
def compute_F(n):

    j = np.arange(2 ** n) 
    k = np.arange(2 ** n)  
    
    J, K = np.meshgrid(j, k, indexing='ij')  
    
    constant = np.sqrt(1 / (2 ** n))
    
    exponent = 1j * 2 * np.pi * J * K / (2 ** n)
    exponential = np.exp(exponent)
    
    F = constant * exponential
    
    return F
#a) (compute_F(n))
#b) f_110 = F_3w_110 <=> F_3^-1 f_110 = w_110
f_110 = np.array([1,-1,-1,-1,1,-1,-1,1])
f_126 = np.array([1, -1, -1, -1, -1, -1, -1, 1])

F = compute_F(n)
F_inv = inv(F)
w_110 = F_inv @ f_110
w_126 = F_inv @ f_126

f_r_110 = (F @ w_110).real
f_r_126 = (F @ w_126).real

#c)
#We compute X = Wx where W is the Fourier matrix and X (our case w) is the DFT of the signal. x is the input signal, f_xxx.
w_110 = np.fft.fft(f_110) / np.sqrt(2**n)
w_126 = np.fft.fft(f_126) / np.sqrt(2**n)

f_r_110 = (F @ w_110).real
f_r_126 = (F @ w_126).real

#print(f_r_126)
#d)
F_1 = compute_F(1)
F_2 = compute_F(2)
F_3 = compute_F(3)
F_4 = compute_F(4)

F_1_c = F_1.conj().T
F_2_c = F_2.conj().T
F_3_c = F_3.conj().T
F_4_c = F_4.conj().T

#print((F_2_c @ F_2).real)

#Observation: F_i_c @ F_i is the identity matrix of size 2**i <=> F_i is unitary <=> rows and colums vectors are orthonormal.
# As F_i is unitary F^-1 exists with  F_i.conj().T. Therefore  every 2**i-dimensional vector has a Fourier transform.
