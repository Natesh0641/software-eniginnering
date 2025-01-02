
def quadratic_solution(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None


try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    result = quadratic_solution(a, b, c)
    print(f"Roots based on user input: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
