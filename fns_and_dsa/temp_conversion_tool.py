FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius


def convert_to_fahrenheit(celcius):
    fahrenheit = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit


temp = float(input("Enter the temperature to convert: "))
which_temp = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if which_temp == "C":
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp:.2f}°F.")
elif which_temp == "F":
    f_temp = convert_to_celsius(temp)
    print(f"{temp}°F is equal to {f_temp :.2f}°C.")
else:
    print("Invalid input. Please specify whether temp is Celcius 'C' or fahrenheit 'F'!")
