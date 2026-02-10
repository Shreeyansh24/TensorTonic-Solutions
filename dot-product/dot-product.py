import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x=np.asarray(x)
    y=np.asarray(y)
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError
    if len(x)!=len(y):
        raise ValueError 
    dot=float(np.sum(x*y))
    return dot