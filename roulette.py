from tools import *
import random, time, sys


def roulette_game():
    ROULETTE_EUROPEENNE = [
        0,
        32,
        15,
        19,
        4,
        21,
        2,
        25,
        17,
        34,
        6,
        27,
        13,
        36,
        11,
        30,
        8,
        23,
        10,
        5,
        24,
        16,
        33,
        1,
        20,
        14,
        31,
        9,
        22,
        18,
        29,
        7,
        28,
        12,
        35,
        3,
        26,
    ]
    COULEURS_ROULETTE = {
        0: "VERT",
        1: "ROUGE",
        2: "NOIR",
        3: "ROUGE",
        4: "NOIR",
        5: "ROUGE",
        6: "NOIR",
        7: "ROUGE",
        8: "NOIR",
        9: "ROUGE",
        10: "NOIR",
        11: "NOIR",
        12: "ROUGE",
        13: "NOIR",
        14: "ROUGE",
        15: "NOIR",
        16: "ROUGE",
        17: "NOIR",
        18: "ROUGE",
        19: "ROUGE",
        20: "NOIR",
        21: "ROUGE",
        22: "NOIR",
        23: "ROUGE",
        24: "NOIR",
        25: "ROUGE",
        26: "NOIR",
        27: "ROUGE",
        28: "NOIR",
        29: "NOIR",
        30: "ROUGE",
        31: "NOIR",
        32: "ROUGE",
        33: "NOIR",
        34: "ROUGE",
        35: "NOIR",
        36: "ROUGE",
    }
    numero = random.choice(ROULETTE_EUROPEENNE)
    couleur = COULEURS_ROULETTE[numero]
    compte, mise, prediction, pari_type, iswon, montant_gain = (
        0,
        "",
        "",
        None,
        False,
        0,
    )

    def roulette_animation(resultat):
        nonlocal ROULETTE_EUROPEENNE, COULEURS_ROULETTE, couleur, compte
        compte = 0
        for num in ROULETTE_EUROPEENNE:
            compte += 1
            if num == 0:
                continue
            print(f"[ {match_color(COULEURS_ROULETTE[num])}{num}{RESET} ]", end=" ")
            if compte == 13 or compte == 25:
                print("\n")
        print(f"\n{' ' * 40}↓")
        for i in range(30):
            numero = random.choice(ROULETTE_EUROPEENNE)

            couleur = COULEURS_ROULETTE[numero]

            if couleur == "ROUGE":
                affichage = f"{ROUGE_FLASH}{numero}{RESET}"
            elif couleur == "NOIR":
                affichage = f"{NOIR}{numero}{RESET}"
            else:
                affichage = f"{VERT_FLASH}{numero}{RESET}"

            print(f"\r{' ' * 38}[ {affichage:^5} ] ", end="", flush=True)

            time.sleep(0.02 + i * 0.008)

        print(
            f"\r{' ' * 38}[ {ROUGE_FLASH if COULEURS_ROULETTE[resultat] == 'ROUGE' else NOIR if COULEURS_ROULETTE[resultat] == 'NOIR' else VERT}{resultat}{RESET} ] ",
            flush=True,
        )

    def affichage():
        nonlocal mise, prediction, pari_type, numero, iswon, montant_gain
        iswon = False
        clear()
        print(f"+{'-' * 80}+\n")
        print(f"{' ' * 33}ROULETTE GAME\n")
        roulette_animation(numero)
        print("\n")
        match pari_type:
            case "num_simple":
                if numero == prediction:
                    config["sold"] += mise * 35
                    iswon, montant_gain = True, mise * 35
                else:
                    config["sold"] -= mise
                prediction = f"{ROUGE if COULEURS_ROULETTE[prediction] == 'ROUGE' else NOIR }{prediction}{RESET}"
            case "num_split_n2":
                if numero in prediction:
                    config["sold"] += mise * 17
                    iswon, montant_gain = True, mise * 17
                else:
                    config["sold"] -= mise
                prediction = f"{LOG_DISCRET}{formate_collections(prediction)}{RESET}"
            case "num_street":
                if numero in prediction:
                    config["sold"] += mise * 11
                    iswon, montant_gain = True, mise * 11
                else:
                    config["sold"] -= mise
                prediction = f"{LOG_DISCRET}{formate_collections(prediction)}{RESET}"

        if iswon:
            cprint(f"You predicted [ {prediction} ] and §you Won!!", SUCCESS)
            cprint(f"You won €{montant_gain} !", VERT_FLASH)
        else:
            cprint(f"You predicted [ {prediction} ]  §(wrong...)!", ERROR)
            cprint(f"You lost €{mise} !", ROUGE_FLASH)
        input()

    def num_simple():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "num_simple"
            faire_titre_section("Numéro simple", color="FOND_ROUGE")
            prediction = input("\nEnter your prediction (1-36):   ").strip().lower()
            if prediction == "right":
                prediction = numero
                clear_lines()
                print(f"enter your prediction (n):  {prediction}")
            elif not prediction.isdigit():
                cprint("incorrect", ERROR)
                time.sleep(0.3)
                clear_lines(2)
                continue
            elif not 1 <= int(prediction) <= 36:
                cprint("incorrect", ERROR)
                time.sleep(0.3)
                clear_lines(2)
                continue
            prediction = int(prediction)
            break

    def num_split_n2():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type, leave = (
                random.choice(ROULETTE_EUROPEENNE),
                "num_split_n2",
                False,
            )
            faire_titre_section("Numéros doubles", color="FOND_ROUGE", largeur=80)
            compte = 0
            print("\n")
            for num in ROULETTE_EUROPEENNE:
                compte += 1
                if num == 0:
                    continue
                print(f"[ {match_color(COULEURS_ROULETTE[num])}{num}{RESET} ]", end=" ")
                if compte == 13 or compte == 25:
                    print("\n")

            prediction = (
                input(
                    f"\n\nEnter your predictions (1-36) {SOULIGN2}(n1 n2 (ajd)){RESET}:   "
                )
                .strip()
                .lower()
            )
            if prediction == "right":
                prediction = []
                prediction.append(numero)
                prediction.append(
                    int(
                        ROULETTE_EUROPEENNE[
                            (ROULETTE_EUROPEENNE.index(int(numero)) + 1)
                        ]
                    )
                )
            else:
                prediction = prediction.split()
                for i in prediction:
                    if leave:
                        break
                    elif len(prediction) != 2:
                        leave = True
                    elif not i.isdigit():
                        leave = True
                    elif 0 >= int(i) or int(i) > 36:
                        leave = True
                if leave:
                    continue
                if ROULETTE_EUROPEENNE[
                    (ROULETTE_EUROPEENNE.index(int(prediction[0])) + 1)
                ] != int(prediction[1]):
                    continue
            prediction = [int(x) for x in prediction]
            clear_lines()
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def num_street():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type, leave = (
                random.choice(ROULETTE_EUROPEENNE),
                "num_street",
                False,
            )
            faire_titre_section("Numéros doubles", color="FOND_ROUGE", largeur=80)

            prediction = (
                input(
                    f"\n\nEnter your predictions (1-36) {SOULIGN2}(n1 +1 +2 (conséc)){RESET}:   "
                )
                .strip()
                .lower()
            )
            if prediction == "right":
                prediction = []
                prediction.append(numero, numero + 1, numero + 2)
            else:
                prediction = prediction.split()
                for i in prediction:
                    if leave:
                        break
                    elif len(prediction) != 3:
                        leave = True
                    elif not i.isdigit():
                        leave = True
                    elif 0 >= int(i) or int(i) > 36:
                        leave = True
                if leave:
                    continue
                if (
                    int(prediction[0]) != int(prediction[1]) - 1
                    and int(prediction[0]) != int(prediction[2]) - 2
                ):
                    continue
            prediction = [int(x) for x in prediction]
            clear_lines()
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    roulette_animation(numero)
    input()
    while config["sold"] >= 10:
        pari_options = menu_options(
            [
                "1. Numéro simple    (35:1)",
                "2. Cheval / Split   (17:1)",
                "3. Street           (11:1)",
                "4. Carré / Corner   (8:1)",
                "5. Sixain           (5:1)",
                "6. Douzaine         (2:1)",
                "7. Colonne          (2:1)",
                "8. Rouge / Noir     (1:1)",
                "9. Pair / Impair    (1:1)",
                "10. Manque / Passe  (1:1)",
                "11. Exit",
            ],
            "Options de pari",
        )
        clear()
        match pari_options:
            case "1. Numéro simple    (35:1)":
                num_simple()
            case "2. Cheval / Split   (17:1)":
                num_split_n2()
            case "3. Street           (11:1)":
                num_street()
            case "4. Carré / Corner   (8:1)":
                pass
            case "5. Sixain           (5:1)":
                pass
            case "6. Douzaine         (2:1)":
                pass
            case "7. Colonne          (2:1)":
                pass
            case "8. Rouge/Noir       (1:1)":
                pass
            case "9. Pair / Impair    (1:1)":
                pass
            case "10. Manque / Passe  (1:1)":
                pass
            case "11. Exit":
                pass

        while True:
            mise = input(f"enter a mise (sold = {config['sold']}):  ").strip().lower()
            if "all" in mise and "-" in mise:
                mise = mise.replace("all", "").replace("-", "")
                mise = mise.strip()
                if not mise.isdigit():
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                if int(mise) >= config["sold"]:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                mise = config["sold"] - int(mise)
                clear_lines()
                print(f"Enter a mise:   {mise}")
            elif mise == "all":
                mise = config["sold"]
                clear_lines()
                print(f"Enter a mise:   {mise}")
            elif "last" in mise and ("-" in mise or "+" in mise):
                operateur = "+" if "+" in mise else "-"
                mise = mise.replace("last", "").replace("-", "").replace("+", "")
                mise = mise.strip()
                if not mise.isdigit():
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                if operateur == "+":
                    if last_mise + int(mise) >= config["sold"]:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    mise = last_mise + int(mise)
                    clear_lines()
                    print(f"Enter a mise:   {mise}")
                else:
                    if last_mise - int(mise) <= 0:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    mise = last_mise - int(mise)
                    clear_lines()
                    print(f"Enter a mise:   {mise}")

            elif mise == "last":
                if last_mise > config["sold"]:
                    clear_lines()
                    continue
                mise = last_mise
                clear_lines()
                print(f"Enter a mise:   {mise}")

            elif ("half" in mise or mise == "h") and ("-" in mise or "+" in mise):
                operateur = "+" if "+" in mise else "-"
                mise = (
                    mise.replace("half", "")
                    .replace("-", "")
                    .replace("+", "")
                    .replace("h", "")
                )
                mise = mise.strip()
                if not mise.isdigit():
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                if operateur == "+":
                    if config["sold"] // 2 + int(mise) >= config["sold"]:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    mise = config["sold"] // 2 + int(mise)
                else:
                    if config["sold"] // 2 - int(mise) <= 0:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    mise = config["sold"] // 2 - int(mise)
                clear_lines()
                print(f"Enter a mise:   {mise}")

            elif mise == "half" or mise == "h":
                mise = config["sold"] // 2
                clear_lines()
                print(f"Enter a mise:   {mise}")
            elif any(
                x in mise for x in ["r", "rand", "random", "aleatoire", "aléatoire"]
            ):
                val = mise
                for x in ["rand", "random", "aleatoire", "aléatoire", "r"]:
                    val = val.replace(x, "")
                val = val.strip()
                parts = val.split()

                if (
                    len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit()
                ):  # Syntaxe: "r 50 200"
                    start = int(parts[0])
                    stop = min(int(parts[1]), int(config["sold"]))
                    if stop <= start:
                        mise = min(max(start, 1), int(config["sold"]))
                    else:
                        mise = random.randrange(start, stop)
                elif len(parts) == 1 and parts[0].isdigit():  # Syntaxe: "r 50"
                    start = int(parts[0])
                    if start >= int(config["sold"]):
                        mise = max(1, int(config["sold"]) - 1)
                    else:
                        mise = random.randrange(start, int(config["sold"]))
                else:
                    if int(config["sold"]) > 20:
                        mise = random.randrange(int(config["sold"]))
                    else:
                        mise = random.randrange(
                            11, int(config["sold"]) + 1
                        )  # Syntaxe: "r"
                clear_lines()
                print(f"Enter a mise:   {mise}")

            elif not mise.isdigit() or int(mise) > config["sold"] or 10 > int(mise):
                cprint("incorrect", ERROR)
                time.sleep(0.3)
                clear_lines(2)
                continue
            mise, last_mise = int(mise), int(mise)

            break
        time.sleep(0.5)
        affichage()


roulette_game()
