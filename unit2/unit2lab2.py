#Write a Python program to find the factorial of a positive integer using loop.
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial = 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial =", fact)