# userinput
number = int(input("Enter a number to see its multiplication table:"))
for i in range(1, 10+1):
    result = i * number
    print(f"{i} * {number} = {result}")
