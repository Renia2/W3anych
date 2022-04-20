import numpy as np
import pandas as pd

# s = pd.Series([1, 3, 5.5, np.nan, 'a'])
# print(s)

s1 = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s1)

dane = {'Kraj': ["Belgia", 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [12432123, 324123456, 1513512345]}
# print(dane)
df = pd.DataFrame(dane)
print(df)

# daty = pd.date_range('20220420', periods=5)
# df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df2)

# df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# print(df)
# df.to_csv('nowy.csv', index=False)
#
# xlsx = pd.ExcelFile('wyniki.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('nowy.xlsx', sheet_name='arkusz1', index=False)

# print(s1['a'])
# print(s1.a)
#
# print(df['Stolica'])
# print(df.iloc[[0], [0]])
# print(df.loc[[0], ['Kraj']])
# print(df.at[0, 'Kraj'])
#
# print('kraj: ' + df.Kraj)
#
# print(df.sample(1))
# print(df.sample(2))
#
# print(df.sample(frac=0.5))
#
# print(df.sample(10, replace=True))
#
# print(df.head())
# print(df.head(1))
# irisdf = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# print(irisdf)
# print(irisdf.head(10))
# print(irisdf.tail(10))

# print("")
# print(s1)
# print(s1[(s1 > 9)])
#
# print(s1.where(s1 > 10, 'elementy za mały'))
# seria = s1.copy()
# print(seria)
# seria.where(seria > 10, 'elementy za mały', inplace=True)
# print(seria)

# print(s1[~(s1 > 10)])
# print(s1[(s1 < 13) & (s1 > 8)])

# print(df[df['Populacja'] > 1242315125])
# print(df[((df.Populacja > 124321230) & (df.index.isin([0, 2])))])
#
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))

s1['e'] = 15
print(s1)

df.loc[3] = 'nowy element'
df.loc[4] = ['Polska', 'Warszawa', 35697482]
print(df)
df.drop([3], inplace=True)
print(df)
# df.drop('Kraj', axis=1, inplace=True)
# print(df)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

print(df.sort_values(by='Kraj'))

grupa = df.groupby(['Kontynent'])
print(grupa.get_group('Europa'))

print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))