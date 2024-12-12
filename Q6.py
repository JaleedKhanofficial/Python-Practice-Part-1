# Write a program that takes a percentage as input and prints the grade based on the following conditions:
# 90% and above: A
# 80% to 89%: B
# 70% to 79%: C
# Below 70%: F

print("**Grade Calculator**")
per = float(input("Enter grade of the student: "))
if per >= 90 and per <= 100:
    print(" Grade A")
elif per >= 80 and per < 89 :
    print(" Grade B")
elif per >= 70 and per < 79:
    print("Grade C")
elif per < 69 and per >= 0:
    print(" Grade F")
else:
    print("Invalid Input!")
