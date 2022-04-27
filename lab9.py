import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx', header=0)

# zad 1
# lista = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres = grupa.plot(xticks=lista, figsize=(10, 6))
# wykres.tick_params(axis='x', labelrotation=90)
# plt.show()

# zad 2
# grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Plec')
# wykres.set_ylabel('Liczba urodzonych w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend(['Liczba urodzonych'])
# plt.show()

# zad 3
grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})