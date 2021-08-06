import numpy as np
v1 = np.array([4, 3])
c = np.linalg.norm(v1)
print(c)
print(np.sqrt(sum(v1 ** 2)))
v1 = np.array([2, 2, 3])
v2 = np.array([3, 2, 10])
print(v1 @ v2)
print(v1 * v2)
v1 = np.array([400000, np.sqrt(8 ** 2 - 4 ** 2)])
print(np.sqrt(8 ** 2 - 4 ** 2))
v2 = np.array([100000, 0])

print((v1 @ v2)/(np.linalg.norm(v1) * np.linalg.norm(v2)))
