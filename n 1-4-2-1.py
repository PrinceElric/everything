import sys

n = int(input(">>> "))

if not 1 < n < pow(10, 6):
    sys.exit("Please enter a number between 1 and 10^6")

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

    if n == 1:
        print(n)
    else:
        print(n, end=" -> ")
input('')