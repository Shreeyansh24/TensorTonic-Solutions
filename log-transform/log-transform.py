import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    transform=[math.log(1+x) for x in values]
    return transform
    # Write code here