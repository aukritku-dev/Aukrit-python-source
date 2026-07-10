print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()


#input
r = float(input("Radius: "))

#process
area = 3.14159 * r ** 2

#output
print(f"Area = {area}")

print("2.Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")

#input
s = int(input("seconds: "))

#process
hour = s // 3600 
sec_remain = s % 3600 

minute = s // 60
sec_remain = s % 60

#output
print(s, "seconds = ",hour,"hour,",minute,"minute,",sec_remain,"second")
print(f"{s} seconds = {hour} hour, {minute} minute,{sec_remain} second")