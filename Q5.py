# Write a program that takes three numbers as input and prints the largest of the three.


print("**Find the Largest Number**")
largest = -1
count = 3
while count > 0:
    num = input("Enter number: ")
    try:
        fnum = float(num)
        if fnum > largest:
            largest = fnum
            count = count -1
            
    except:
        print("Invalid input. Please enter a number.")
print(largest)