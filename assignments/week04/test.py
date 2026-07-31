#รับคาชื่อจริงจากผู้ใช้
#เขียน loop เพื่อนับจำนวนสระในภาษาอังกฤษในชื่อที่รับมานั้นว่ามีกี่ตัว

#ตัวอย่างหน้าจอ

#what is you name? : Boonchoo

#Your name have 4 vowels.
name = input("what is you name? : ")

vowels = "aeiou"
count = 0

for x in name.lower():     
    if x in vowels:
        count += 1

print(f"Your name have {count} vowels.")