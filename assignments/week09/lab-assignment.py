def calculate_electricity_cost(units):
    if units <= 50:
        total = 2.50 * units + 25
        print(f"1-50 หน่วย: {total:.2f} บาท")

    elif units <= 100:
        total = 2.50 * 50 + 3.00 * (units - 50) + 25
        print(f"1-50 หน่วย: 125.00 บาท")
        print(f"51-100 หน่วย: {total:.2f} บาท")

    elif units <= 200:
        total = 2.50 * 50 + 3.00 * 50 + 3.50 * (units - 100) + 25
        print(f"1-50 หน่วย: 125.00 บาท")
        print(f"51-100 หน่วย: 150.00 บาท")
        print(f"101-200 หน่วย: {total:.2f} บาท")

    else:
        total = 2.50 * 50 + 3.00 * 50 + 3.50 * 100 + 4.00 * (units - 200) + 25
        print(f"1-50 หน่วย: 125.00 บาท")
        print(f"51-100 หน่วย: 150.00 บาท")
        print(f"101-200 หน่วย: 350.00 บาท")
        print(f"201 หน่วยขึ้นไป: {total:.2f} บาท")

    print(f"ค่าบริการ: 25.00 บาท")

    return total

while True:
      
    print("== โปรเเกรมคำนวนค่าไฟฟ้า ==")
    print("1. คำนวนค่าไฟฟ้า")
    print("2. ออกจากโปรเเกรม")
    choices = input("Enter the choice 1 or 2:")

    if choices == "1":
        units = float(input("Enter the number of units : "))
        if units < 0:
            print("Invalid input. ")
            break

        cost = calculate_electricity_cost(units)
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} Baht\n")

    elif choices == "2":
        print("Exiting the program.")
        exit()

    else:
        print("Please enter 1 or 2.")


