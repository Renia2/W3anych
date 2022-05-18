import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zad 1 i 2
# x = np.arange(1, 20)
# y = 1/x
# plt.plot(x, y, color='green', linestyle='dotted',  marker='>'
#          , markerfacecolor='green', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x[1,20]')
# plt.legend()
# plt.axis([0, 20, 0, 1])
# plt.show()

# zad 3
# x1 = np.arange(0, 30, 0.1)
# x2 = np.arange(0, 30, 0.1)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-', label='f(x) = sin(x)')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.legend()
# ax = plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-', label='f(x) = cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.legend()
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# zad 4

# # zad 5
# df = pd.read_excel('imiona.xlsx', header=0)
# # wykres 1
# etykiety_plci = ['K', 'M']
# wartosci_ur_plec = df.groupby(['Plec'])['Liczba'].sum().values
# plt.subplot(1, 3, 1)
# plt.bar(x=etykiety_plci, height=wartosci_ur_plec, color=['orange'], label='Liczba urodzonych')
# plt.xticks(etykiety_plci, rotation=0)
# plt.xlabel('Plec')
# plt.ylabel('Liczba urodzonych')
# plt.legend()
# # wykres 2
# etykiety = df['Rok'].unique()
# wartosci_M = df[df['Plec'] == 'M'].groupby(['Rok']).sum().values
# wartosci_K = df[df['Plec'] == 'K'].groupby(['Rok']).sum().values
# plt.subplot(1, 3, 2)
# plt.plot(etykiety, wartosci_M, 'b', label='Mezczyzn')
# plt.plot(etykiety, wartosci_K, 'r', label='Kobiet')
# plt.xticks(etykiety, rotation=90)
# plt.xlabel('Rok')
# plt.ylabel('Liczba urodzonych')
# plt.legend()
# # wykres 3
# wartosci_ur_rok = df.groupby(['Rok'])['Liczba'].sum().values
# plt.subplot(1, 3, 3)
# plt.bar(x=etykiety, height=wartosci_ur_rok, color='green')
# plt.xticks(etykiety, rotation=90)
# plt.xlabel('Rok')
# plt.ylabel('Liczba urodzonych')
# plt.legend(['Liczba urodzonych dzieci'])
# plt.subplots_adjust(wspace=0.5)
# plt.show()

# zad 6
df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa = df2.groupby(['Sprzedawca'])['Utarg'].sum()
explode = (0, 0, 0, 0, 0, 0, 0, 0.2, 0)
grupa.plot(kind='pie', subplots=True, explode=explode, autopct='%.2f%%', shadow=True)
plt.title('Suma zamowien')
plt.show()