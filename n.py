import sys

n = int(input(">>>  "))
if not 1 < n < pow(10, 6):
    sys.exit("Please enter a number between 1 and 10")
while not n == 1:
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
    if n == 1:
        print(n)
    else:
        print(n, end=" -> ")
input('')