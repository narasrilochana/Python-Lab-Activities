# Write a Python program to print the first n terms of the Fibonacci series
# Using Recursion.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print(f"Fibonacci series (first {n} terms):")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()


n = int(input("Enter the number of terms: "))
print_fibonacci_series(n)