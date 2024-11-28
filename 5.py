import numpy as np

# Пример массива
x = np.arange(4, dtype=np.int64)

# Создание нового массива из 10 с той же формой и типом, что и x
result = np.full_like(x, 10)

print("Исходный массив:")
print(x)

print("\nМассив из 10 с такой же формой и типом:")
print(result)
