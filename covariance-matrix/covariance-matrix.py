import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X=np.asarray(X)
    if X.shape[0]<2 or X.ndim != 2:
        return None
    n,d=X.shape
    mean=np.mean(X,axis=0)
    X_normal=X-mean
    cov=(X_normal.T @ X_normal)/(n-1)
    return cov
