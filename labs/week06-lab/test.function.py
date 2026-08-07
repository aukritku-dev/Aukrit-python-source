def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * base
    print(f"triangle with height {height} and base {base}")
    print(f"Area = 0.5*{height} x {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

def calculate_circle_area(radius):
    """Calculates and displays rectangle area"""
    area = 3.1416 * radius * radius
    print(f"circle with radius {radius}")
    print(f"Area = 3.1416*{radius}*2= {area:.2f}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(10)