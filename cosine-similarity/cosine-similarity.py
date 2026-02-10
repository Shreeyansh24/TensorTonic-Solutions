import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a=np.array(a)
    b=np.array(b)
    if len(a)!=len(b):
        return 0.0
    if np.linalg.norm(a)==0 or np.linalg.norm(b)==0:
        return 0.0
    sim=float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    return sim
