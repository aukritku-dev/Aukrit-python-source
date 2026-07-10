print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

w = float(input("weight: "))
h = float(input("height: "))

bmi = w / (h ** 2)

print(f"BMI = {bmi}")
