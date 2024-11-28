import numpy as np

# Заданные массивы
array1 = np.array([1.0, 2.0, 3.0, 4.0])
array2 = np.array([1.0, 2.1, 3.0, 4.0])

# Сравнение на равенство по элементам
equal_elements = np.equal(array1, array2)

# Сравнение на равенство в пределах допуска (например, допускаемая погрешность 0.1)
tolerance = 0.1
close_elements = np.isclose(array1, array2, atol=tolerance)

print("Массив 1:", array1)
print("Массив 2:", array2)

print("\nПоэлементное сравнение на равенство:")
print(equal_elements)

print("\nПоэлементное сравнение на равенство в пределах допуска:")
print(close_elements)
