import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# Вихідні дані: функція та точки
x = np.linspace(0, np.pi, 15)  # 15 рівномірно розподілених точок на [0, π]
y = np.sin(x)

# Побудова кубічного інтерполяційного сплайна
spline = CubicSpline(x, y, bc_type='natural')

# Точки для побудови графіків
x_dense = np.linspace(0, np.pi, 500)  # Більше точок для гладких графіків
y_dense = spline(x_dense)  # Значення сплайна
dy_dense = spline(x_dense, 1)  # Перша похідна
d2y_dense = spline(x_dense, 2)  # Друга похідна

# Графіки
plt.figure(figsize=(12, 8))

# Графік функції та сплайна
plt.subplot(3, 1, 1)
plt.plot(x_dense, np.sin(x_dense), label="Початкова функція: sin(x)", color="blue")
plt.plot(x_dense, y_dense, label="Кубічний сплайн", color="orange", linestyle="--")
plt.scatter(x, y, color="red", label="Точки значень")
plt.title("Інтерполяція кубічного сплайну")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

# Графік першої похідної
plt.subplot(3, 1, 2)
plt.plot(x_dense, dy_dense, label="Перша похідна кубічного сплайну", color="purple", linestyle="--")
plt.title("Перша похідна")
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.legend()
plt.grid()

# Графік другої похідної
plt.subplot(3, 1, 3)
plt.plot(x_dense, d2y_dense, label="Друга похідна кубічного сплайну", color="magenta", linestyle="--")
plt.title("Друга похідна")
plt.xlabel("x")
plt.ylabel("d²y/dx²")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Виведення коефіцієнтів сплайна
coefficients = spline.c.T  # Коефіцієнти поліномів у правильному порядку
#print("Коефіцієнти сплайна (для кожного сегмента):\n", coefficients)

# Перевірка значень у точках
for i in range(len(x)):
    assert np.isclose(spline(x[i]), y[i])

# Перевірка граничних умов (для природного сплайна)
assert np.isclose(spline(x[0], 2), 0)
assert np.isclose(spline(x[-1], 2), 0)

# Обчислення максимальної похибки
x_test = np.linspace(0, np.pi, 1000)
y_test = np.sin(x_test)
y_spline_test = spline(x_test)
max_error = np.max(np.abs(y_test - y_spline_test))
print("Максимальна похибка:", max_error)

# Створення списку інтервалів
intervals = [(x[i], x[i+1]) for i in range(len(x)-1)]

# Створення DataFrame з коефіцієнтами та інтервалами
data = {
    'Сегмент': range(1, len(x)),
    'Інтервал': intervals,
    'a': coefficients[:, 3],
    'b': coefficients[:, 2],
    'c': coefficients[:, 1],
    'd': coefficients[:, 0]
}

df = pd.DataFrame(data)
print(df)
