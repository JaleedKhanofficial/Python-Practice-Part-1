#Write a function square(number) that takes a number as input and returns its square. Use this function to print the square of 5 numbers given by the user.


def square(number):
    return pow(number, 2)  

count = 5
while count > 0:
    try:
        number = float(input("Enter number: "))  
        sq = square(number)
        print(f"The square of {number} is {sq}")
        count -= 1  
    except ValueError:
        print("Invalid input. Please enter a valid number.")
