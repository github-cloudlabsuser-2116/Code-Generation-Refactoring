def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

choice = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {choice} is {factorial(choice)}")