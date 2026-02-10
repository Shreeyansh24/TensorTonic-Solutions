import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    try:
        X = np.asarray(matrix, dtype=float)
    except Exception:
        return None

    if X.ndim != 2:
        return None

    if norm_type not in ('l1', 'l2', 'max'):
        return None

    try:
        if norm_type == 'l2':
            norms = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))
        elif norm_type == 'l1':
            norms = np.sum(np.abs(X), axis=axis, keepdims=True)
        else:  # max norm
            norms = np.max(np.abs(X), axis=axis, keepdims=True)
    except Exception:
        return None

    # Avoid division by zero
    norms[norms == 0] = 1.0

    return X / norms