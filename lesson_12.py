import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
#2
'''
Посчитать среднюю доходность женщин
'''

file = '/home/albemute/Polytech-tasks/Mall_Customers.csv'
df = pd.DataFrame()

df = pd.read_csv(file, delimiter=',', index_col=None)
df = df.set_index("Genre")
df = df.groupby(level = "Genre").mean()

print(df.head(15))
print('Средняя доходность женщин: ', df.iloc[0]['Annual Income (k$)'])

#3
'''
Определить у обеих полов людей с бОльшими расходами;
'''

file = '/home/albemute/Polytech-tasks/Mall_Customers.csv'
df = pd.DataFrame()

df = pd.read_csv(file, delimiter=',', index_col=None)
df = df.set_index("Genre")
df = df.groupby(level = 'Genre').max()

print(df.head(15))
print('Люди с большими расходами у женщин, ее CustomerID: ', df.iloc[0]['CustomerID'])
print('Люди с большими расходами у мужчин, его CustomerID: ', df.iloc[1]['CustomerID'])

#4
'''
Построить график зависимости доходов от возраста для мужчин;
'''

file = '/home/albemute/Polytech-tasks/Mall_Customers.csv'
df = pd.DataFrame()

df = pd.read_csv(file, delimiter=',', index_col=None)
df = df.set_index("Genre")

male_template = df.where(df['Genre'] == 'Male')
df = df.where(df('Genre') == 'Male').dropna()

plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.figsize'] = [10, 6]
plt.scatter(df['Annual Income (k$)'].tolist, df['Age'].tolist)
plt.show()
#male_template = df.where(df('Genre') == 'Male')
#df = df.where(df('Genre') == 'Male').dropna()
#plt.scater(df[''].tolist, df[''.tolist])






