import string, random  # noqa: E401
from tools import * # noqa: F403

letzte, sequ_of_possibl, alpha = '', {}, string.ascii_lowercase

def math(txt, n, decrypt=True):
    global alpha
    text = ''
    for i in txt:
        if i in alpha:
            a = alpha.find(i)
            if decrypt:
                a = (a - n) % len(alpha)
            else:
                a = (a + n) % len(alpha)
            text += alpha[a]
        elif i.isascii() and i.lower() != i:
            i_lower = i.lower()
            a = alpha.find(i_lower)
            if decrypt:
                a = (a - n) % len(alpha)
            else:
                a = (a + n) % len(alpha)
            text += alpha[a].upper()
        elif i.isdigit():
            if decrypt:
                a = (int(i) - n) % 10
            else:
                a = (int(i) + n) % 10
            text += str(a)
        elif i == " ":
            text += " "
        else:
            text += i
    return text

def encrypt():
    global letzte, alpha
    txt = input("enter a text to encrypt:  \n")
    n = int(input("enter a key of encryption *NOTE! This is using the Ceaser cipher (or 0 to make it random)\n"))
    if n == 0:
        n = random.randint(1, len(alpha) - 1)
    if txt == "":
        txt = ''.join(random.choices(alpha, k=50))
    elif 'last' in txt:
        txt = letzte
    apr = math(txt, n, decrypt=False)
    letzte = apr
    print(f"here the text : {txt} in Cesar with key of {n}:\n {apr}")

def decrypt(txt):
    global letzte
    n = int(input("enter a key of decryption \n"))
    if 'last' in txt:
        txt = letzte
    apr = math(txt, n, decrypt=True)
    letzte = apr
    print(f"the text :  {txt} decrypted in key {n} is : \n {apr}")

def decrypt_without_key(txt, sign="elric"):
    global letzte, sequ_of_possibl
    if 'last' in txt:
        txt = letzte
    for n in range(1, len(alpha) + 1):
        apr = math(txt, n, decrypt=True)
        if sign in apr:
            sequ_of_possibl[n] = apr
            letzte = apr
            break
    for cle, valeur in sequ_of_possibl.items():
        print(f'possible key :  {cle}')
        print(f'text would pass from {txt} to : {valeur}')

while True:
    choice = menu_options(["1. encrypt a text", "2. decrypt a text", '3. decrypt without key', '4. Exit'])  # noqa: F405
    match choice:
        case "1. encrypt a text":
            encrypt()
        case "2. decrypt a text":
            text = input("enter a text to decrypt: \n")
            decrypt(text)
        case '3. decrypt without key':
            text = input("enter a text to decrypt: \n")
            kff = input('enter the sign that you know is in this text:  \n')
            while kff == ' ':
                print('not valid sign !!')
                kff = input('pls, enter the sign that you know is in this text:  \n')
            if kff != '':
                decrypt_without_key(text, kff)
            else:
                decrypt_without_key(text)
        case '4. Exit':
            cprint('thank you!', SURLIGN2_VERT)  # noqa: F405
            break
    input(">>>   ")
input("")
