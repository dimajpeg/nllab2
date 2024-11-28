import numpy as np

# Исходные массивы
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])

# Вычисление уникальных значений, которые находятся только в одном из массивов
exclusive_or_result = np.setxor1d(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("\nУникальные значения, которые есть только в одном (а не в обоих) входных массивах:")
print(exclusive_or_result)
