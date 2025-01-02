import math


with open("/content/input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    try:
        a, b, c = map(float, line.split())
        discriminant = b**2 - 4*a*c
        
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots for coefficients {a}, {b}, {c}: {root1}, {root2}")
        else:
            print(f"No real roots for coefficients {a}, {b}, {c}.")
    except ValueError:
        print(f"Invalid input: {line.strip()}")
