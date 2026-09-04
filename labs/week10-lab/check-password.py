#รับค่า password จากผู้ใช้

#password นั้นเเข็งเเรงหรือไม่

#passwordนั้นเเข็งเเรง ถ้าประกอบไปด้วยตัวเลข ตัวอักษร เเละ @ 1ตัว ยาวมากกว่า8ตัว
#ตัวอย่างหน้าจอ
#please input your passworrd:Boonchoo
#your password is not strong!
#please input your password:Boonchoo@123
#your password is strong!
password = input("please input your password:")

digit = False
alpha = False

for ch in password:
    if ch.isdigit():
        digit = True
    if ch.isalpha():
        alpha = True

count_at = password.count('@')

if digit and alpha and count_at == 1 and len(password) > 8:
    print("your password is strong!")
else:
    print("your password is not strong!")



