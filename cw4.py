import numpy as np

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# d = np.array([2.5, 65.2, 45.2, 2.6])
# c = a + b
# print(c)
# print(b**2)
# e = d + a
# print(e)
# print(e.dtype)

# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))

# a = np.arange(3)
# b = np.arange(3)
#
# print(a)
# print(b)
#
# c = a.dot(b)
# print(c)
#
# d = np.array([[3, 2, 4], [5, 2, 4]])
# e = np.array([[2, 3], [6, 3], [2, 5]])
# print(e.dot(d))

# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))

a = np.arange(6).reshape((3, 2))
print(a)
for b in a.flat:
    print(b)

# a = np.arange(12)
# print(a)
# b = a.reshape((3, 4))
# print(b)
# c = a.reshape((4, 3))
# print(c)
# d = b.ravel()
# print(d)
# e = b.T
# print(e)
