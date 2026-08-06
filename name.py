import time, sys
from tools import *

name, just_namee, a, b = "", "", 0, 0


def name():
    global name, just_namee, a, b
    a, b, name = 0, 0, input("Enter your name: ")
    just_namee = name
    if "Elric" in name or "elric" in name:
        print("Admin is there")
        b = 1
    elif name:
        check_username()
    else:
        while name == "" or name == " ":
            name = input("Enter your name: ")
            a += 1
        check_username()
        just_namee = name
        if "Elric" in name or "elric" in name:
            print("Admin is there")
            b = 1
    if a >= 10:
        print(f"{a}, c'est bien trop, tu vas me recommencer tout ça")
        name()
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


def check_username():
    global name
    username = name
    if len(username) >= 12:
        cprint("username too long", ERROR)
        name()
    elif " " in username:
        cprint("username must not have spaces", ERROR)
        name()
    elif not username.isalpha():
        cprint("username must be alphabetical", ERROR)
        name()
    else:
        cprint("username ok", VERT_FLASH)


def fonction_password():
    global password
    password, verif = "", ""
    password = str(input("Enter your password: "))
    while password == "" or password == " ":
        password = str(input("Enter your password: "))
    if not 5 < len(password) < 15:
        print("password has a not valid length")
        fonction_password()
    if " " in password:
        print("password must not have spaces")
    else:
        verif = input(f"{just_namee}, enter a second time your password: ")
        while verif != password:
            print(f"{just_namee}, the password are not the same")
            verif = input(f"{just_namee}, reenter your password ('abc' to remake it): ")
            if verif == "abc":
                fonction_password()
            while verif == "" or verif == " ":
                verif = input(f"pls {just_namee}, reenter your password to be sure: ")
            if verif == password:
                print("password ok")
                break


name()
time.sleep(0.7)
start_password, password, size = "", "", 0
print(f"{just_namee}, you have to define a password")
if b == 1:
    just_namee = "Elric"
    print(f"for the user {just_namee}sama, the password is already defined:")
    password = "Elric33160"
else:
    fonction_password()
hide_password = password[-3:]
for i in range(len(password) - 3):
    start_password += "*"
print()
print(f" your username is {just_namee.capitalize()}")
print(f" your password is {start_password + hide_password}")
input()
