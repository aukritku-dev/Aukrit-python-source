weight = float(input("กรอกน้ำหนัก (กิโลกรัม): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

print(f"BMI ของคุณคือ: {bmi:.1f}")

if bmi < 18.5:
    print("หมวดหมู่: Underweight (น้ำหนักน้อยกว่าเกณฑ์)")
elif bmi < 25.0:
    print("หมวดหมู่: Normal weight (น้ำหนักปกติ)")
elif bmi < 30.0:
    print("หมวดหมู่: Overweight (น้ำหนักเกิน)")
else:
    print("หมวดหมู่: Obese (อ้วน)")