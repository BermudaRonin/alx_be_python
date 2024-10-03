def safe_divide(numerator, denominator):
    try:
        results = float(numerator) / float(denominator)
        print(f"The result of the division is {results}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
