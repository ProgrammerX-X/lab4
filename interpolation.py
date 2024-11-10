import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([0, 4, 10, 15, 21, 29, 36, 51])  
y_values = np.array([5, 41, 106, 145, 205, 285, 350, 3510])  

def L(x_values, x, y):
    result = 0 
    n = len(x_values)
    for i in range(n):
        l = 1
        for j in range(n):
            if j != i:
                l *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += l * y[i]
    return result

dx = 10
h = (max(x_values) - min(x_values)) / dx
xi = [min(x_values) + h * i for i in range(dx + 1)]
x_plot = np.linspace(min(x_values), max(x_values), 1000)
y_plot = np.array([L(x_values, x, y_values) for x in x_plot])

plt.plot(x_plot, y_plot, label="Polinom", color='b')
plt.scatter(x_values, y_values, color='r', label="Points")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
