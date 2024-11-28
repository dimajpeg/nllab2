import numpy as np

# Исходный массив
array = np.array([[0, 10, 20],
                  [20, 30, 40]])

# Условие для нахождения элементов больше 10
values_greater_than_10 = array[array > 10]

# Получение индексов элементов, которые больше 10
indices = np.where(array > 10)

print("Исходный массив:")
print(array)

print("\nЗначения больше 10:", values_greater_than_10)
print("Их индексы:", indices)
