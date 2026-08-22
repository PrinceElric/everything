from tools import *
import time, random, sys, json, string, os

# -------------------------------------------------------------------------------

# --- Jeux ---
def mise():
    while True:
        mise = input(f'Enter a mise (sold = {config['sold']}):  ')
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
        return mise


def pendu_game(mode="normal"):
    """launch mytique pendu_game. Multiple mode"""
    global mots_921
    mots = mots_921.copy()
    mots, letter, letters, count_pendu, false_answers, count_down = (
        list(filter(lambda x: True if len(x) > 5 else False, mots_921)),
        "",
        [],
        0,
        [],
        6,
    )
    word = random.choice(mots)
    word = enlever_accents(word).lower()
    pendu_etapes = (
        " +---+\n     \n     \n     \n     ",
        " +---+\n |   \n     \n     \n     ",
        " +---+\n |   \n O   \n     \n     ",
        " +---+\n |   \n O   \n/|   \n     ",
        " +---+\n |   \n O   \n/|\\  \n     ",
        " +---+\n |   \n O   \n/|\\  \n/    ",
        " +---+\n |   \n O   \n/|\\  \n/ \\  ",
    )

    def start():
        global mots_921
        mots_921 = list(filter(lambda x: True if len(x) > 5 else False, mots_921))
        nonlocal mots, count_down, letter, letters, count_pendu, false_answers, pendu_etapes, word
        mots = mots_921.copy()
        letter, letters, count_pendu, false_answers, count_down = (
            "",
            [],
            0,
            [],
            6,
        )
        if not mots:
            raise ValueError(
                "La liste des mots du pendu est vide. Vérifiez que mots_francais.py ou mots_francais.json est présent."
            )
        word = random.choice(mots)
        word = enlever_accents(word).lower()
        pendu_etapes = (
            " +---+\n     \n     \n     \n     ",
            " +---+\n |   \n     \n     \n     ",
            " +---+\n |   \n O   \n     \n     ",
            " +---+\n |   \n O   \n/|   \n     ",
            " +---+\n |   \n O   \n/|\\  \n     ",
            " +---+\n |   \n O   \n/|\\  \n/    ",
            " +---+\n |   \n O   \n/|\\  \n/ \\  ",
        )

    def show_word(mode="normal"):
        nonlocal count_down, word, letters
        if not letters and mode == "normal":
            print("_" * len(word))
            return
        elif not letters and mode == "facile":
            letters.append(word[0])
        elif not letters and mode == "tr_facile":
            letters.append(word[0])
            letters.append(word[-1])
        elif not letters and mode == "difficile":
            count_down = 4
        elif mode == "debug":
            print(f"word is {VERT_FLASH + SOULIGN2}{word}{RESET}")
        print("".join(i if i in letters else "_" for i in word))
        print()

    def enter_letter():
        nonlocal letter, false_answers, word, count_pendu
        while True:
            remaining_attempts = max(0, count_down - len(false_answers))
            cprint(f"Attempts left: {remaining_attempts}", WARNING)
            if false_answers:
                print(
                    f"{ROUGE_FLASH}False guesses:   {', '.join(false_answers)}{RESET}"
                )
            letter = input("enter a letter or a full word:    ").strip().lower()
            normalized_input = enlever_accents(letter)

            if normalized_input in ["exit", "quit", "ex"]:
                clear()
                sys.exit()
            elif normalized_input == "re":
                clear()
                run()
            elif normalized_input == word:
                verif_game(True)
                return
            if len(normalized_input) != 1 or not normalized_input.isalpha():
                cprint("JUST ONE LETTER OR A FULL WORD!", ERROR)
                time.sleep(0.5)
                if false_answers:
                    clear_lines(3)
                else:
                    clear_lines(2)
                continue

            clear_lines(1)
            if normalized_input in letters or normalized_input in false_answers:
                cprint("Answer already gave!", WARNING)
                time.sleep(1)
                clear()
                return
            if normalized_input in word:
                print(
                    f"enter a letter or a full word:    {VERT_FLASH}{GRAS}{normalized_input}{RESET}"
                )
                print(f"{normalized_input} {SUCCESS}is in the word!{RESET}")
                letters.append(normalized_input)
            else:
                print(
                    f"enter a letter or a full word:    {ROUGE_FLASH}{GRAS}{normalized_input}{RESET}"
                )
                print(f"{normalized_input} {ERROR}not in the word!{RESET}")
                count_pendu += 1
                false_answers.append(normalized_input)
            time.sleep(1)
            return

    def show_pendu(level: int = 0) -> None:
        print()
        for line in pendu_etapes[level].split("\n"):
            print(line)
        match level:
            case 0:
                clear_lines(3)
            case 1:
                clear_lines(2)
            case 2 | 3:
                clear_lines(1)
        print()

    def verif_game(full_word=False):
        if not full_word:
            if len(false_answers) >= count_down:
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint(
                    f"You gave {len(false_answers)} bad answers!",
                    ROUGE_FLASH + SOULIGN2,
                )
                cprint(f"You had {len(letters)} good answers!", SUCCESS)
                cprint("But...", ROUGE_FLASH)
                cprint("You lost!", ERROR)
                end()
            elif len(letters) == len(set(word)):
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint("You found all the letters!", VERT_FLASH + SOULIGN2)
                cprint("And...", VERT)
                cprint("You won", SUCCESS)
                end()
            return
        cprint(f"You guessed the word!, it was good {word}", SUCCESS)
        print(
            f"{VERT}You gave {len(letters)} good answers {ROUGE}and {len(false_answers)} bad answers!{RESET}"
        )
        cprint("You won!", SUCCESS)
        end()

    def end():
        choice = input("New round? (y/n)\n").strip().lower()
        if choice in ["y", "yes", "o", "oui", "1"]:
            run()
        else:
            return

    def main(mode="normal"):
        while True:
            nonlocal count_pendu
            clear()
            show_pendu(count_pendu)
            verif_game()
            show_word(mode)
            enter_letter()

    def run(mode="normal"):
        faire_titre_section("Pendu Game")
        start()
        main(mode)

    run(mode)


