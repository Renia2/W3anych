import pandas as pd

# zad 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# zad 2
# print(df[df['Liczba'] > 1000])
#
# print(df[df['Imie'] == 'RENE'])
#
# print(df.agg({'Liczba': ['sum']}))
#
# print(df[df['Rok'] <= 2005].groupby(['Rok']).agg({'Liczba': ['sum']}))
#
# print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))

# print(df.groupby(['Rok', 'Plec'])['Liczba'].max()) popraw

# print(df.groupby(['Plec'])['Liczba'].max()) popraw

# zad 3
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df)

# print(df['Sprzedawca'].unique())

# print(df.nlargest(5, 'Utarg'))

# print(df.groupby(['Sprzedawca'])['idZamowienia'].count().reset_index(name='ilosc zamowien'))

# print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))

# print(df[((df['Kraj'] == 'Polska') & ((df['Data zamowienia'] >= '2005-01-01') &
#           (df['Data zamowienia'] <= '2005-12-31')))].groupby(['Sprzedawca']).agg({'Utarg': ['sum']}))

# print(df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
#       ['Utarg'].mean().round(2))

# df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]\
#     .to_csv('zamowienia_2004.csv', index=False)

# df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))]\
#     .to_csv('zamowienia_2005.csv', index=False)
