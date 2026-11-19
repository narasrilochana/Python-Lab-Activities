#Write a Python program to check whether a given positive integer is a
#Prime Number or Not a Prime Number.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
