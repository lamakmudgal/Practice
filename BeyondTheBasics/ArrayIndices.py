import numpy as np
a = np.array([1,2,34,44,555,6,7,8,9,11,12,13,14,15,16,17])
p = np.percentile(a, 50)  #Returns 50th percentile, e.g. median
print(p)