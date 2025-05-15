def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

sample_number = 6
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")
