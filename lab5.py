import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

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
plt.plot(x_dense, np.cos(x_dense), label="Перша похідна sin(x): cos(x)", color="green")
plt.plot(x_dense, dy_dense, label="Перша похідна кубічного сплайну", color="purple", linestyle="--")
plt.title("Перша похідна")
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.legend()
plt.grid()

# Графік другої похідної
plt.subplot(3, 1, 3)
plt.plot(x_dense, -np.sin(x_dense), label="Друга похідна sin(x): -sin(x)", color="brown")
plt.plot(x_dense, d2y_dense, label="Друга похідна кубічного сплайну", color="magenta", linestyle="--")
plt.title("Друга похідна")
plt.xlabel("x")
plt.ylabel("d²y/dx²")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Виведення коефіцієнтів сплайна
coefficients = spline.c  # Коефіцієнти поліномів для кожного сегмента
print("Коефіцієнти сплайна (для кожного сегмента):\n", coefficients)
