import numpy as np


# # zad 1
# a = 4 * (np.arange(1, 21))
# print(a)

# # zad 2
# b = np.arange(5, dtype='float')
# print(b)
# c = b.astype('int32')
# print(c)

# # zad 3
# def poteg2(n):
#     mat = np.arange(1, n*n+1)
#     mat = mat.reshape(n, n)
#     print(2**mat)
#
#
# poteg2(int(input("n: ")))

# # zad 4
# def poteg(n, i):
#     return np.logspace(1, i, num=i, endpoint=True, base=n)
#
#
# print(poteg(int(input("n: ")), int(input("i: "))))

# # zad 5
# def macwek(n):
#     wektor = np.arange(n, 0, -1)
#     print(wektor)
#     mat_diag_k = np.diag(wektor, k=2)
#     print(mat_diag_k)
#
#
# macwek(int(input("n: ")))

# zad 6 zrob

# # zad 7
# def macwielokro(n):
#     a = np.diag(np.linspace(2, 2, num=n, dtype=int))
#     for i in range(n - 1):
#         b = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=i + 1)
#         b = b[:n, :n]
#         c = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=-i - 1)
#         c = c[:n, :n]
#         a = a + b + c
#     return a
#
#
# print(macwielokro(int(input("n: "))))

# # zad 8
# def ciac(n, kierunek):
#     if n % 2 == 1:
#         print("Prosze wpisac parzyste n")
#     else:
#         if n < 0:
#             print("Prosze wpisac dodatnie n")
#         else:
#             macierz = np.arange(1, n * n + 1)
#             macierz = macierz.reshape(n, n)
#             print(macierz)
#             if kierunek == 'poziomo':
#                 print(macierz[:(n // 2)])
#                 print(macierz[(n // 2):])
#             if kierunek == 'pionowo':
#                 print(macierz[:, :(n // 2)])
#                 print(macierz[:, (n // 2):])
#
#
# ciac(int(input("n: ")), input("kierunek: "))

# # zad 9
# a1 = int(input("a1: "))
# r = int(input("r: "))
# n = a1 + 25 * r
# wynik = np.arange(a1, n, r)
# wynik = wynik.reshape(5, 5)
# print(wynik)
