# a = 6
# b = 5
#
# if a > b:
#     print("liczba a jest wieksza od b")
# elif a < b:
#     print("liczba a jest mniejsza od liczba b")
# else:
#     print("liczby są równe")

# a = input('wczytaj liczbę: ')
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))

# a = input('wczytaj liczbę: ')
# b = input('wczytaj liczbę: ')
# c = input('wczytaj liczbę: ')
# d = input('wczytaj liczbę: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a>b) & (c>d):
#     print("liczba a jest od liczby b i liczba c jest wieksza od liczby d")
# else:
#     print("liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d")

# for a in range(0, 7, 1):
#     print(a)

# lista = ['a', 3, 4, 5.6]
# for a in lista:
#     print(a)
# else:
#     print("wyśietlone zostały elementy z listy")

# licznik = 0
# while licznik != 11:
#     print(licznik)
#     licznik += 1

# lista = [4, 6, 2, 5, 3, 9, 8, 7]
# a = input("Podaj liczbę: ")
# licznik = 0
# while licznik != len(lista):
#     if int(a) - lista[licznik] == 0:
#         print("liczba " + str(a) + '-' + str(lista[licznik]) + '= 0')
#         break
#     else:
#         licznik += 1
# else:
#     print("żadna z wartości nie dała odpowiedniego wyniku")

# lista1 = [4, 6, 3, 2, 7, 9, 5, 1]
# lista2 = [4, 7, 5, 3]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# a = input ("pierwsza liczba: ")
# b = input ("druga liczba: ")
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie dzieli się przez 0")
# except ValueError:
#     print("nie wczytano liczby całkowitej")

żarcie = {
    "kebab": 1,
    "frytki": 2,
    "nachos": 3,
    "pizza": 4,
}
a = input ("wpisz zarcie: ")
print(żarcie[a])