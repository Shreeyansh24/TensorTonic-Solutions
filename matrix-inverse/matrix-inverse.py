import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A=np.array(A)
    if A.ndim != 2:
        return None
    n, m = A.shape
    if n != m:
        return None
    if np.isclose(np.linalg.det(A), 0):
        return None

    try:
        A_inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None

    # Verify numerically: ||A A^{-1} - I|| < 1e-7
    I = np.eye(n)
    err = np.linalg.norm(A @ A_inv - I)

    if err >= 1e-7:
        return None

    return A_inv
