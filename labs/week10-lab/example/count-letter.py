#เขียนโปรเเกรม
#รับค่าข้อความจากผู้ใช้ เป็นแปร str ชื่อ text
#รับค่าอักขระที่ต้องการนับในขข้อความ text
#ดำเนินการนัลอักขระตามที่ผู้ใช้ต้องการ เเละเเสดงออกทางหน้าจอ

text = input("Enter your text: ")
letter_to_count = input("Enter a letter to count: ")
count = 0
for letter in text:
    if letter == letter_to_count:
        count += 1
print(f"{count} letters '{letter_to_count}' found in '{text}'")
