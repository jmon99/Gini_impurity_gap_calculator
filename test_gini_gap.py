import numpy as np
from Gini_gap import p
#test p value

X = np.array([[4,2,3],[2,3,1],[3,4,1], [4,1,2], [2,4,3]])
print(p(X), "ans: 2/5, 2/5, 1/5")

