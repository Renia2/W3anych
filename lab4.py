# # zad 1
# plik = open("zadanie1.txt", "w+")
# import random
# list = []
# for i in range(0, 2):
#     x = random.randint(0, 30)
#     list.append(x)
#     print(list)
# wynik = []
# for i in list:
#     x = i * 2
#     wynik.append(x)
#     print(wynik)
# plik.writelines(str(wynik))
# plik.close()

# # zad 2
# plik = open("zadanie1.txt", "r")
# a = plik.readline()
# print(a)
# plik.close()

# # zad 3
# import sys
# with open("zadanie3.txt", "w+") as plik:
#     for i in range(0, 3):
#         tekst = sys.stdin.readline()
#         plik.writelines(str(tekst))
# plik = open("zadanie3.txt", 'r')
# print(plik.readlines())
# plik.close()

# # zad 4
# class NaZakupy:
#     """NaZakupy"""
#     def __init__(self, nazwa_prod, ilosc, jednostka_miary, cena_jd):
#         self.nazwa_prod = nazwa_prod
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jd = cena_jd
#
#     def wyswietl_produkt(self):
#         self.ilosc = str(self.ilosc)
#         self.jednostka_miary = str(self.jednostka_miary)
#         self.cena_jd = str(self.cena_jd)
#         print(self.nazwa_prod + ' ' + self.ilosc + ' ' + self.jednostka_miary + ' ' + self.cena_jd)
#
#     def ile_produktu(self):
#         print(self.ilosc + ' ' + self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         self.jednostka_miary = int(self.jednostka_miary)
#         self.cena_jd = int(self.cena_jd)
#         return str(self.jednostka_miary * self.cena_jd) + ' zl'
#
# kupione = NaZakupy('ziemniaki', 2, 3, 4)
# print(kupione.wyswietl_produkt())
# print(kupione.ile_produktu())
# print(kupione.ile_kosztuje())
