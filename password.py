import random, string  # noqa: E401
from tools import *  # noqa: F403

def password():
    char = string.ascii_lowercase
    txt_password = ""
    if Maj:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    if punctuation:
        char += string.punctuation
    txt_password = "".join(random.choices(char, k=n))
    return txt_password


print("*********************")
print("FREE PASSWORD MAKER !")
print("*********************")
print()
n = int(input("enter the lenght of your password:\n"))
Maj = input("do you want MAJ letters in your password ? (y/n):\n").strip().casefold()
digits = input("do you want numbers in your password? (y/n):\n").strip().casefold()
punctuation = (
    input("do you want sign of punctuation in your password? (y/n):\n")
    .strip()
    .casefold()
)

if Maj == "y":
    Maj = True
else:
    Maj = False
if digits == "y":
    digits = True
else:
    digits = False
if punctuation == "y":
    punctuation = True
else:
    punctuation = False

clear()  # noqa: F405
print(f"password made:\v{ROUGE}{password()}")  # noqa: F405
input('')