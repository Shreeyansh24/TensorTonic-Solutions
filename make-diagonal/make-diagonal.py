import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v=np.asarray(v)
    n=len(v)
    diag=np.zeros((n,n))
    for i in range(n):
        diag[i][i]=v[i]
    return diag