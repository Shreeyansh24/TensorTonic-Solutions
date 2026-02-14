import numpy as np
def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    ratings_matrix=np.asarray(ratings_matrix,dtype=float)
    n,m=ratings_matrix.shape
    if mode=="user":
      summ=np.sum(ratings_matrix,axis=1)
      count=np.sum(ratings_matrix!=0,axis=1) 
      avg=summ/np.maximum(count,1)
      for i in range(n):
        for j in range(m):
          if ratings_matrix[i][j]==0:
            ratings_matrix[i][j]=avg[i]
    elif mode=="item":
      summ=np.sum(ratings_matrix,axis=0)
      count=np.sum(ratings_matrix!=0,axis=0) 
      avg=summ/np.maximum(count,1)
      for i in range(n):
        for j in range(m):
          if ratings_matrix[i][j]==0:
            ratings_matrix[i][j]=avg[j]

    return ratings_matrix.tolist()      