from tools import *
import random, time


def Red_or_Black_game(mode="normal"):
    """mode normal, +50 or easy"""
    (
        familys,
        values,
        historique,
        stats,
        color,
        card,
        tour,
        mise,
        prediction,
        last_mise,
        last_prediction,
    ) = (
        ["♥", "♦", "♣", "♠"],
        [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ],
        [],
        {},
        "",
        [],
        1,
        0,
        "",
        0,
        "",
    )
    cards = [f"{value}{color}" for color in familys for value in values]

    def game(tour=1):
        nonlocal stats, color, card, mise, prediction, last_mise, last_prediction
        random.shuffle(cards)
        card = cards.pop()
        historique.append(card)
        stats = {
            "Rouge": f'%{(len(list(filter(lambda x: True if "♥" in x or "♦" in x else False, cards))) * 100)// len(cards):.2f}',
            "Noir": f'%{(len(list(filter(lambda x: True if "♣" in x or "♠" in x else False, cards))) * 100)// len(cards):.2f}',
        }
        color = (
            f"{ROUGE_FLASH}Rouge{RESET}"
            if "♥" in card or "♦" in card
            else f"{NOIR}Noir{RESET}"
        )
        if tour != 1:
            while True:
                mise = input("Enter a mise:   ").strip().lower()
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

                elif "half" in mise and ("-" in mise or "+" in mise):
                    operateur = "+" if "+" in mise else "-"
                    mise = mise.replace("half", "").replace("-", "").replace("+", "").replace("h", "")
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
                elif any(x in mise for x in ["r", "rand", "random", "aleatoire", "aléatoire"]):
                    val = mise
                    for x in ["rand", "random", "aleatoire", "aléatoire", "r"]:
                        val = val.replace(x, "")
                    val = val.strip()
                    parts = val.split()

                    if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():  # Syntaxe: "r 50 200"
                        mise = random.randrange(int(parts[0]), min(int(parts[1]), config["sold"]))
                    elif len(parts) == 1 and parts[0].isdigit():  # Syntaxe: "r 50"
                        mise = random.randrange(int(parts[0]), config["sold"])
                    else:
                        mise = random.randrange(20, config["sold"])  # Syntaxe: "r"
                    clear_lines()
                    print(f"Enter a mise:   {mise}")

                elif not mise.isdigit() or int(mise) > config["sold"]:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                mise, last_mise = int(mise), int(mise)
                prediction = input("Enter your prediction (R/N):   ").lower().strip()
                if prediction in exit:
                    clear_lines(2)
                    continue
                elif prediction == "last":
                    prediction = last_prediction
                elif prediction in ["ra", "rand", "random", "aleatoire", "aléatoire"]:
                    Colors_list = (f"{ROUGE_FLASH}Rouge{RESET}", f"{NOIR}Noir{RESET}")
                    prediction = random.choice(Colors_list)
                elif prediction in ["ch", "change", "not", "c"]:
                    prediction = (
                        f"{ROUGE_FLASH}Rouge{RESET}"
                        if last_prediction == f"{NOIR}Noir{RESET}"
                        else f"{NOIR}Noir{RESET}"
                    )
                elif prediction in [
                    "r",
                    "red",
                    "rouge",
                    "1",
                    "sang",
                    "s",
                    "b",
                    "blood",
                ]:
                    prediction = f"{ROUGE_FLASH}Rouge{RESET}"
                else:
                    prediction = f"{NOIR}Noir{RESET}"
                last_prediction = prediction
                cprint(f"You chosed §{prediction}!", SOULIGN2)
                time.sleep(0.35)
                break

    def affichage():
        nonlocal stats, color, mise
        random_card = random.choice(cards)
        clear()
        hist_affichage = [
            f"{ROUGE_FLASH}{x}{RESET}" if "♥" in x or "♦" in x else f"{NOIR}{x}{RESET}"
            for x in historique
        ]
        hist_str = " ".join(hist_affichage)
        print("+--------------------------------------------------+\n")
        print(f"{' ' * 13}RED OR BLACK\n")
        for i in range(30):
            random_card = random.choice(cards)
            print(
                f"\r{' ' * 15}[ {ROUGE if "♥" in random_card or "♦" in random_card else NOIR}{random_card}{RESET} ] ",
                end="",
                flush=True,
            )
            time.sleep(0.02 + (i * 0.01))
        print(
            f"\r{' ' * 15}[ {ROUGE if "♥" in card or "♦" in card else NOIR}{card}{RESET} ]   \n"
        )
        print(f"{' ' * 6}{ROUGE_FLASH}Rouge{RESET}{' ' * 13}{NOIR}Noir{RESET}")
        print(f"{' ' * 6}{stats['Rouge']}{' ' * 11}{stats['Noir']}\n")
        print("----------------------------------------------\n")
        if tour >= 2:
            if prediction == color:
                if mode == "normal":
                    config["sold"] += mise
                elif mode == "+50":
                    config["sold"] += 1.5 * mise
                elif mode == "easy":
                    config["sold"] += mise * 2

                cprint(f"You predicted {prediction} and §you Won!!", SUCCESS)
                cprint(
                    f"You won €{mise if mode == "normal" else 1.5 * mise if mode == "+50" else mise * 2}!",
                    VERT_FLASH,
                )
            else:
                if mode == "normal":
                    config["sold"] -= mise
                elif mode == "+50":
                    config["sold"] -= 1.5 * mise
                elif mode == "easy":
                    config["sold"] -= 0.9 * mise

                cprint(f"You predicted {prediction}  §(wrong...)!", ERROR)
                cprint(
                    f"You lost €{mise if mode == "normal" else 1.5 * mise if mode == "+50" else mise * 0.9}!",
                    ROUGE_FLASH,
                )
            input()
            mise = 0
            clear_lines(5)
            print("----------------------------------------------\n")

        print(f"mise : {mise} €")
        print(f"solde : {config['sold']} €\n")
        print(hist_str)
        print("\n+--------------------------------------------------+")

    while config["sold"] > 0 and cards:
        game(tour)
        affichage()
        if mode == "easy" and config["sold"] <= 10:
            break
        tour += 1


Red_or_Black_game()
