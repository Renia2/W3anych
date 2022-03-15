# zad 1
# ulub_sport = ['5. pilka nozna', '2. plywanie', '1. e-sport', '4. boks', '3. tenis stolowy']
# # '1.' oznacza najwiekszy lubiane, natomiast '5.' oznacza najmniej
# ulub_sport.reverse()
# print(ulub_sport)
# ulub_sport.sort()
# print(ulub_sport)

# zad 2
# skroty = {'WTF': 'What The F**k', 'LOL': 'Laugh out loud', 'IDK': "I don't know"}
# print(skroty[input("skroty: ")])

# zad 3
# ulub_gry = {'Roguelike': 'Enter The Gungeon', 'FPS': 'Payday 2', 'Funny game': 'Human: Fall Flat'}
# print(len(ulub_gry))

# zad 4
# napis = input('Pisz cos: ')
# print(napis.count(input()))

# zad 5
# import sys as system
# a = system.stdin.readline()
# b = system.stdin.readline()
# c = system.stdin.readline()
# wynik = int(a)**int(b)+int(c)
# system.stdout.write(str(wynik))

# zad 6
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a > b & a > c:
#     print("Liczba a jest najwieksza liczba")
# elif a == b == c:
#     print("Liczby sa rowne")
# else:
#     if b > c:
#         print("Liczba b jest najwieksza liczba")
#     else:
#         print("Liczba c jest najwieksza liczba")

# zad 7
# liczb = [2, 4, 1.5, 3.5]
# for i in liczb:
#     wynik = i**2
#     print(wynik)

# zad 8
# liczb = 0
# parzyste = []
# while liczb != 10:
#     if liczb % 2 == 0:
#         parzyste.append(liczb)
#     liczb += 1
# print(parzyste)

# zad 9
# import math
# a = int(input("a: "))
# try:
#     wynik = math.sqrt(a)
#     print("Wynik:", wynik)
# except ValueError:
#     print("Nie liczy pierwiastek z liczby ujemnej")
