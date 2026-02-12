import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    X=np.asarray(X,dtype=float)
    mean=np.mean(X,axis=axis,keepdims=True)
    #std=np.maximum(np.std(X,axis=axis,keepdims=True),eps)
    std = np.std(X, axis=axis, keepdims=True) + eps
    Z=(X-mean)/std
    return Z
    # Write code here
    pass