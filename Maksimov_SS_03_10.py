#1
'''
Создать объект pandas Series из листа, объекта NumPy, и словаря
'''
import pandas as pd
import numpy as np

my_list = pd.Series([1, 3, 5, 7, 9])
my_array = pd.Series(np.array([1, 2, 3, 4, 5]))
my_dict = pd.Series({'a': 1, 'b' : 2, "c" : 3, "d": 4, "e" : 5})


print(f"Oбъект pandas Series из листa: \n{my_list}")
print(f"Oбъект pandas Series из объекта NumPy: \n{my_array}")
print(f"Объект pandas Series из словаря: \n{my_dict}")

#2
'''
Получить не пересекающиеся элементы в двух объектах Series
'''
import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

itog = series1[~series1.isin(series2)]
print("Непересекающиеся элементы из первого объекта Series:")
print(itog)

itog = series2[~series2.isin(series1)]
print("Непересекающиеся элементы из второго объекта Series:")
print(itog)

#3
'''
Узнать частоту уникальных элементов объекта Series (гистограмма)
'''
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

series = pd.Series([randint(1, 10) for x in range(30)])

value_counts = series.value_counts().sort_index()
print(f"Подсчет уникальных значений:\n{value_counts}")

plt.figure(figsize=(8, 4))
value_counts.plot.bar()
plt.xlabel('Уникальные значения')
plt.xticks(rotation = 0)
plt.ylabel('Частота')
plt.title('Гистограмма частоты уникальных значений')
plt.show()

#4
'''
Объединить два объекта Series вертикально и горизонтально
'''
import pandas as pd

series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])

vertical_concat = pd.concat([series1, series2], axis=0)
print("Объединение вертикально:")
print(vertical_concat)

horizontal_concat = pd.concat([series1, series2], axis=1)
print("Объединение горизонтально:")
print(horizontal_concat)

#5
'''
Найти разность между объектом Series и смещением объекта Series на n
'''
import pandas as pd

n = 2

s = pd.Series([1, 2, 5, 9, 13, 15])
s_shifted = s.shift(n)

print(s - s_shifted)














































