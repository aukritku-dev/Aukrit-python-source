EXCHANGE_RATE = 35.5  

print("เลือกรูปเเบบการแปลงเงิน:")
print("1. THB -> USD")
print("2. USD -> THB")

choice = input("เลือก (1 หรือ 2): ")

amount = float(input("กรอกจำนวนเงินที่ต้องการแปลง: "))

if choice == "1":
    result = amount / EXCHANGE_RATE
    print(f"สูตรที่ใช้: {amount:.2f} THB / {EXCHANGE_RATE} = {result:.2f} USD")
    print(f"ผลลัพธ์: {amount:.2f} THB = {result:.2f} USD")
elif choice == "2":
    result = amount * EXCHANGE_RATE
    print(f"สูตรที่ใช้: {amount:.2f} USD x {EXCHANGE_RATE} = {result:.2f} THB")
    print(f"ผลลัพธ์: {amount:.2f} USD = {result:.2f} THB")
else:
    print("เลือก 1 หรือ 2 เท่านั้น")