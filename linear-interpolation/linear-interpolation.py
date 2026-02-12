def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    n=len(values)
    for i in range(n):
        if values[i]==None:
            left=i-1
            for j in range(i+1,n):
                if values[j]==None:
                    continue
                else:
                    right=j
            values[i]=values[left]+1/(right-left)*(values[right]-values[left])

        else:
            continue
    return values