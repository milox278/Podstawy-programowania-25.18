###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
celcius = float(input("Enter temperature in degrees Celsius: "))
fahrenheit = (9/5) * celcius + 32
kelvin = celcius + 273.15
print(f"Temperature in Celsius: {celcius}")
print(f"Temperature in Fahrenheit: {fahrenheit}")
print(f"Temperature in Kelvin: {kelvin}")
