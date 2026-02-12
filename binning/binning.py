import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    values=np.asarray(values)
    if len(values) == 0:
        return []
    maxi=np.max(values)
    mini=np.min(values)
    category = np.zeros(len(values))
    if maxi==mini:
        return list(category)
    width=(maxi-mini)/num_bins
    for i in range(len(values)):
        category[i]=min(int((values[i]-mini)/width),num_bins-1)
    return list(category)