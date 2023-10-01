import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

b = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])

o = np.dot(a, b)

print(o)

# Prøv at lave en en såkaldt identitetsmatrice med 1'taller på diagonalen.

i = np.eye(5)
print(i)
