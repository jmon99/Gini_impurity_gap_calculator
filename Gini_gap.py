import numpy as np

#Calculate p values 𝑝̂_𝑗𝑦 = ∑𝑘:𝑥𝑘∈𝑅𝑗1[𝑦𝑖=𝑦]i / ∑𝑘:𝑥𝑘∈𝑅𝑗

def p(X):
  p_vals = []
  labels, counts = np.unique(X[:,-1], return_counts = 1)
  #print(labels, counts)
  size_X = np.size(X)

  for i in range(size_X):
    print(np.where(labels == 1))
    #p = counts[np.where(labels == X[i, -1])/size_X]
    #p_vals.append(p)

  return p_vals
    
