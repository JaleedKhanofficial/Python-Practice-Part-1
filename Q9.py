# Write a function is_divisible(num, divisor) that checks if a number is divisible by another. It should return True if divisible and False otherwise.

def is_divisible(num, divisor):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")  # Handle division by zero
    return num % divisor == 0


print(is_divisible(10, 2))  
print(is_divisible(10, 3))  
print(is_divisible(15, 5)) 