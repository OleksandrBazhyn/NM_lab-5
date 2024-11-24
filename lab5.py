import numpy as np

# Вхідні дані
x = np.linspace(0, np.pi, 15)  # 15 рівномірно розподілених точок на [0, π]
y = np.sin(x)

n = len(x)

# Обчислення проміжних значень
h = np.diff(x)  # Різниці між x
alpha = np.zeros(n)
for i in range(1, n-1):
    alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])

# Формування матриці для СЛАР
A = np.zeros((n, n))
b = np.zeros(n)

# Граничні умови для природного сплайна: c''(x_0) = c''(x_n) = 0
A[0, 0] = 1
A[n-1, n-1] = 1
b[0] = 0
b[n-1] = 0

for i in range(1, n-1):
    A[i, i-1] = h[i-1]
    A[i, i] = 2 * (h[i-1] + h[i])
    A[i, i+1] = h[i]

b[1:n-1] = alpha[1:n-1]

# Розв'язування СЛАР для c
c = np.linalg.solve(A, b)

# Виведення коефіцієнтів сплайна
print("Коефіцієнти сплайна (для кожного сегмента):\n", c)
