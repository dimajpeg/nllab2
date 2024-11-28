import numpy as np

# Исходный массив
array = np.array([[0, 1],
                  [2, 3]])

# Уплощение массива
flattened_array = array.flatten()

# Нахождение максимального и минимального значений
max_value = flattened_array.max()
min_value = flattened_array.min()

print("Оригинальный сплющенный массив:")
print(flattened_array)

print("\nМаксимальное значение вышеуказанного сплющенного массива:")
print(max_value)

print("Минимальное значение вышеуказанного сплющенного массива:")
print(min_value)
