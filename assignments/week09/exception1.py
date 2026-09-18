'''โจทย์ เครื่องคำนวณอย่างปลอดภัย
เขียนโปรเเกรมรับเลข 2 จำนวนเเละตัวดำเนินการ 1 ตัว ได้เเก่ + - * / เเล้วเเสดงผลลัพธ์โปรเเกรมต้องจัดการกรฯีต่อไปนี้
- ผู้ใช้กรอกรข้อมูลที่ไม่ใช่ตัวเลข #ValueError
- ผู้ใช้เลือกกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
- ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
- โปรเเกรมต้องเเสดง จบการทำงาน เสมอด้วย finally

ตัวอย่างผลลัพธ์ที่คาดหวัง

ตัวเลขที่ 1: 10
ตัวเลขที่ 2: 0
เครื่องหมาย (+ - * /): /

ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน
'''

try:
    num1 = float(input("ตัวเลขที่ 1: "))
    
    num2 = float(input("ตัวเลขที่ 2: "))
    
    operator = input("เครื่องหมาย (+ - * /): ")
    
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("ตัวดำเนินการไม่ถูกต้อง")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
        result = num1 / num2
    
    print(f"\nผลลัพธ์: {num1} {operator} {num2} = {result}")

except ValueError as error:
    print(f"\nข้อผิดพลาด: ตัวเลขไม่ถูกต้อง")
except ZeroDivisionError as error:
    print(f"\n{error}")

finally:
    print("จบการทำงาน")