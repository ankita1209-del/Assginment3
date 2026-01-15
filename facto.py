def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))

# Function call and output
print("Factorial of", num, "is:", factorial(num))
