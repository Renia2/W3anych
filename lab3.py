# # zad 1
# a = [1-x for x in range(0, 10)]
# print(a)
# b = [4**x for x in range(0, 8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# # zad 2
# import random
# lista1 = []
# for x in range(0, 10, 1):
#     x = random.randint(0, 10)
#     lista1.append(x)
# print(lista1)
# lista2 = [i for i in lista1 if i % 2 == 0]
# print(lista2)

# # zad 3
# towary = {'maka': 'kg', "woda": 'litr', 'makaron': 'kg', "lizak": 'sztuki'}
# towary_sztuki = [a for (a, b) in towary.items() if b == 'sztuki']
# print(towary_sztuki)

# # zad 4
# def trojprostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         print("Ten trojkat jest prostokatny")
#         return 1
#     else:
#         print("Ten trojkat nie jest prostokatny")
#         return 0
#
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print(trojprostokatny(a, b, c))


# # zad 5
# def poletrapezu(a=0, b=0, h=0):
#     return ((a + b) * h) / 2
#
#
# print(poletrapezu())
# print(poletrapezu(6.5, 5.5, 2.5))

# # zad 6
# def ciag(a=1, b=4, ile=10):
#     wynik = a
#     element = []
#     for x in range(ile):
#         x = a + x * b
#         element.append(x)
#         wynik *= x
#     print(element)
#     return wynik
#
#
# print(ciag())
# print(ciag(1, 1, 5))

# # zad 7
# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         wynik = 1
#         for x in liczby:
#             wynik *= x
#         return wynik
#
#
# print(ciag(1, 5, 9, 13))

# # zad 8
# def zakupy(**towary):
#     koszt = 0
#     ilosc = 0
#     for key, value in towary.items():
#         ilosc += 1
#         koszt += value
#     print("ilosc: ", ilosc)
#     print("koszt: ", koszt)
#
#
# zakupy(mleko=2, kakao=3, chleb=2, szynka=4)


# # zad 9
# from ciagi import *
#
# ciag_ary.wzory()
# ciag_geo.wzory()
# print(ciag_geo.dzialanie(2, 2, 4))
# print(ciag_ary.dzialanie(2, 2, 4))
