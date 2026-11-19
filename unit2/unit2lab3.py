#Write a Python program to print the first n terms of the Fibonacci series.
n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a, end=" ")
    print(b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
    print()  # Print newline at the end
