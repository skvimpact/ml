import numpy as np
A = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])

# print(A.shape)
# print(A[1:2, 1:2])
# print(A[1:, 1:])


# print(np.zeros((3, 5)))

# print(A - 2)

# M1 = np.ones((3, 6))
# print(M1)
# print(M1.T)
M1 = np.array(
   [[1,2],
    [3,4],
    [5,6],
    [7,8]]
)
M2 = np.array(
    [
        [1, 2, 3],
        [5, 4, 3],
        [2, 0, 1]
    ]
)
# M2 = np.array([
#    [1,2],
#    [3,4]
# ])
# print(M1)
# print(M2)
# M3 = M2

M4 = np.linalg.inv(M2)
print(M4)
# print(M4)
print(M2 @ M4)