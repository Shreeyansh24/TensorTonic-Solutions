import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos = np.arange(seq_len).reshape(-1, 1)

    # Dimension indices for sine terms: (1, ceil(d_model/2))
    i = np.arange((d_model + 1) // 2).reshape(1, -1)

    # Compute denominator: base^(2i/d_model)
    denom = np.power(base, (2 * i) / d_model)

    # Angles: broadcasted to (seq_len, ceil(d_model/2))
    angles = pos / denom

    # Initialize PE matrix
    pe = np.zeros((seq_len, d_model), dtype=float)

    # Fill even columns with sin
    pe[:, 0::2] = np.sin(angles)

    # Fill odd columns with cos (if they exist)
    if d_model > 1:
        pe[:, 1::2] = np.cos(angles[:, :d_model//2])

    return pe
