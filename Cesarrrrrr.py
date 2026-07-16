import string, random, sys, tools  # noqa: E401

def encrypt():
    global letzte
    alpha = string.ascii_lowercase
    text = input("enter a text to encrypt:  \n")
    n = int(
        input(
            "enter a key of encryption *NOTE! This is using the Ceaser cipher (or enter 0 to make it randomly)\n"
        )
    )

    if str(n) == "0":
        n = random.randint(1, len(alpha) - 1)
    cesar = ""
    
    for i in range(2):
        if text == "":
            for i in range(random.randint(1, 50)):
                text += random.choice(alpha)
        elif 'last' in text:
            text = letzte
    for i in text:
        if i in alpha:
            a = alpha.find(i)
            a = (a + n) % len(alpha)
            cesar += alpha[a]
        elif i.isascii() and i.lower() != i:
            i = i.lower()
            a = alpha.find(i)
            a = (a + n) % len(alpha)
            cesar += alpha[a].upper()
        elif i.isdigit():
            a = (int(i) - n) % 10
            cesar += str(a)
        elif i == " ":
            cesar += " "
        else:
            cesar += i
    letzte = cesar
    print(f"here the text : {text} in Cesar with key of {n} :\n {cesar}")

def decrypt(abc):
    global letzte
    n = int(input("enter a key of decryption \n"))
    alpha = string.ascii_lowercase
    text = ""
    if 'last' in abc:
        abc = letzte
    for i in abc:
        if i in alpha:
            a = alpha.find(i)
            a = (a - n) % len(alpha)
            text += alpha[a]
        elif i.isascii() and i.lower() != i:
            i = i.lower()
            a = alpha.find(i)
            a = (a - n) % len(alpha)
            text += alpha[a].upper()
        elif i.isdigit():
            a = (int(i) + n) % 10
            text += str(a)
        elif i == " ":
            text += " "
        else:
            text += i
    letzte = text
    print(f"the text :  {abc} decrypted in key {n} is : \n {text}")


def not_key_decrypt(txt, sign="elric"):
    global letzte, sequ_of_possibl
    n = 1
    alpha = string.ascii_lowercase
    text = ""
    if 'last' in txt:
        txt = letzte
    for e in range(len(alpha)):
        text = ''
        for i in txt:
            if i in alpha:
                a = alpha.find(i)
                a = (a - n) % len(alpha)
                text += alpha[a]
            elif i.isascii() and i.lower() != i:
                i = i.lower()
                a = alpha.find(i)
                a = (a - n) % len(alpha)
                text += alpha[a].upper()
            elif i.isdigit():
                a = (int(i) + n) % 10
                text += str(a)
            elif i == " ":
                text += " "
            else:
                text += i
        n += 1
        if sign in text:
            sequ_of_possibl.update({n-1: text})
            break
    letzte = text
    for cle, valeur in sequ_of_possibl.items():
        print(f'possible key :  {cle}')
        print(f'text would pass from {txt} to : {valeur}')

is_running = True
letzte =''
sequ_of_possibl = {}
while is_running:
    print("1. encrypt a text")
    print("2. decrypt a text")
    print('3. decrypt without key')
    print('4. Exit')
    choice = input(">>> ")
    match choice:
        case "1":
            encrypt()
        case "2":
            text = input("enter a text to decrypt: \n")
            decrypt(text)
        case '3':
            text = input("enter a text to decrypt: \n")
            kff = input('enter the sign that you know is in this text:  \n')
            while kff == ' ':
                print('not valid sign !! ')
                kff = input('pls, enter the sign that you know is in this text:  \n')
            if kff != '':
                not_key_decrypt(text, kff)
            else:
                not_key_decrypt(text)
        case '4':
            is_running = False
            print(f'{tools.VERT}thank you!{tools.RESET}')
        case _:
            is_running = False
            print('not valid input selected')
            tools.shutdown()
            sys.exit("go to Hell!!")
input("")