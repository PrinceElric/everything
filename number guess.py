import random


def numberr():
    global number
    while not number.isdigit():
        number = input(f"Please enter a number between {mini} and {maxi}: ")
    while not mini < int(number) < maxi:
        number = input(f"Please enter a number between {mini} and {maxi}: ")
    number = int(number)


def high_low():
    global number_rand, number, guesses
    if int(number) > number_rand:
        print(f"{number} is too high! Try again!")
        guesses += 1
        number = input(f"Please enter a number between {mini} and {maxi}: ")
        numberr()
    else:
        print(f"{number} is too low! Try again!")
        guesses += 1
        number = input(f"Please enter a number between {mini} and {maxi}: ")
        numberr()


mini = 1
maxi = 100
cheat = False
print("Welcome to the Number Guessing Game!")
number_rand = random.randint(mini, maxi)
number_rand = int(number_rand)
number = input(f"Please enter a number between {mini} and {maxi}: ")
guesses = 1
if " " in number:
    cheat = True
else:
    numberr()
if cheat:
    for i in range(2):
        choi = (1, 2)
        a = random.choice(choi)
        if a == 1:
            print(f"{number} is too LOW! Try again!")
            number = input(f"Please enter a number between {mini} and {maxi}: ")

        else:
            print(f"{number} is too HIGH! Try again!")
            number = input(f"Please enter a number between {mini} and {maxi}: ")
        guesses += 1
else:
    while number != number_rand:
        high_low()

print("Congratulations! You guessed the number!")
print(f"You guessed {guesses} times!")
input("")
