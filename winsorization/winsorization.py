import math
def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    values=sorted(values)
    n=len(values)
    upper_index=(n-1)*upper_pct/100
    lower_index=(n-1)*lower_pct/100
    upper_val=values[math.floor(upper_index)]+(upper_index-math.floor(upper_index))*(values[math.ceil(upper_index)]-values[math.floor(upper_index)])
    lower_val=values[math.floor(lower_index)]+(lower_index-math.floor(lower_index))*(values[math.ceil(lower_index)]-values[math.floor(lower_index)])  
    for i in range(n):
      if values[i]<lower_val:
        values[i]=lower_val
      elif values[i]>upper_val:
        values[i]=upper_val
    return values