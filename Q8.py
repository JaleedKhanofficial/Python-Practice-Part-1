# Write a user-defined function calculate(a, b, operator) that performs addition, subtraction, multiplication, or division based on the operator provided.

print("**Simple Calculator**")
def calculator(a,b, operator):
    if operator == '+':
        sum = a+b
        print("The sum of the two number is :",sum)
    elif operator == '-':
        diff = num1 - num2
        print("The Subtraction of numbers (second from first) :",diff)
    
    elif operator == '*':
        product = num1 * num2
        print("The product of the two number is :",product)
    
    elif operator == '/':
        quot = num1/num2
        print("The quotient is :",quot)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = str(input("Enter Operator: "))
calculator(num1, num2, op)