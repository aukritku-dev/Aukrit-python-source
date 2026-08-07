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
    pass

# เขียน function ชื่อ calculate_sphere(radius):
# คำนวณหา ปริมาตร ของทรงกลม volumn = 4.0 / 3 * pi * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ
import math

def calculate_sphere(radius):
    volume = 4.0 / 3 * math.pi * radius ** 3
    print(f"sphere with radius {radius}")
    print(f"Volume = 4/3 * pi * {radius}**3 = {volume:.2f}")
    print()

print("Calculating sphere volumes:")
calculate_sphere(5)
calculate_sphere(10)