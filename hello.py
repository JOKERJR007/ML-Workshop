def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is: {result}")

