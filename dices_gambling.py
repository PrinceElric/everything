from tools import *
from games import mise
import random, time, sys

# add animation to the cube
proba = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
while config["sold"] > 10:
    des = random.randint(1, 6) + random.randint(1, 6)
    print(des)
    while True:
        leave, iswon = False, False
        pari = input("Entre ton pari :\n> ").lower().strip()
        if pari.replace(" ", "").isdigit():
            pari_type = "nombres"
            pari = pari.split()
            pari = [int(x) for x in pari]
            for i in pari:
                if not 2 <= i <= 12:
                    leave = True
            if leave:
                clear_lines(2)
                continue
            pourc = (sum([proba[x] for x in pari]) * 100) / 36
            cote = 100 / (pourc + ((5 * pourc) / 100))
            print(f"Probabilités : {pourc:.2f} %\nCote : {cote:.2f}")
        elif pari in exit:
            sys.exit()
        else:
            clear_lines(2)
            continue
        remake = input().lower().strip()
        if remake in exit:
            clear_lines(5)
            continue
        break
    mise = mise()

    if pari_type == "nombres" and (des in pari):
        iswon = True
    if iswon:
        cprint(
            f"You predicted {LOG_DISCRET}[ {formate_collections(sorted(pari))} ]{RESET} and §you Won!!",
            SUCCESS,
        )
        cprint(f"You won {mise * cote:.2f}€ !", SUCCESS)
    else:
        cprint(f"You predicted {LOG_DISCRET}{pari}{RESET} and §you Lost!!", ERROR)
        cprint(f"You lost {mise:.2f}€ !", ERROR)
    input('')
    clear()
input("")
