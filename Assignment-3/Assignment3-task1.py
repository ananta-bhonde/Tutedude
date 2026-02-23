def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number =int(input("Enter a number: ")) # enter number 5
output = factorial(number)
print(f"Factorial of {number} is {output}")