def paper_scissor_game():
    """Execut legendary paper_scissor-game with cheat capa"""
    faire_titre_section("Rock, Paper, Scissor Game")

    choices, won, lose = ("rock", "paper", "scissor"), 0, 0

    while True:
        computer = random.choice(choices)
        player = input("\nEnter your choice (q to quit): ")
        if player.lower() == "q":
            break
        cheat = player != player.lower()

        if not player:
            player = random.choice(choices)
            print(f"Player chose {player.upper()}")
        else:
            player = player.lower()

        if player not in choices:
            cprint("You chose an invalid option", ERROR)
            time.sleep(0.7)
            clear_lines(2)
            continue

        if cheat:
            if player == "rock":
                computer = "scissor"
            elif player == "paper":
                computer = "rock"
            elif player == "scissor":
                computer = "paper"

        print(f"the computer chose: {computer}")

        if player == computer:
            print("It's a tie")
        elif player == "rock" and computer == "paper":
            cprint("You lost!", ERROR)
            lose += 1
        elif player == "paper" and computer == "scissor":
            cprint("You lost!", ERROR)
            lose += 1
        elif player == "scissor" and computer == "rock":
            cprint("You lost!", ERROR)
            lose += 1
        else:
            cprint("You won!", SUCCESS)
            won += 1

    print(f"{SUCCESS}you won {won} times,{RESET} {ERROR}and lost {lose} times{RESET}")
    print(
        f"{SUCCESS}Good game!{RESET}"
        if won > lose
        else f"{ERROR}You will do it better next time!{RESET}"
    )
    input("Press enter to exit\n>>>    ")


