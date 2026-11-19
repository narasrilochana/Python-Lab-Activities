#Write a Python program to print the first n terms of the Fibonacci series
#Using Recursion.
def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n):
    """Print the first n terms of the Fibonacci series."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    print(f"Fibonacci series (first {n} terms):")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()