def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/denominator
        return f" The result of the division is: {result} "
    except ZeroDivisionError:
        if denominator <= 0:
            print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
