num = int(input("Enter a number: "))
decimal = 2.5
name = "Anosh"
print("Name:", name)
print("Number:", num)
print("Decimal:", decimal)
print(type(num))
print(type(decimal))
print(type(name))
# Assignment operators
count = 1
count += 2
print("Count:", count)
# Conditional statements
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
# For loop
for i in range(1, 8):
    print(i)
# Continue and break
for number in range(1, 8):
    if number == 3:
        continue
    if number == 6:
        break
    print("Number:", number)
# While loop
counter = 1
while counter <= 5:
    print("Counter:", counter)
    counter += 1
