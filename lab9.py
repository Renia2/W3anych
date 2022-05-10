import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx', header=0)
df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

# zad 1
# lista = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres = grupa.plot(xticks=lista, figsize=(10, 6))
# wykres.tick_params(axis='x', labelrotation=90)
# wykres.legend(['Liczba urodzonych dzieci'])
# plt.show()

# zad 2
# grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Plec')
# wykres.set_ylabel('Liczba urodzonych w mln')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend(['Liczba urodzonych'])
# plt.show()

# zad 3
# grupa = df[df['Rok'] > 2011].groupby(['Plec']).agg({'Liczba': ['sum']})
# grupa.plot(kind='pie', subplots=True, fontsize=20, autopct='%.2f%%', figsize=(6, 6),
# colors=['red', 'blue'])
# plt.title('Liczba urodzonych w 5 ostatnich latach')
# plt.show()

# zad 4
grupa = df2.groupby(['Sprzedawca'])['idZamowienia'].count()
wykres = grupa.plot.bar()
wykres.set_xlabel('Sprzedawcy')
wykres.set_ylabel('Ilosc zamowien')
wykres.tick_params(labelrotation=45)
wykres.legend(['Ilosc zamowien'])
plt.show()
