import numpy as np

def luDecomposition(A):
    L = np.tril(A, k=-1) + np.eye(A.shape[0])
    U = np.triu(A)
    return L, U
    