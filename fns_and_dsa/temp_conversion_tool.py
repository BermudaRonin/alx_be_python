FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Prompt the user for the value of temperature
temp = float(input("Enter the temperature to convert: "))

# Prompt the user for the unit of conversion
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# Results
if unit == "C":
    print(f"{temp}°C is {str(convert_to_fahrenheit(temp))}°F")
elif unit == "F":
    print(f"{temp}°F is {str(convert_to_celsius(temp))}°C")
else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")