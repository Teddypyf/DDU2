import numpy as np

a = np.random.rand(3, 3, 3)
print(a)
a = np.round(a)
a = a.astype(int)
print(a)
