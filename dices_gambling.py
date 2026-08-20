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
        elif "sup" in pari or "inf" in pari:
            operateur = "sup" if "sup" in pari else "inf"
            pari, pari_type = pari.replace("sup", '').replace("inf", '').strip(), "inf_sup"
            if not pari.isdigit():
                clear_lines(2)
                continue
            elif not (2 <= int(pari) <= 12):
                clear_lines(2)
                continue
            if operateur == 'sup':
                pourc = (sum([proba[x] for x in (filter(lambda x: True if x > int(pari) else False, list(range(2, 13))))]) * 100) / 36
                pari = list(filter(lambda x: True if x > int(pari) else False, list(range(2, 13))))
            elif operateur == 'inf':
                pourc = (sum([proba[x] for x in (filter(lambda x: True if x < int(pari) else False, list(range(2, 13))))]) * 100) / 36
                pari = list(filter(lambda x: True if x < int(pari) else False, list(range(2, 13))))
            
        elif pari in exit:
            sys.exit()
        else:
            clear_lines(2)
            continue
        
        cote = 100 / (pourc + ((5 * pourc) / 100))
        print(f"Probabilités : {pourc:.2f} %\nCote : {cote:.2f}")
        remake = input().lower().strip()
        if remake in exit:
            clear_lines(5)
            continue
        break
    Mise = mise()
    jump()
    clear_lines()

    for i in range(37): # animation
        print(f"\r{' ' * len('Enter a mise:  ')}[ {random.randint(1, 6) + random.randint(1, 6)} ] ", end="", flush=True)
        time.sleep(0.02 + i * 0.008)
    print(f"\r{' ' * len('Enter a mise:  ')}[ {des} ] ", flush=True)
    jump()
    clear_lines()

    if (pari_type == "nombres" and (des in pari)) or (pari_type == "inf_sup" and (des in pari)):
        iswon = True
    if iswon:
        cprint(
            f" You predicted {LOG_DISCRET}[ {formate_collections(sorted(pari))} ]{RESET} and §you Won!!",
            SUCCESS,
        )
        cprint(f" You won {Mise * cote:.2f}€ !", SUCCESS)
    else:
        cprint(f" You predicted {LOG_DISCRET}[ {formate_collections(sorted(pari))} ]{RESET} and §you Lost!!", ERROR)
        cprint(f" You lost {Mise:.2f}€ !", ERROR)
    input('')
    clear()
input("")
