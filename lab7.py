import numpy as np

# zad 1
# a = np.arange(3).reshape(3, 1)
# b = np.arange(3, 6).reshape(3, 1)
# print(3*a)
# print(4*b)

# zad 2
# a = np.array([[3, 1, 2], [4, 5, 6], [8, 9, 7]])
# b = np.array([[19, 32, 23, 13], [4, 21, 15, 31], [17, 54, 15, 35], [7, 10, 11, 24]])
#
# print(a)
# print("najmniejsza wartosc z 3x3: ")
# i = 0
# for c in range(3):
#     mini = 100
#     for d in a[i, :].flat:
#         if mini > d:
#             mini = d
#     print("w{}: ".format(i+1), mini)
#     mini = 100
#     for d in a[:, i].flat:
#         if mini > d:
#             mini = d
#     print("k{}: ".format(i+1), mini)
#     i += 1
#
# print(b)
# print("najmniejsza wartosc z 4x4: ")
# i = 0
# for c in range(4):
#     mini = 100
#     for d in b[i, :].flat:
#         if mini > d:
#             mini = d
#     print("w{}: ".format(i+1), mini)
#     mini = 100
#     for d in b[:, i].flat:
#         if mini > d:
#             mini = d
#     print("k{}: ".format(i+1), mini)
#     i += 1

# zad 3
# a = np.arange(3).reshape(3, 1)
# b = np.arange(3, 6).reshape(1, 3)
# c = np.dot(a, b)
# print(a)
# print(b)
# print(c)

# zad 4
# a = np.arange(3).reshape(3, 1)
# b = np.arange(3, 6, dtype='float').reshape(3, 1)
# print(3*a)
# print(4*b)

# # zad 5
# mat1 = np.arange(6).reshape(2, 3)
# a = np.sin(mat1)
# print(a)
#
# # zad 6
# mat2 = np.arange(6, 12).reshape(2, 3)
# b = np.cos(mat2)
# print(b)
#
#
# # zad 7
# def dodmac(a, b):
#     return a + b
#
#
# print(dodmac(a, b))

# zad 8
# a = np.arange(9).reshape(3, 3)
# for b in a:
#     print(b)

# zad 9
# a = np.arange(9).reshape(3, 3)
# for b in a.flat:
#     print(b)
#
# zad 10
# a = np.arange(81).reshape(9, 9)
# print(a)
# Mamy możliwości zmiany tylko (1, 81), (3, 27), (27, 3), (81, 1),
# bo ilości liczby w macierze muszą zgadzać się.

# zad 11
# w = np.arange(12)
# print(w)
# kom1 = w.reshape(3, 4)
# kom2 = w.reshape(4, 3)
# kom3 = w.reshape(2, 6)
#
# print("kombinacja 1 - 3x4")
# for a in kom1.flat:
#     print(a)
#
# print("kombinacja 2 - 4x3")
# for b in kom2.flat:
#     print(b)
#
# print("kombinacja 3 - 2x6")
# for c in kom3.flat:
#     print(c)
