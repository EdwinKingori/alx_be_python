# User inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = (input("Choose the operation (+, -, *, /): "))

# perform operations
match operation:
    case "+":
        result = num1 + num2
        print(f"the result is", result, ".")
    case "-":
        result = num1 - num2
        print(f"the result is", result, ".")
    case "*":
        result = num1 * num2
        print(f"the ruesult is", result, ".")
    case "/":
        if num2 == 0:
            print(f"cannot devide by zero")
        else:
            result = num1 / num2
            print(f"The result is [result].")
    case _:
        print(f"invalid operation entered.")
