import time
import sys

name = ""
just_namee = ""
b = 0
a = 0


def azer():
    global name
    global just_namee
    global b
    global a
    a = 0
    b = 0
    name = str(input("Enter your name: "))
    just_namee = name
    if "Elric" in name or "elric" in name:
        print("Admin is there")
        b = 1
    if b == 1:
        pass
    elif name:
        tyuiop()
    else:
        while name == "" or name == " ":
            name = str(input("Enter your name: "))
            a += 1
        tyuiop()
        just_namee = name
        if "Elric" in name or "elric" in name:
            print("Admin is there")
            b = 1
    if a >= 10:
        print(f"{a}, c'est bien trop, tu vas me recommencer tout ça")
        azer()
    elif b == 1:
        print(f"Welcome to the game {name} sama the Master of the world")
    elif a >= 2:
        print(f"il t'en aura fallu du temps ({a})")
        print(f"Welcome to the game {name}")
    elif a == 1:
        print("enfin arrivé")
        print(f"que {a} essai, ça va")
        print(f"Welcome to the game {name}")
    else:
        print(f"Welcome to the game {name}")


def tyuiop():
    global name
    username = name
    if len(username) >= 12:
        print("username too long")
        sys.exit()
    elif " " in username:
        print("username must not have spaces")
        sys.exit()
    elif not username.isalpha():
        print("username must be alphabetical")
        sys.exit()
    else:
        print("username ok")


def fonction_password():
    global password, size
    password = ""
    size = ""
    verif = ""
    password = str(input("Enter your password: "))
    while password == "" or password == " ":
        password = str(input("Enter your password: "))
    size = len(password)
    if not 5 < size < 15:
        print("password has a not valid length")
        sys.exit()
    if " " in password:
        print("password must not have spaces")
    else:
        verif = input(f"pls {just_namee}, enter a second time your password: ")
        while verif != password:
            print(f"{just_namee}, the password are not the same")
            verif = input(f"{just_namee}, reenter your password ('abc' to remake it): ")
            if verif == "abc":
                fonction_password()
                break
            while verif == "" or verif == " ":
                verif = input(f"pls {just_namee}, reenter your password to be sure: ")
            if verif == password:
                print("password ok")
                break
            else:
                pass


azer()
time.sleep(1)
start_password = ""
password = ""
size = 0
print(f"{just_namee}, you have to define a password")
if b == 1:
    just_namee = "Elric"
    print(f"for the user {just_namee}sama, the password is already defined:")
    password = "Elric33160"
    size = len(password)
else:
    fonction_password()
hide_password = password[-3:]
for i in range(size - 3):
    start_password += "*"
print()
print(f" your username is {just_namee.capitalize()}")
print(f" your password is {start_password + hide_password}")
input('')
