def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter a positive number.")
