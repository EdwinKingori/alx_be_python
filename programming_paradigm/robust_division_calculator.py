def safe_divide(numerator, denominator):
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))

        result = numerator/denominator
        return f" The result of the division is: {result} "
    except ZeroDivisionError:
        if denominator <= 0:
            print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")


print(safe_divide(10, 5))
