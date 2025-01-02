import math
import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(a, b, c):
   
    discriminant = b**2 - 4 * a * c
    roots = []

   
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        roots = [root1, root2]
        print(f"Two real roots: x = {root1:.2f}, x = {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        roots = [root]
        print(f"One real root: x = {root:.2f}")
    else:
        print("No real roots exist.")

    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    print(f"Vertex: ({vertex_x:.2f}, {vertex_y:.2f})")

    
    x = np.linspace(vertex_x - 10, vertex_x + 10, 500)
    y = a * x**2 + b * x + c

   
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')

    if roots:
        for root in roots:
            plt.scatter(root, 0, color='red', label=f'Root: ({root:.2f}, 0)')
   
    plt.scatter(vertex_x, vertex_y, color='green', label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')
    plt.text(vertex_x, vertex_y + 1, f'({vertex_x:.2f}, {vertex_y:.2f})', color='green', fontsize=10)

   
    y_intercept = c
    plt.scatter(0, y_intercept, color='purple', label=f'Y-intercept: (0, {y_intercept:.2f})')
    plt.text(0.5, y_intercept, f'(0, {y_intercept:.2f})', color='purple', fontsize=10)

   
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

  
    plt.title(f"Graph of {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


a = 2
b = -8
c = 6


plot_quadratic(a, b, c)
