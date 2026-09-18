#try-exception ==> ความพยายามในการจัดการข้อผิดพลาดของโปรเเกรม
#ERROR (BUGS)
# 3 type, syntax error, runtime error,logical error

#valueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณจะอายุ: {age+1} ปี")
except ValueError:
    print("กรุณากรอกตัวเลขจำนวนเต็มเท่านั้น")

#ZeroDivisionException
try:
    numerator = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))

    result = numerator / denominator
    print(f"ผลลัพธ์: {result}")

except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

#FileNotFoundException , PermissionException
try:
    filename = input("กรอกชื่อไฟล์: ")

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

        print("เนื้อหาในไฟล์:")
        print(content)

except FileNotFoundError:
    print(f"ไม่พบชื่อไฟล์ {filename}")

except PermissionError:
    print("คุณไม่มีสิทธิ์ในการเข้าถึงไฟล์")




