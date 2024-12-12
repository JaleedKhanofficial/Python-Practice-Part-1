# Write a program that asks the user for a number and prints whether it is even or odd.


print("**Even Or Odd**")
num = input("Enter number: ")
try:
    num = float(num)
    if num%2 ==0 :
        print("The number you enter is Even.")
    else:
        print("The number you enter is Odd.")
except:
    print("Invalide input. Please enter a number.")