def number_guess_game(minimum=0, maximum=100):
    """start number_guess_game, with a cheat capa!"""
    faire_titre_section("Number Guessing Game!")
    (
        number_rand,
        guesses,
        my_number,
        choix,
    ) = (
        int(random.randint(minimum, maximum)),
        0,
        None,
        (1, 3),
    )

    def enter_num():
        nonlocal my_number, guesses
        while True:
            user_input = input(
                f"Please enter a number between {minimum} and {maximum}: "
            )
            if user_input.lower() in exit:
                cprint("Exiting the game.", WARNING)
                sys.exit()
            elif user_input.lower() == "re":
                cprint("Restarting the game.", WARNING)
                number_guess_game(minimum, maximum)
            elif user_input.strip() != user_input:
                high_low(cheat=True)
            try:
                my_number = int(user_input.strip())
            except ValueError:
                cprint("Invalid input. Please enter a valid number.", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue

            if minimum <= my_number <= maximum:
                guesses += 1
                break

    def high_low(cheat=False):
        nonlocal number_rand, my_number, guesses
        if cheat:
            for _ in range(2):
                a = random.choice(choix)
                if a == 1:
                    print(f"{my_number} is too LOW! Try again!")
                    enter_num()

                else:
                    print(f"{my_number} is too HIGH! Try again!")
                    enter_num()
            end()
        if int(my_number) > number_rand:
            print(f"{my_number} is too High! Try again!")
        else:
            print(f"{my_number} is too Low! Try again!")

    def end():
        cprint("Congratulations! You guessed the number!", SUCCESS)
        cprint(f"You guessed {guesses} times!", WARNING)
        input("")
        sys.exit()

    while True:
        enter_num()
        if my_number == number_rand:
            end()
        high_low()


def code_names_game():
    """reprodution of code_names"""
    faire_titre_section(code_names_game)

    def afficher_grille(grille, mode="joueur"):
        """Affiche la grille selon le mode : 'joueur' (brut) ou 'maitre' (avec filtres)"""
        for e in range(5):
            for i in range(5):
                mot = grille[e][i]
                if mode == "maitre":
                    if mot in accepted_prop:
                        print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")
                    elif mot in mots_rouges:
                        print(f"{ROUGE}{mot:<15}{RESET}", end="")
                    elif mot in mots_verts:
                        print(f"{VERT}{mot:<15}{RESET}", end="")
                    else:
                        print(f"{mot:<15}", end="")

                else:
                    if mot in accepted_prop:
                        print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")
                    else:
                        print(f"{mot:<15}", end="")
            print("")

    def repetition_aceptation_rep(props):
        """augmente le nb de rep gave (de 1) et ajoute la proposition a une liste pour ensuite les masquer (next turn)"""
        nonlocal nb_rep_gave, accepted_prop
        nb_rep_gave += 1
        accepted_prop.append(props)

    mots = random.choices(mots_921, k=25)
    while len(set(mots)) != len(mots):
        mots = random.choices(mots_921, k=25)
    accepted_prop, rouge, vert, pts, mots2, nb_rep_gave = (
        [],
        (range(3)),
        (range(5)),
        0,
        mots.copy(),
        0,
    )
    random.shuffle(mots)
    random.shuffle(mots2)
    matrice, matrice2 = (
        (mots[:5]),
        (mots[5:10]),
        (mots[10:15]),
        (mots[15:20]),
        (mots[20:]),
    ), ((mots2[:5]), (mots2[5:10]), (mots2[10:15]), (mots2[15:20]), (mots2[20:]))
    mots_rouges = [matrice[4][i] for i in rouge]
    mots_verts = [matrice[0][i] for i in vert] + [matrice[1][i] for i in vert[:2]]
    while not set(accepted_prop) == set(mots_verts):
        clear()
        afficher_grille(matrice, mode="maitre")

        key_word = (
            input("Enter a word for the person can devine:\n>>>   ").strip().lower()
        )
        reponses = []

        while True:
            continueeee = 0
            reponses.append(
                input("What are the answers ?(q to quit)(enter for each one):   ")
                .lower()
                .strip()
            )
            for i in mots_rouges:
                if i in reponses:
                    print(f"{ROUGE}Incorrect enter{RESET}")
                    reponses.remove(i)
                    continueeee = 1
            if continueeee == 1:
                continue
            if "q" in reponses:
                reponses.pop()
                break
            for i in reponses:
                if i not in mots:
                    print(f"{ROUGE}Incorrect enter{RESET}")
                    print(
                        f"{ROUGE}{GRAS}IMPORTANT : Les answers entered have been deleted bc you made a mistake!{RESET}"
                    )
                    reponses = []
                    continueeee = 1
            if continueeee == 1:
                continue
            print("Element succesfuly added to the answers, what's the next ?")

        clear()
        nb_rep = 0
        print("The answers are: ", end="")
        for i in reponses:
            nb_rep += 1
            print(i, end="   ")
        print("")
        print(f"There are {nb_rep} rep at total")
        input("")
        clear()

        propositions, nb_rep_gave, nb_good_answ, pts_before = "", 0, 0, pts

        while True:
            clear()
            print(
                f"The player selected {nb_rep} words to find, the keyword is: {key_word}\n {VERT}GOOD LUKE{RESET}"
            )
            afficher_grille(matrice2)

            if nb_rep_gave == nb_rep:
                break
            propositions = (
                input(
                    f"Which answer propose you ?(again {nb_rep - nb_rep_gave} to enter):\n>>> "
                )
                .lower()
                .strip()
            )
            if propositions not in mots:
                print(f"{ROUGE}Propostion invalid{RESET}")
                print("The proposition isn't in the table, pls select an other one")
                input("")
                continue
            if propositions in mots_rouges:
                cprint(f"You lost!", ROUGE)
                cprint(f"the answers were : {reponses}", VERT + SOULIGN2)
                sys.exit(f"See you next time, you had {pts}pts")
            if propositions in mots_verts and propositions in reponses:
                pts += 1
                cprint(f"You won 1pts, you are now to {pts}pts!", VERT)
                repetition_aceptation_rep(propositions)
                nb_good_answ += 1
            elif propositions in reponses:
                cprint(
                    f"{VERT}Very well answer but you didn't make points{RESET}", VERT
                )
                cprint(f"You have {pts}!", VERT)
                repetition_aceptation_rep(propositions)
                nb_good_answ += 1
            else:
                print(f"{ROSE} Not good Answer,{RESET} keep schearching")
                repetition_aceptation_rep(propositions)
            input("")

        clear()
        print(
            f"The player selected the {nb_rep} reponses\n He found {nb_good_answ} good answers, and made {pts - pts_before}pts!"
        )
        input("Next round ?\n")

    cprint("You won!", VERT + SOULIGN2 + GRAS + ITALIC)
    print(f"You had {pts}pts !")


def pile_face_game(load=True):
    """just pile/face game! great animation and cheat capa->J"""
    faire_titre_section("Pile ou Face Game")
    choix = ("pile", "face")
    while True:
        reponse = input(">>>   ")
        if reponse.lower() in exit:
            break
        elif reponse.strip() != reponse:
            if load:
                loading_bar(1)
            slow_type("And it's...", 1, color=LOG_DISCRET)
            cprint(" FACE", LOG_DISCRET)
        else:
            if load:
                loading_bar(1)
            slow_type("And it's...", 1, color=LOG_DISCRET)
            choi = random.choice(choix)
            cprint(f" {choi}", LOG_DISCRET)


def word_guess_game(mode="nul", lenght_word_min=6, max_guesses=10):
    """the word_guess_game were you input word and make color on letter -> /help"""
    global mots_921
    mots_921 = list(
        filter(lambda x: True if len(x) >= lenght_word_min else False, mots_921)
    )
    word = random.choice(mots_921)
    word = enlever_accents(word)
    (
        letters,
        propositions_color,
        good_answ,
        esp,
        total_props,
        guesses,
        alphabet,
        letters_red,
        letters_yellow,
        letters_green,
    ) = (
        list(set(list(word))),
        [],
        0,
        "    " if len(word) <= 9 else "   ",
        [],
        0,
        string.ascii_lowercase,
        [],
        [],
        [],
    )

    def affichage():
        clear()
        faire_titre_section("Word Guessing Game!", largeur=51)
        print("")
        for i in alphabet:
            if i in letters_green:
                print(f"{SUCCESS}{i}{RESET}", end=" ")
            elif i in letters_yellow:
                print(f"{WARNING}{i}{RESET}", end=" ")
            elif i in letters_red:
                print(f"{ERROR}{i}{RESET}", end=" ")
            else:
                print(i, end=" ")
        print("\n")
        if mode == "debug":
            print(f" " * 28 + {word})
        for prop in total_props:
            print(f"{esp}{prop}", end="\n")
        if max_guesses - guesses <= 3:
            print("\n")
            if max_guesses - guesses != 1:
                cprint(f"Just {max_guesses - guesses} guesses left!", WARNING)
            else:
                cprint("Just 1 attempt left!!", WARNING)
                cprint("Be really carefull!", WARNING)
        print(f" " * 28 + "_" * len(word))

    def test_word():
        nonlocal good_answ, propositions_color, guesses, enter, guesses
        guesses += 1
        enter, propositions_color, good_answ = str(enter), [], 0
        for i in range(len(word)):
            if enter[i] == word[i]:
                propositions_color.append(f"{SUCCESS}{enter[i]}{RESET}")
                if not enter[i] in letters_green:
                    letters_green.append(enter[i])
                    if enter[i] in letters_yellow:
                        letters_yellow.remove(enter[i])
                good_answ += 1
            elif enter[i] in letters:
                propositions_color.append(f"{WARNING}{enter[i]}{RESET}")
                if not enter[i] in letters_yellow and enter[i] not in letters_green:
                    letters_yellow.append(enter[i])
            else:
                propositions_color.append(f"{ERROR}{enter[i]}{RESET}")
                if not enter[i] in letters_red:
                    letters_red.append(enter[i])
        total_props.append(" ".join(propositions_color))

    while not good_answ == len(word) and not guesses >= 10:
        while True:
            affichage()
            enter = (
                input(f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}")
                .lower()
                .strip()
            )
            if enter.lower() in exit:
                cprint("Exiting the game.", WARNING)
                return
            elif enter.lower() == "re":
                cprint("Restarting the game.", WARNING)
                time.sleep(0.3)
                word_guess_game()
            elif enter == "1":
                cprint(f"The word was: {SURLIGN2_BLANC}{word}", ERROR)
                return
            elif enter in ["-help", "/help"]:
                cprint("Type '1' to reveal the word and exit.", WARNING)
                cprint("Type 're' to restart the game.", WARNING)
                cprint("Type 'help' to receive help with the word", WARNING)
                time.sleep(2)
                clear_lines(4)
                continue
            elif not enter.isalpha():
                cprint("Word must only contain letters!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            elif enter == "help":
                enter = "".join(
                    list(random.choices(string.ascii_lowercase, k=len(word)))
                )
                clear_lines()
                print(
                    f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}", end=""
                )
                slow_type(enter, 1, color=LOG_DISCRET)
                time.sleep(0.5)
            elif len(enter) != len(word):
                cprint(f"Word must be {len(word)} letters long!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            clear_lines(2)
            break
        test_word()
        if good_answ >= len(word):
            affichage()
            clear_lines(2)
            print(f"{SUCCESS}{esp}{' '.join(list(word))}{RESET}", end="\n")
            cprint(f"Congratulations! You found the word: {word}", SUCCESS)
            choice = input("New game?:  ")
            if choice in continuer:
                word_guess_game()
            return
        elif guesses >= max_guesses:
            affichage()
            clear_lines()
            cprint(f"Sorry but you lost!\n{VERT_FLASH}The word was {word}", ERROR)
            choice = input("New game?:  ")
            if choice in continuer:
                word_guess_game()
            return


def dice(n_faces=6, n=1):
    """simule n lances de dés à n_faces faces"""
    simulation, total = 0, 0
    for i in range(n):
        simulation = random.randint(1, n_faces)
        slow_type(f"{i+1} -> {simulation}\n", 0.20)
        total += simulation
    print("\n")
    slow_type(f"total = {total}", 0.05)
    input("")
    return total


def tictactoe_game():
    def game_style_selection():
        choix = menu_options(
            [
                "1. Solo (Joueur contre IA)",
                "2. Multi (Joueur contre Joueur)",
                "3. IA vs IA",
            ]
        )
        while True:
            if choix == "1. Solo (Joueur contre IA)":
                return "solo"
            elif choix == "2. Multi (Joueur contre Joueur)":
                return "multi"
            elif choix == "3. IA vs IA":
                return "ia"

    tictactoe_game_style = game_style_selection()

    def launch_tic_tac_toe(game_style="solo"):
        faire_titre_section("TicTacToe Game!")
        time.sleep(0.3)
        clear()

        vars = {"grille": [[" " for _ in range(3)] for _ in range(3)], "tour": 0}

        def afficher_grille():
            for i in range(3):
                for j in range(3):
                    if j == 2:
                        print(vars["grille"][i][j], end="  ")
                    else:
                        print(vars["grille"][i][j], end=" | ")
                print()

        def verifier_victoire(symbole):
            # Vérifie les lignes
            for ligne in vars["grille"]:
                if all(cell == symbole for cell in ligne):
                    return True

            # Vérifie les colonnes
            for col in range(3):
                if all(vars["grille"][row][col] == symbole for row in range(3)):
                    return True

            # Vérifie les diagonales
            if all(vars["grille"][i][i] == symbole for i in range(3)) or all(
                vars["grille"][i][2 - i] == symbole for i in range(3)
            ):
                return True

            return False

        def est_grille_pleine():
            return all(cell != " " for ligne in vars["grille"] for cell in ligne)

        def coup_joueur():
            while True:
                try:
                    pos = input("Entrez votre coup (1-9): ")
                    num = int(pos)
                    if num < 1 or num > 9:
                        cprint("Veuillez entrer un nombre entre 1 et 9.", color=ERROR)
                        time.sleep(0.34)
                        clear_lines()
                        continue
                    ligne = (num - 1) // 3
                    col = (num - 1) % 3
                    if vars["grille"][ligne][col] != " ":
                        cprint("Cette case est déjà occupée!", color=ERROR)
                        time.sleep(0.34)
                        clear_lines()
                        continue
                    if game_style == "multi":
                        symbole = (
                            f"{ROUGE}X{RESET}"
                            if vars["tour"] % 2 == 0
                            else f"{BLEU}O{RESET}"
                        )
                        vars["grille"][ligne][col] = symbole
                    else:
                        vars["grille"][ligne][col] = f"{ROUGE}X{RESET}"
                    break
                except ValueError:
                    cprint("Entrée invalide!")
                    time.sleep(0.34)
                    clear_lines()

        def coup_ia():
            cases_libres = [
                (i, j)
                for i in range(3)
                for j in range(3)
                if vars["grille"][i][j] == " "
            ]
            symbole = f"{ROUGE}X{RESET}" if vars["tour"] % 2 == 0 else f"{BLEU}O{RESET}"
            adversaire = (
                f"{BLEU}O{RESET}"
                if symbole == f"{ROUGE}X{RESET}"
                else f"{ROUGE}X{RESET}"
            )

            def trouver_coup_gagnant(symbole_recherche):
                for ligne, col in cases_libres:
                    vars["grille"][ligne][col] = symbole_recherche
                    gagne = verifier_victoire(symbole_recherche)
                    vars["grille"][ligne][col] = " "
                    if gagne:
                        return ligne, col
                return None

            if cases_libres and len(cases_libres) < 7:
                # Priorité à l'attaque : si l'IA peut gagner immédiatement, elle joue cette case.
                coup_attaque = trouver_coup_gagnant(symbole)
                if coup_attaque:
                    ligne, col = coup_attaque
                    vars["grille"][ligne][col] = symbole
                    slow_type("L'IA joue pour gagner!\n", color=WARNING)
                    return

                # Défense : si l'adversaire peut gagner au prochain tour, bloquer.
                coup_defense = trouver_coup_gagnant(adversaire)
                if coup_defense:
                    ligne, col = coup_defense
                    vars["grille"][ligne][col] = symbole
                    slow_type("L'IA bloque votre mouvement!\n", color=WARNING)
                    return

                slow_type("L'IA réfléchit...\n", color=WARNING)
                time.sleep(0.3)
                cases_vip, cases_centre = [(0, 0), (0, 2), (2, 0), (2, 2)], [
                    (1, 1)
                ]  # Coins and centre
                # Priorité aux cases vips, puis au centre, sinon choix aléatoire
                for ligne, col in cases_vip:
                    if vars["grille"][ligne][col] == " ":
                        vars["grille"][ligne][col] = symbole
                        return
                for ligne, col in cases_centre:
                    if vars["grille"][ligne][col] == " ":
                        vars["grille"][ligne][col] = symbole
                        return

            ligne, col = random.choice(cases_libres)
            vars["grille"][ligne][col] = symbole

        slow_type("Bienvenue dans le jeu TicTacToe!\n", color=WARNING, tps_total=1)
        while (
            not verifier_victoire(f"{ROUGE}X{RESET}")
            and not verifier_victoire(f"{BLEU}O{RESET}")
            and not est_grille_pleine()
        ):
            afficher_grille()
            if game_style == "solo":
                if vars["tour"] % 2 == 0:
                    coup_joueur()
                else:
                    coup_ia()
            elif game_style == "multi":
                coup_joueur()
            elif game_style == "ia":
                coup_ia()
                time.sleep(0.7)
            vars["tour"] += 1
            time.sleep(0.5)
            clear()
        afficher_grille()
        if game_style == "multi":
            if verifier_victoire(f"{ROUGE}X{RESET}"):
                slow_type("Le joueur 1 (X) a gagné! 🎉\n", color=WARNING)
            elif verifier_victoire(f"{BLEU}O{RESET}"):
                slow_type("Le joueur 2 (O) a gagné! 🎉\n", color=WARNING)
            else:
                slow_type("Match nul!\n", color=WARNING)

        elif game_style == "solo":
            if verifier_victoire(f"{ROUGE}X{RESET}"):
                slow_type("Vous avez gagné! 🎉\n", color=WARNING)
            elif verifier_victoire(f"{BLEU}O{RESET}"):
                slow_type("L'IA a gagné! 🎉\n", color=WARNING)
            else:
                slow_type("Match nul!\n", color=WARNING)

        else:  # game_style == 'ia'
            if verifier_victoire(f"{ROUGE}X{RESET}"):
                slow_type("L'IA 1 (X) a gagné! 🎉\n", color=WARNING)
            elif verifier_victoire(f"{BLEU}O{RESET}"):
                slow_type("L'IA 2 (O) a gagné! 🎉\n", color=WARNING)
            else:
                slow_type("Match nul!\n", color=WARNING)

        continue_choice = menu_options(["1. Rejouer", "2. Quitter"])
        if continue_choice == "1. Rejouer":
            mode_change = menu_options(["1. Garder le mode", "2. Le changer"])
            if mode_change == "1. Garder le mode":
                launch_tic_tac_toe(game_style)
            else:
                tictactoe_game_style = game_style_selection()
                launch_tic_tac_toe(game_style=tictactoe_game_style)
        else:
            slow_type("Merci d'avoir joué! À bientôt!\n", color=WARNING)
            time.sleep(0.67)
            clear()

    launch_tic_tac_toe(game_style=tictactoe_game_style)


def Red_or_Black_game(mode="normal", cheat=True):
    """mode normal, +50, easy or hard"""
    global deck_of_cards
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

    if mode in {"+50", "easy"}:
        config["sold"] *= 1.5

    def save_high_score(win_serie_score, sold_score):
        config["sold"] = 200
        if win_serie_score > config["highest_win_serie_R/B"]:
            config["highest_win_serie_R/B"] = win_serie_score
            save_config(config)
        if sold_score > config["highest_sold_R/B"]:
            config["highest_sold_R/B"] = sold_score
            save_config(config)

    def game(current_tour=1):
        nonlocal stats, color, card, mise, prediction, last_mise, last_prediction, tour, cheat_use
        random.shuffle(deck_of_cards)
        card = deck_of_cards.pop()
        historique.append(card)
        if not deck_of_cards:
            return
        stats = {
            "Rouge": (
                len(
                    list(
                        filter(
                            lambda x: True if "♥" in x or "♦" in x else False,
                            deck_of_cards,
                        )
                    )
                )
                * 100
            )
            / len(deck_of_cards),
            "Noir": (
                len(
                    list(
                        filter(
                            lambda x: True if "♣" in x or "♠" in x else False,
                            deck_of_cards,
                        )
                    )
                )
                * 100
            )
            / len(deck_of_cards),
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
                    input()
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
                elif cheat and ("change" in mise):
                    cheat_use += 1
                    tour += 1
                    deck_of_cards.append(card)
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
                elif cheat and ("cheat -" in mise):
                    mise = mise.replace('cheat -', '').strip()
                    if not mise.isdigit():
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    if int(mise) <= 0:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    cheat_use -= int(mise)
                    cprint(f'cheat_use = {cheat_use} now!', WARNING)
                    time.sleep(0.67)
                    clear_lines(2)
                    continue
                elif cheat and ("cheat =" in mise):
                    mise = mise.replace('cheat =', '').replace('ch', '').strip()
                    if not mise.isdigit():
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    if int(mise) <= 0:
                        cprint("incorrect", ERROR)
                        time.sleep(0.3)
                        clear_lines(2)
                        continue
                    cheat_use = int(mise)
                    cprint(f'cheat_use = {cheat_use} now!', WARNING)
                    time.sleep(0.67)
                    clear_lines(2)
                    continue


                elif "all" in mise and "-" in mise:
                    mise = mise.replace("all", "").replace("-", "").strip()
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
        if not deck_of_cards:
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
                random_card = random.choice(deck_of_cards)
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
        if tour >= 2 and not animation == "fast":
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

            clear_lines(5)
            print(f"{'-' * 46}\n")
        mise = 0
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
        Win_rate = (100 / (Wins + Losses) * Wins) if (Wins + Losses) else 0
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
            if cheat_use < 0:
                print(arc_en_ciel('USSOTSKI!', 'ansi'))
                time.sleep(0.4)
                shutdown(kill=True)
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

    while config["sold"] > 10 and deck_of_cards:
        game(tour)
        if mise in exit:
            return
        affichage()
        tour += 1
    journal_transactions()
    save_high_score(highest_score, highest_sold)


def roulette_game(animationn=True, cheat=True):
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
    BET_PAYOUTS = {
        "num_simple": 35,
        "num_split_n2": 17,
        "num_street": 11,
        "num_corner": 8,
        "num_sixain": 5,
        "num_douzaine": 2,
        "num_colonne": 2,
        "red_black": 1,
        "pair_impair": 1,
    }
    numero = random.choice(ROULETTE_EUROPEENNE)
    couleur = COULEURS_ROULETTE[numero]
    compte, mise, prediction, pari_type, iswon, montant_gain, last_mise = (
        0,
        "",
        "",
        None,
        False,
        0,
        0,
    )

    def roulette_animation(resultat, animation=True):
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
        if animation:
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

    def affichage(animation=True):
        nonlocal mise, prediction, pari_type, numero, iswon, montant_gain
        iswon = False
        clear()
        print(f"+{'-' * 80}+\n")
        print(f"{' ' * 33}ROULETTE GAME\n")
        roulette_animation(numero, animation)
        print("\n")
        payout = BET_PAYOUTS.get(pari_type, 1)

        if pari_type in ["red_black", "pair_impair", "manque_passe"]:
            iswon = (
                (COULEURS_ROULETTE[numero] == prediction)
                or (("PAIR" if numero % 2 == 0 else "IMPAIR") == prediction)
                or (("SUP A 18" if numero >= 18 else "INF A 18") == prediction)
            )
        elif isinstance(prediction, list):
            iswon = numero in prediction
        else:
            iswon = numero == prediction

        if iswon:
            montant_gain = mise * payout
            config["sold"] += montant_gain
        else:
            config["sold"] -= mise
        if iswon:
            cprint(
                f"You predicted [ {LOG_DISCRET}{prediction}{RESET} ] and §you Won!!",
                SUCCESS,
            )
            cprint(f"You won €{format_number(montant_gain)} !", VERT_FLASH)
        else:
            cprint(
                f"You predicted [ {LOG_DISCRET}{prediction}{RESET} ]  §(wrong...)!",
                ERROR,
            )
            cprint(f"You lost €{mise} !", ROUGE_FLASH)
        input()

    def num_simple():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "num_simple"
            faire_titre_section("Numéro simple", color="FOND_ROUGE")
            prediction = input("\nEnter your prediction (1-36):   ").strip().lower()
            if ("right" | "re" | "not" in prediction) and not cheat:
                continue
            elif prediction == "right" and cheat:
                if numero == 0:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                prediction = numero
                clear_lines()
                print(f"enter your prediction (n):  {prediction}")
            elif ("re" in prediction) and cheat:
                prediction = prediction.replace("re", "").strip()
                if not prediction.isdigit():
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                if (int(prediction) not in ROULETTE_EUROPEENNE) or int(prediction) == 0:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                numero, prediction = int(prediction), int(prediction)
            elif "not" in prediction:
                while True:
                    prediction = random.choice(ROULETTE_EUROPEENNE)
                    if prediction == numero:
                        continue
                    break
            elif prediction == "random":
                prediction = random.choice(ROULETTE_EUROPEENNE)
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

            if prediction == "right" and not cheat:
                continue
            elif prediction == "right" and cheat:
                prediction = []
                prediction.append(numero)
                if numero == ROULETTE_EUROPEENNE[len(ROULETTE_EUROPEENNE) - 1]:
                    prediction.append(ROULETTE_EUROPEENNE[0])
                else:
                    prediction.append(
                        int(
                            ROULETTE_EUROPEENNE[
                                (
                                    (ROULETTE_EUROPEENNE.index(int(numero)) + 1)
                                    % len(ROULETTE_EUROPEENNE)
                                )
                            ]
                        )
                    )
            elif prediction == "random":
                prediction = []
                prediction.append(random.choice(ROULETTE_EUROPEENNE))
                if prediction[0] == ROULETTE_EUROPEENNE[len(ROULETTE_EUROPEENNE) - 1]:
                    prediction.append(ROULETTE_EUROPEENNE[0])
                else:
                    prediction.append(
                        int(
                            ROULETTE_EUROPEENNE[
                                (ROULETTE_EUROPEENNE.index(int(prediction[0])) + 1)
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
            numero, pari_type, = random.choice(ROULETTE_EUROPEENNE), "num_street"

            faire_titre_section("Numéros Sreet", color="FOND_ROUGE")

            prediction = (
                input(
                    f"\nEnter your predictions (1-36) {SOULIGN2}(n1 +1 +2 (conséc)){RESET}:   "
                )
                .strip()
                .lower()
            )
            if ("re" in prediction or "right" in prediction )and not cheat:
                continue
            elif prediction == "right" and cheat:
                prediction = []
                prediction.extend([numero, (numero % 36) + 1, (numero + 1) % 36 + 1])
            elif ("re" in prediction) and cheat:
                prediction = prediction.replace("re", "").strip()
                if not prediction.isdigit():
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                if (int(prediction) not in ROULETTE_EUROPEENNE) or int(prediction) == 0:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                numero = int(prediction)
                prediction = []
                prediction.extend([numero, (numero % 36) + 1, (numero + 1) % 36 + 1])

            elif prediction == "random":
                prediction = []
                r = random.choice(ROULETTE_EUROPEENNE)
                prediction.extend([r, (r % 36) + 1, (r + 1) % 36 + 1])
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
                    int(prediction[1]) != int(prediction[0]) + 1
                    or int(prediction[2]) != int(prediction[0]) + 2
                ):
                    continue
            prediction = [int(x) for x in prediction]
            clear_lines()
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def num_corner():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "num_corner"
            faire_titre_section("Numéros Corner", color="FOND_ROUGE")

            prediction = (
                input(
                    f"\nEnter your predictions (1-36) {SOULIGN2}(n1 n2 n3 n4){RESET}:   "
                )
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                nums = list(set(ROULETTE_EUROPEENNE))
                random.shuffle(nums)
                if numero in nums:
                    nums.remove(numero)
                prediction = nums[:3] + [numero]
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                nums = list(set(ROULETTE_EUROPEENNE))
                random.shuffle(nums)
                prediction = nums[:4]
            else:
                prediction = prediction.split()
                if len(prediction) != 4 or len(set(prediction)) != 4:
                    continue
                if not all(x.isdigit() for x in prediction):
                    continue
                prediction = [int(x) for x in prediction]
                if any(x <= 0 or x > 36 for x in prediction):
                    continue
            prediction = [int(x) for x in prediction]
            random.shuffle(prediction)
            clear_lines()
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def num_sixain():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "num_sixain"
            faire_titre_section("Sixains", color="FOND_ROUGE")

            prediction = (
                input(
                    f"\nEnter your predictions (1-36) {SOULIGN2}(n1 n2 n3 n4 n5 n6){RESET}:   "
                )
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                nums = list(set(ROULETTE_EUROPEENNE))
                random.shuffle(nums)
                if numero in nums:
                    nums.remove(numero)
                prediction = nums[:5] + [numero]
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                nums = list(set(ROULETTE_EUROPEENNE))
                random.shuffle(nums)
                prediction = nums[:6]
            else:
                prediction = prediction.split()
                if len(prediction) != 6 or len(set(prediction)) != 6:
                    continue
                if not all(x.isdigit() for x in prediction):
                    continue
                prediction = [int(x) for x in prediction]
                if any(x <= 0 or x > 36 for x in prediction):
                    continue
            prediction = [int(x) for x in prediction]
            random.shuffle(prediction)
            clear_lines()
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def num_douzaine():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "num_douzaine"
            faire_titre_section("Douzaines", color="FOND_ROUGE")

            print(f"1.  1-12\n2.  13-24\n3.  25-36")
            prediction = str(
                input(f"\nEnter your predictions {SOULIGN2}(1, 2, 3){RESET}:   ")
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                prediction = (
                    list(range(1, 13))
                    if numero <= 12
                    else list(range(13, 25)) if numero <= 24 else list(range(25, 37))
                )
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                prediction = random.choice([1, 2, 3])
                prediction = (
                    list(range(1, 13))
                    if prediction == 1
                    else list(range(13, 25)) if prediction == 2 else list(range(25, 37))
                )
            else:
                if not prediction in ["1", "2", "3"]:
                    continue
                else:
                    if prediction == str(1):
                        prediction = list(range(1, 13))
                    if prediction == str(2):
                        prediction = list(range(13, 25))
                    if prediction == str(3):
                        prediction = list(range(25, 37))

            clear_lines()
            prediction = [int(x) for x in prediction]
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def num_colonne():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type, col1, col2, col3 = (
                random.choice(ROULETTE_EUROPEENNE),
                "num_colonne",
                [32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13],
                [36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20],
                [14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26],
            )
            faire_titre_section("Colonnes", color="FOND_ROUGE", largeur=84)

            compte = 0
            print("\n")
            for num in ROULETTE_EUROPEENNE:
                compte += 1
                if num == 0:
                    continue
                print(
                    f"{f'{'1.' if compte == 2 else '2.' if compte == 14 else '3.'}   ' if compte in [2, 14, 26] else ''}[ {match_color(COULEURS_ROULETTE[num])}{num}{RESET} ]",
                    end=" ",
                )
                if compte == 13 or compte == 25:
                    print("\n\n")

            prediction = str(
                input(f"\n\nEnter your prediction {SOULIGN2}(1, 2, 3){RESET}:   ")
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                prediction = (
                    col1 if numero in col1 else col2 if numero in col2 else col3
                )
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                prediction = random.choice([1, 2, 3])
                prediction = (
                    col1 if prediction == 1 else col2 if prediction == 2 else col3
                )
            else:
                if not prediction in ["1", "2", "3"]:
                    continue
                else:
                    if prediction == str(1):
                        prediction = col1
                    if prediction == str(2):
                        prediction = col2
                    if prediction == str(3):
                        prediction = col3

            clear_lines()
            prediction = [int(x) for x in prediction]
            print(f"Enter your prediction :   {formate_collections(prediction)}")

            break

    def red_black():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "red_black"
            faire_titre_section("Rouge et Noir", color="FOND_ROUGE", largeur=80)

            compte = 0
            print("\n")
            for num in ROULETTE_EUROPEENNE:
                compte += 1
                if num == 0:
                    continue
                print(
                    f"[ {match_color(COULEURS_ROULETTE[num])}{num}{RESET} ]",
                    end=" ",
                )
                if compte == 13 or compte == 25:
                    print("\n")

            prediction = str(
                input(f"\n\nEnter your prediction {SOULIGN2}(R/N){RESET}:   ")
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                prediction = COULEURS_ROULETTE[numero]
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                prediction = random.choice(["NOIR", "ROUGE"])
            else:
                if not str(prediction).lower() in ["r", "b", "red", "black"]:
                    continue
                else:
                    if prediction.lower() in [
                        "r",
                        "red",
                    ]:
                        prediction = "ROUGE"
                    else:
                        prediction = "NOIR"

            clear_lines()
            print(
                f"Enter your prediction :   {ROUGE if prediction == 'ROUGE' else NOIR}{prediction}{RESET}"
            )

            break

    def pair_impair():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "pair_impair"
            faire_titre_section("Pair et Impair", color="FOND_ROUGE")

            prediction = str(
                input(f"\nEnter your prediction {SOULIGN2}(P/I){RESET}:   ")
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                prediction = "PAIR" if numero % 2 == 0 else "IMPAIR"
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                prediction = random.choice(["IMPAIR", "PAIR"])
            else:
                if not prediction in ["pair", "impair", "p", "i"]:
                    continue
                else:
                    if prediction in ["pair", "p"]:
                        prediction = "PAIR"
                    else:
                        prediction = "IMPAIR"
            clear_lines()
            print(f"Enter your prediction :   {LOG_DISCRET}{prediction}{RESET}")

            break

    def manque_passe():
        while True:
            nonlocal numero, prediction, pari_type
            numero, pari_type = random.choice(ROULETTE_EUROPEENNE), "manque_passe"
            faire_titre_section("Manque et Passe", color="FOND_ROUGE")

            prediction = str(
                input(f"\nEnter your prediction {SOULIGN2}(+/-) de 18{RESET}:   ")
                .strip()
                .lower()
            )
            if prediction == "right" and cheat:
                prediction = "SUP A 18" if numero >= 18 else "INF A 18"
            elif prediction == "right" and not cheat:
                continue
            elif prediction == "random":
                prediction = random.choice(["SUP A 18", "INF A 18"])
            else:
                if not prediction in ["-", "+", "moins", "plus"]:
                    continue
                else:
                    if prediction in ["+", "plus"]:
                        prediction = "SUP A 18"
                    else:
                        prediction = "INF A 18"
            clear_lines()
            print(f"Enter your prediction :   {LOG_DISCRET}{prediction}{RESET}")

            break

    clear()
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
                num_corner()
            case "5. Sixain           (5:1)":
                num_sixain()
            case "6. Douzaine         (2:1)":
                num_douzaine()
            case "7. Colonne          (2:1)":
                num_colonne()
            case "8. Rouge / Noir     (1:1)":
                red_black()
            case "9. Pair / Impair    (1:1)":
                pair_impair()
            case "10. Manque / Passe  (1:1)":
                manque_passe()
            case "11. Exit":
                return

        while True: # mise
            mise = input(f"enter a mise (sold = {config['sold']}):  ").strip().lower()

            if cheat and ("sold" in mise and ("+" in mise or "*" in mise)):
                # cheat_use += 1
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
            elif cheat and ("inf" in mise or "full" in mise):
                # cheat_use += 1
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
        affichage(animationn)
    print(
        f"{ROUGE if config['sold'] <= 200 else VERT}You had €200 to the start and finished with {config['sold']}!{RESET}"
    )


def dice_gambling_game(animationn=True):
    global config
    proba = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    while config["sold"] > 10:
        clear()
        des = random.randint(1, 6) + random.randint(1, 6)
        # print(des)
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
            elif 'pair' in pari or 'impair' in pari:
                pari_type = 'pair_imp'
                pari = list(filter(lambda x: True if x % 2 == 0 else False, list(range(2, 13)))) if 'pair' in pari else list(filter(lambda x: True if x % 2 == 1 else False, list(range(2, 13))))
                pourc = (sum([proba[x] for x in pari]) * 100) / 36
            elif pari in exit:
                return
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

        if animationn:
            for i in range(37): # animation
                print(f"\r{' ' * len('Enter a mise:  ')}[ {random.randint(1, 6) + random.randint(1, 6)} ] ", end="", flush=True)
                time.sleep(0.02 + i * 0.008)
        print(f"\r{' ' * len('Enter a mise:  ')}[ {des} ] ", flush=True)
        jump()
        clear_lines()

        if (pari_type == "nombres" and (des in pari)) or (pari_type == "inf_sup" and (des in pari)) or (pari_type == 'pair_imp' and (des in pari)):
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


def menu_game():
    """Le menu des jeux organisé par catégories."""
    while True:
        categorie = menu_options(
            [
                "1. Jeux de Mots",
                "2. Classiques & Stratégie",
                "3. Hasard & Nombres",
                "4. Casino & Argent",
                "5. Exit",
            ],
            "Games Menu",
        )

        match categorie:
            case "1. Jeux de Mots":
                choix = menu_options(
                    [
                        "1. Pendu Game",
                        "2. Code Names Game",
                        "3. Word guessing Game",
                        "4. Retour",
                    ],
                    "Jeux de Mots Menu",
                )
                match choix:
                    case "1. Pendu Game":
                        mode = menu_options(
                            [
                                "1. Normal",
                                "2. Facile",
                                "3. Très Facile",
                                "4. Difficile",
                                "5. Debug",
                                "6. Exit",
                            ]
                        )
                        match mode:
                            case "1. Normal":
                                pendu_game("normal")
                            case "2. Facile":
                                pendu_game("facile")
                            case "3. Très Facile":
                                pendu_game("tr_facile")
                            case "4. Difficile":
                                pendu_game("difficile")
                            case "5. Debug":
                                pendu_game("debug")
                    case "2. Code Names Game":
                        code_names_game()
                    case "3. Word guessing Game":
                        word_guess_game()
            case "2. Classiques & Stratégie":
                choix = menu_options(
                    [
                        "1. Rock, Paper, Scissor Game",
                        "2. Tic Tac Toe Game",
                        "3. Retour",
                    ],
                    "Classiques & Stratégie Menu",
                )
                match choix:
                    case "1. Rock, Paper, Scissor Game":
                        paper_scissor_game()
                    case "2. Tic Tac Toe Game":
                        tictactoe_game()
            case "3. Hasard & Nombres":
                choix = menu_options(
                    [
                        "1. Number Guessing Game",
                        "2. Pile ou Face Game",
                        "3. Dice simulator Game",
                        "4. Retour",
                    ],
                    "Hasard & Nombres Menu",
                )
                match choix:
                    case "1. Number Guessing Game":
                        number_guess_game()
                    case "2. Pile ou Face Game":
                        pile_face_game()
                    case "3. Dice simulator Game":
                        face, dices = input("How many face (6 by def):    "), input(
                            "How many dice? (1 by def):    "
                        )
                        face, dices = int(face) if face else 6, (
                            int(dices) if dices else 1
                        )
                        dice(face, dices)
            case "4. Casino & Argent":
                choix = menu_options(
                    ["1. Red or Black game", "2. Roulette_game", "3. Dice gambling game", "4. Retour"], "Casino & Argent"
                )
                match choix:
                    case "1. Red or Black game":
                        while True:
                            parameter = menu_options(
                                [
                                    "1. Normal",
                                    "2. +50",
                                    "3. Easy",
                                    "4. Hard",
                                    "5. Exit",
                                ],
                                "Red or Black GAME",
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
                                    break

                            Red_or_Black_game(mode)
                    case "2. Roulette_game":
                        roulette_game()
                    case "3. Dice gambling game":
                        dice_gambling_game()
            case "5. Exit":
                return

if __name__ == "__main__":
    menu_game()
