from tools import *
import random, sys, time, json


def Red_or_Black_game(mode="normal", cheat=True):
    """mode normal, +50, easy or hard"""
    families = ["♣", "♠", "♦", "♥"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    historique = []
    stats = {}
    color = ""
    card = []
    tour = 1
    mise = 0
    prediction = ""
    last_mise = 0
    last_prediction = ""
    journal = []
    total_won = []
    total_lost = []
    score = 0
    highest_score = 0
    highest_sold = 0
    cheat_use = 0

    cards = [f"{value}{color}" for color in families for value in values]
    if mode in {"+50", "easy"}:
        config["sold"] *= 1.5

    def save_high_score(win_serie_score, sold_score):
        if win_serie_score > config["highest_win_serie_R/B"]:
            config["highest_win_serie_R/B"] = win_serie_score
            save_config(config)
        if sold_score > config["highest_sold_R/B"]:
            config["highest_sold_R/B"] = sold_score
            save_config(config)

    def game(current_tour=1):
        nonlocal stats, color, card, mise, prediction, last_mise, last_prediction, tour, cheat_use
        random.shuffle(cards)
        card = cards.pop()
        historique.append(card)
        if not cards:
            return
        stats = {
            "Rouge": (
                len(
                    list(
                        filter(lambda x: True if "♥" in x or "♦" in x else False, cards)
                    )
                )
                * 100
            )
            / len(cards),
            "Noir": (
                len(
                    list(
                        filter(lambda x: True if "♣" in x or "♠" in x else False, cards)
                    )
                )
                * 100
            )
            / len(cards),
        }
        color = (
            f"{ROUGE_FLASH}Rouge{RESET}"
            if "♥" in card or "♦" in card
            else f"{NOIR}Noir{RESET}"
        )
        if current_tour != 1:
            while True:
                mise = input("Enter a mise:   ").strip().lower()
                if mise in exit:
                    return

                if mise == "capa":
                    clear()
                    print("\n" * 17)
                    print(f"\t{'code':<15}{'utilisation'}\nMISE:")
                    slow_type(
                        f"\t{'n':<15}{'just mise the number n'}\n\t{'all':<15}{'mise all the sold'}\n\t{'all - n':<15}{'mise the all sold - n€'}\n\t{'last':<15}{'mise the last montant mised'}\n\t{'last +/- n':<15}{'last_mise + ou - n€'}\n\t{'half':<15}{'mise half of the sold'}\n\t{'half +/- n':<15}{'half of the sold +/- n€'}\n\t{'r':<15}{'random mise btw 11 and sold'}\n\t{'r n1':<15}{'mise and random amount btw n1 and sold'}\n\t{'r n1 n2':<15}{'mise and random amount btw n1 and n2'}\n",
                        tps_btw_letters=0.008,
                    )
                    print("\nPREDICT:")
                    slow_type(
                        f"\t{'ex, n, no, q':<15}{'revient au choix de la mise'}\n\t{'last':<15}{'re-enter the last_prediction'}\n\t{'ra, al':<15}{'choose random prediction'}\n\t{'ch, not':<15}{'enter the opposite of the last_prediction'}\n\t{'logic, best':<15}{'chose the best option by the stat, if equals -> random'}\n\t{'r, blood, red':<15}{'prediction = ROUGE'}\n\t{'any else':<15}{'prediction = NOIR'}",
                        tps_btw_letters=0.008,
                    )
                    print("\n" * 2)
                    input()
                    clear()
                    continue
                elif cheat and hach_word(mise) == config["code"]:
                    cheat_use += 1
                    clear_lines()
                    print(arc_en_ciel("secret"))
                    time.sleep(0.5)
                    clear_lines()
                    print("\n" * 2)
                    print(f"\t{'dark code':<15}{'utilisation'}\nMISE:")
                    slow_type(
                        f"\t{A1Z26(txtt='19-15-12-4  +-/-*  14', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='1-16-16-12-9-17-21-5  +  15-21  *  14  19-21-18  12-5  19-15-12-4', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='3-1-18-4  ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='1-6-6-9-3-8-5  12-5-19  9-14-6-15-19  4-5  3-1-18-4  1-3-21-20-512-12-5 ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='3-8-(-1-14-7-5-) ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='18-5-18-15-12-12  12-1  3-1-18-20-5  (-5-14  3-12-5-1-14-1-14-20  12-5  20-15-21-20-)  ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='9-14-6-/-6-21-12-12  14 ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='16-5-18-13-5-20  4-5  13-9-19-5-18  2-9-5-14  1-21  4-5-19-19-21-19  4-21  19-15-12-4-,  13-9-19-5  =  14-. ', choix="2. Decode from A1-Z26")}\n",
                        tps_btw_letters=0.008,
                    )
                    print("\nPREDICT:")
                    slow_type(
                        f"\t{A1Z26(txtt='16-5-18-6-5-3-20 / -18-9-7-8-20  ', choix="2. Decode from A1-Z26").replace('20', 't'):<15}{A1Z26(txtt='16-18-5-4-9-3-20  12-1  2-15-14-14-5  22-1-12-5-21-18  4-5  3-1-18-4-!  ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='14-15-20 / -9-13-16-5-18-6-5-3-20 ', choix="2. Decode from A1-Z26").replace('20', 't'):<15}{A1Z26(txtt='16-18-5-4-9-3-20  12-1  13-1-21-22-1-9-19-5  22-1-12-5-21-18  4-5  3-1-18-4-!  ', choix="2. Decode from A1-Z26")}",
                        tps_btw_letters=0.008,
                    )
                    print("\n" * 3)
                    input()
                    clear_lines(17)
                    continue
                # darks code
                elif cheat and ("sold" in mise and ("+" in mise or "*" in mise)):
                    cheat_use += 1
                    operateur = "*" if "*" in mise else "+"
                    mise = mise.replace("sold", "").replace("+", "").replace("*", "")
                    mise = mise.strip()
                    if not mise.isdigit():
                        cprint("incorrect", ALERTE_CRITIQUE)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    if operateur == "+":
                        config["sold"] += float(mise)
                        cprint(f"sold += {float(mise)} -> {config['sold']}", WARNING)
                    elif operateur == "*":
                        config["sold"] *= float(mise)
                        cprint(f"sold *= {float(mise)} -> {config['sold']}", WARNING)
                    time.sleep(0.75)
                    clear_lines(2)
                    continue
                elif cheat and "card" in mise:
                    cheat_use += 1
                    print(f"card -> {card},   color -> {color}")
                    input()
                    clear_lines(3)
                    continue
                elif cheat and "ch" in mise:
                    cheat_use += 1
                    tour += 1
                    cards.append(card)
                    historique.remove(card)
                    clear_lines()
                    game(tour)
                elif cheat and ("inf" in mise or "full" in mise):
                    cheat_use += 1
                    mise = mise.replace("full", "").replace("inf", "")
                    mise = mise.strip()
                    if not mise.isdigit():
                        cprint("incorrect", ALERTE_CRITIQUE)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    mise = float(mise)
                    clear_lines()
                    print(f"Enter a mise:   {mise}")

                elif "all" in mise and "-" in mise:
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

                prediction = input("Enter your prediction (R/N):   ").lower().strip()

                # darks code
                if cheat and (prediction == "perfect" or prediction == "right"):
                    cheat_use += 1
                    prediction = color
                elif cheat and (prediction == "not" or prediction == "false"):
                    cheat_use += 1
                    prediction = (
                        f"{NOIR}Noir{RESET}"
                        if color == f"{ROUGE_FLASH}Rouge{RESET}"
                        else f"{ROUGE_FLASH}Rouge{RESET}"
                    )

                elif prediction in exit:
                    clear_lines(2)
                    continue
                elif prediction == "last":
                    prediction = last_prediction
                elif prediction in [
                    "ra",
                    "rand",
                    "random",
                    "aleatoire",
                    "aléatoire",
                    "al",
                ]:
                    prediction = random.choice(
                        [f"{ROUGE_FLASH}Rouge{RESET}", f"{NOIR}Noir{RESET}"]
                    )
                elif prediction in ["ch", "change", "not", "c"]:
                    prediction = (
                        f"{ROUGE_FLASH}Rouge{RESET}"
                        if last_prediction == f"{NOIR}Noir{RESET}"
                        else f"{NOIR}Noir{RESET}"
                    )
                elif prediction in [
                    "st",
                    "stat",
                    "stats",
                    "lo",
                    "logic",
                    "be",
                    "best",
                    "better",
                ]:
                    pourc_red, pourc_black = float(stats["Rouge"]), float(stats["Noir"])
                    if pourc_black < pourc_red:
                        prediction = f"{ROUGE_FLASH}Rouge{RESET}"
                    elif pourc_red < pourc_black:
                        prediction = f"{NOIR}Noir{RESET}"
                    else:
                        prediction = random.choice(
                            [f"{ROUGE_FLASH}Rouge{RESET}", f"{NOIR}Noir{RESET}"]
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

    def affichage(animation=True):
        nonlocal stats, color, mise, journal, total_won, score, highest_score, highest_sold
        if not cards:
            return
        clear()
        hist_affichage = [
            f"{ROUGE_FLASH}{x}{RESET}" if "♥" in x or "♦" in x else f"{NOIR}{x}{RESET}"
            for x in historique
        ]
        hist_str = " ".join(hist_affichage)
        cprint(
            "enter capa as mise to see all the dispo codes, and config['code'] to see darks code",
            WARNING,
        )
        print(f"+{'-' * 50}+\n")
        print(f"{' ' * 13}RED OR BLACK\n")
        if animation and not animation == "fast":
            for i in range(25):
                random_card = random.choice(cards)
                print(
                    f"\r{' ' * 15}[ {ROUGE if "♥" in random_card or "♦" in random_card else NOIR}{random_card}{RESET} ] ",
                    end="",
                    flush=True,
                )
                time.sleep(0.02 + (i * 0.01))
        print(
            f"\r{' ' * 15}[ {ROUGE if '♥' in card or '♦' in card else NOIR}{card}{RESET} ]   \n"
        )
        print(f"{' ' * 6}{ROUGE_FLASH}Rouge{RESET}{' ' * 13}{NOIR}Noir{RESET}")
        print(f"{' ' * 6}%{stats['Rouge']:.2f}{' ' * 11}%{stats['Noir']:.2f}\n")
        print(f"{'-'*46}\n")
        if tour >= 2:
            if prediction == color:
                if mode == "+50":
                    config["sold"] += 1.5 * mise
                elif mode == "easy":
                    config["sold"] += mise * 2
                elif mode == "hard":
                    config["sold"] += mise * 0.7
                else:
                    config["sold"] += mise

                cprint(f"You predicted {prediction} and §you Won!!", SUCCESS)
                cprint(
                    f"You won €{mise * 1.5 if mode == '+50' else mise * 2 if mode == 'easy' else mise * 0.7 if mode == 'hard' else mise}!",
                    VERT_FLASH,
                )
                score += 1
            else:
                if mode == "+50":
                    config["sold"] -= 1.5 * mise
                elif mode == "easy":
                    config["sold"] -= 0.9 * mise
                elif mode == "hard":
                    config["sold"] -= 1.7 * mise
                else:
                    config["sold"] -= mise

                cprint(f"You predicted {prediction}  §(wrong...)!", ERROR)
                cprint(
                    f"You lost €{mise * 1.5 if mode == '+50' else mise * 0.9 if mode == 'easy' else mise * 1.7 if mode == 'hard' else mise}!",
                    ROUGE_FLASH,
                )
                score = 0
            highest_score = max(score, highest_score)
            highest_sold = max(config["sold"], highest_sold)
            NOIRE, VERTT_FLASH = NOIR, VERT_FLASH
            total_won.append(float(mise) if prediction == color else 0)
            total_lost.append(float(mise) if prediction != color else 0)

            journal.append(
                {
                    "card": f'{ROUGE if "♥" in card or "♦" in card else NOIRE}{card}{RESET}',
                    "guess": prediction,
                    "mise": f"{mise} €",
                    "result": (
                        f"{VERTT_FLASH}WIN{RESET}"
                        if prediction == color
                        else f"{ROUGE_FLASH}LOSS{RESET}"
                    ),
                    "change": (
                        f"{VERTT_FLASH}+{mise} €{RESET}"
                        if prediction == color
                        else f"{ROUGE_FLASH}-{mise} €{RESET}"
                    ),
                    "balance": f'{config["sold"]} €',
                }
            )
            if not animation == "fast":
                afficher_journal = input("").lower().strip()
                if afficher_journal in [
                    "j",
                    "jour",
                    "journal",
                    "st",
                    "stat",
                    "lo",
                    "logic",
                ]:
                    journal_transactions()

            mise = 0
            clear_lines(5)
            print(f"{'-' * 46}\n")

        print(f"mise : {mise} €")
        print(f"sold : {config['sold']} €\n")
        print(hist_str)
        print(f"\n+{'-' * 50}+")

    def journal_transactions():
        nonlocal journal, total_won, cheat_use
        clear()
        print(f"+{'-' * 64}+\n")
        print(f"{'TRANSACTION HISTORY'.center(64)}\n")
        print(f"{'-' * 66}\n")
        print(
            f"{'#':<5}{'Card':<8}{'Guess':<9}{'Mise':<9}{'Result':<11}{'Change':<12}{'Balance':<10}\n"
        )
        for i, entry in enumerate(journal, 1):
            idx_str = f"{i:02d}"
            print(
                f"{idx_str:<5}"
                f"{entry['card']:<17}"
                f"{entry['guess']:<18}"
                f"{entry['mise']:<9}"
                f"{entry['result']:<20}"
                f"{entry['change']:<21}"
                f"{entry['balance']:<10}"
            )
        Wins, Losses, Win_rate = 0, 0, 0
        for i in range(len(journal)):
            Wins += 1 if f"{VERT_FLASH}WIN{RESET}" in journal[i].values() else 0
            Losses += 1 if f"{ROUGE_FLASH}LOSS{RESET}" in journal[i].values() else 0
        Win_rate = 100 / (Wins + Losses) * Wins
        p_m = formate_collections(
            [
                "-" if journal[i]["result"] == f"{ROUGE_FLASH}LOSS{RESET}" else "+"
                for i in range(len(journal))
            ]
        )
        for sim in p_m:
            if sim == " ":
                print(" ", end="")
            elif sim == "+":
                print(f"{VERT_FLASH}+{RESET}", end="")
            elif sim == "-":
                print(f"{ROUGE_FLASH}-{RESET}", end="")
        print(f"\n{'-' * 66}")
        print(f"\n{VERT_FLASH}Wins{RESET}           : {Wins}")
        print(f"{ROUGE_FLASH}Losses{RESET}         : {Losses}")
        print(
            f"{WARNING}Win rate{RESET}       {LOG_DISCRET}:{RESET} {ROUGE_FLASH if float(Win_rate) < 50 else VERT_FLASH}{float(Win_rate)} %{RESET}"
        )
        if cheat:
            cprint(f"Cheat used {cheat_use} times", ALERTE_CRITIQUE)
        print(f"\n{VERT_FLASH}Total Won      : +{sum(total_won)} €{RESET}")
        print(f"{ROUGE_FLASH}Total Lost     : -{sum(total_lost)} €{RESET}")
        print(
            f"{VERT_FLASH if sum(total_won) - sum(total_lost) >= 0 else ROUGE_FLASH}Net Profit     : {sum(total_won) - sum(total_lost)} €{RESET}"
        )
        if 200 + (sum(total_won) - sum(total_lost)) != config["sold"]:
            cprint("YOU CHEATED!!", ALERTE_CRITIQUE)
        print(
            f"{VERT_FLASH if config['sold'] >= 0 else ROUGE_FLASH}Current Balance: {config['sold']} €{RESET}"
        )

        input()
        affichage("fast")

    while config["sold"] > 10 and cards:
        game(tour)
        if mise in exit:
            return
        affichage(False)
        tour += 1
    journal_transactions()
    save_high_score(highest_score, highest_sold)


while True:
    parameter = menu_options(
        ["1. Normal", "2. +50", "3. Easy", "4. Hard", "5. Exit"], "Red or Black GAME"
    )
    match parameter:
        case "1. Normal":
            mode = "normal"
        case "2. +50":
            mode = "+50"
        case "3. Easy":
            mode = "easy"
        case "4. Hard":
            mode = "hard"
        case "5. Exit":
            sys.exit()  # return

    config["sold"] = 200
    Red_or_Black_game(mode, False)
