import numpy as np
import scipy.linalg as la

N = 5
A = np.zeros(shape = (N,N))
for i in range(0,5):
  A[0][i] = i+1
  A[i][0] = i+1
eigvals, eigvecs = la.eig(A)
print(eigvals)

N = 10
A = np.zeros(shape = (N,N))
for i in range(0,10):
  A[0][i] = i+1
  A[i][0] = i+1
eigvals, eigvecs = la.eig(A)
print(eigvals)
