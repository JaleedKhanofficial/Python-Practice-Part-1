# # Calculate the Area of a Circle
# Write a program that takes the radius of a circle as input and calculates its area using the formula:
# Area=π×radius 
# (Use 3.14 for 𝜋).

print("Calculate the Area of a Circle")
pi = 3.14
rad = input("Entre radius: ")
try:
    radius = float(rad)
    area = pi * radius
    cArea = round(area)
    print("Area of thr Circle is :",cArea)
except:
    print("Invalid input. Please enter a number")
