'''
#1
import pandas as pd

my_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(my_list)
print(series_from_list)

import numpy as np
import pandas as pd

my_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(my_array)
print(series_from_array)

import pandas as pd

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(my_dict)
print(series_from_dict)

#2
import pandas as pd

# Создание двух объектов Series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

# Получение непересекающихся элементов из первого объекта Series
series1_difference = series1.difference(series2)
print("Непересекающиеся элементы из первого объекта Series:")
print(series1_difference)

# Получение непересекающихся элементов из второго объекта Series
series2_difference = series2.difference(series1)
print("Непересекающиеся элементы из второго объекта Series:")
print(series2_difference)

#3
import pandas as pd

# Создание объекта Series
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])

# Получение частоты уникальных элементов
value_counts = series.value_counts()
print(value_counts)

value_counts_normalized = series.value_counts(normalize=True)
print(value_counts_normalized)

#4
import pandas as pd

# Создание двух объектов Series
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])

# Объединение вертикально
vertical_concat = pd.concat([series1, series2], axis=0)
print("Объединение вертикально:")
print(vertical_concat)

import pandas as pd

# Создание двух объектов Series
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])

# Объединение горизонтально
horizontal_concat = pd.concat([series1, series2], axis=1)
print("Объединение горизонтально:")
print(horizontal_concat)

#5
import pandas as pd

# Создаем объект Series
s = pd.Series([10, 20, 15, 30, 25])

# Находим разность между s и s смещенным на 2
diff = s.diff(2)

print(diff)
'''
import pandas as pd

n = 2
series = pd.Series([1, 5, 7, 8, 12, 15, 17])
difference = series.diff(periods=n)

print(difference)








