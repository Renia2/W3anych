# zad 1
a = "computer"
b = "games"
c = 3
d = 5
e = 6.2
f = 2.1
g = complex(1, 2)
h = 2 + 4j
print(a, b)
print(c, d)
print(e, f)
print(g, h)

# zad 2
ii = int(input("ii: "))
jj = int(input("jj: "))
operacja = input("operacja: ")
if operacja == "+":
    wynik = ii + jj
    print("Wynik:", wynik)
elif operacja == "-":
    wynik = ii - jj
    print("Wynik:", wynik)
elif operacja == "*":
    wynik = ii * jj
    print("Wynik:", wynik)
elif operacja == "/":
    wynik = ii / jj
    print("Wynik:", wynik)
else:
    print("To nie jest operacja")

# zad 3
k, l, m, n, o, p = 1, 1, 1, 1, 1, 1
for i in range(0, 5, 1):
    k += 2
    l -= 2
    m *= 2
    n /= 2
    o **= 2
    p %= 2
print(k, l)
print(m, n)
print(o, p)

# zad 4
import math
from math import e
print(e**10)
print(math.log((5+math.sin(8)**2))**(1/6))
print(math.floor(3.55))
print(math.ceil(4.80))

# zad 5
im1 = "RENE"
naz1 = "MAKSIMIUK"
txt1 = im1.capitalize() + " " + naz1.capitalize()
print(txt1)

# zad 6
pios = "Rice is amazing, it's a problem if I don't have it " \
    "Rice is a staple food, after all "
txt2 = pios.count("Rice")
print(txt2)

# zad 7
naz2 = "Maksimiuk"
print(naz2[1], naz2[len(naz2)-1])

# zad 8
txt3 = pios.split()
print(txt3)

# zad 9
napis = "Napis"
r = 1.5
s = 10
print(napis, "{0:.2f} {1:2X}".format(r, s))