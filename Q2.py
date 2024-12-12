# Write a program to convert a temperature from Celsius to Fahrenheit using the formula:
# Fahrenheit=(Celsius × 9/5)+32

print("**Temperature Conversion (Celsius to Fahrenheit)**")
celsius = input("Enter celsius:")
try:
    celsius = float(celsius)
    fahren = (celsius * (9/5)) +32
    print("Fahrenheit is:" ,fahren)

except:
    print("Invalid input. Please enter a number")

