from tools import *
import time, random


def menu_ANSI():
    def menu_styles_txt():
        while True:
            faire_titre_section(" Menu styles de texte")
            time.sleep(0.4)
            style_txt = menu_options(
                [
                    "1. Gras",
                    "2. Italic",
                    "3. Souligné",
                    "4. Surligné_blanc",
                    "5. Noir_Invisible",
                    "6. Barré",
                    "7. Exit",
                ]
            )
            match style_txt:
                case "1. Gras":
                    cprint("\nPrince-Elric 33!", GRAS)
                    input("")
                case "2. Italic":
                    cprint("\nPrince-Elric 33!", ITALIC)
                    input("")
                case "3. Souligné":
                    cprint("\nPrince-Elric 33!", SOULIGN2)
                    input("")
                case "4. Surligné_blanc":
                    cprint("\nPrince-Elric 33!", SURLIGN2_BLANC)
                    input("")
                case "5. Noir_Invisible":
                    cprint("\nPrince-Elric 33!", NOIR_INVISIBLE)
                    input("")
                case "6. Barré":
                    cprint("\nPrince-Elric 33!", BARR2)
                    input("")
                case "7. Exit":
                    return

    def menu_couleurs_classiques():
        while True:
            faire_titre_section("Menu Couleurs classiques")
            time.sleep(0.4)
            classic_color = menu_options(
                [
                    "1. GRIS",
                    "2. ROUGE",
                    "3. VERT",
                    "4. JAUNE",
                    "5. BLEU",
                    "6. ROSE",
                    "7. CYAN",
                    "8. Exit",
                ]
            )
            match classic_color:
                case "1. GRIS":
                    cprint("\nPrince-Elric 33!", GRIS)
                    input("")
                case "2. ROUGE":
                    cprint("\nPrince-Elric 33!", ROUGE)
                    input("")
                case "3. VERT":
                    cprint("\nPrince-Elric 33!", VERT)
                    input("")
                case "4. JAUNE":
                    cprint("\nPrince-Elric 33!", JAUNE)
                    input("")
                case "5. BLEU":
                    cprint("\nPrince-Elric 33!", BLEU)
                    input("")
                case "6. ROSE":
                    cprint("\nPrince-Elric 33!", ROSE)
                    input("")
                case "7. CYAN":
                    cprint("\nPrince-Elric 33!", CYAN)
                    input("")
                case "8. Exit":
                    return

    def menu_couleurs_intenses():
        while True:
            faire_titre_section("Menu Couleurs Haute Intensité")
            time.sleep(0.4)
            intense_color = menu_options(
                [
                    "1. ROUGE_FLASH",
                    "2. VERT_FLASH",
                    "3. JAUNE_FLASH",
                    "4. BLEU_FLASH",
                    "5. ROSE_FLASH",
                    "6. CYAN_FLASH",
                    "7. Exit",
                ]
            )
            match intense_color:
                case "1. ROUGE_FLASH":
                    cprint("\nPrince-Elric 33!", ROUGE_FLASH)
                    input("")
                case "2. VERT_FLASH":
                    cprint("\nPrince-Elric 33!", VERT_FLASH)
                    input("")
                case "3. JAUNE_FLASH":
                    cprint("\nPrince-Elric 33!", JAUNE_FLASH)
                    input("")
                case "4. BLEU_FLASH":
                    cprint("\nPrince-Elric 33!", BLEU_FLASH)
                    input("")
                case "5. ROSE_FLASH":
                    cprint("\nPrince-Elric 33!", ROSE_FLASH)
                    input("")
                case "6. CYAN_FLASH":
                    cprint("\nPrince-Elric 33!", CYAN_FLASH)
                    input("")
                case "7. Exit":
                    return

    def menu_color_fond():
        while True:
            faire_titre_section("Menu Couleurs de fonds")
            time.sleep(0.4)
            color_fond = menu_options(
                [
                    "1. FOND_NOIR",
                    "2. FOND_ROUGE",
                    "3. FOND_VERT",
                    "4. FOND_JAUNE",
                    "5. FOND_BLEU",
                    "6. FOND_ROSE",
                    "7. FOND_CYAN",
                    "8. FOND_GRIS",
                    "9. Exit",
                ]
            )
            match color_fond:
                case "1. FOND_NOIR":
                    cprint("\nPrince-Elric 33!", FOND_NOIR)
                    input("")
                case "2. FOND_ROUGE":
                    cprint("\nPrince-Elric 33!", FOND_ROUGE)
                    input("")
                case "3. FOND_VERT":
                    cprint("\nPrince-Elric 33!", FOND_VERT)
                    input("")
                case "4. FOND_JAUNE":
                    cprint("\nPrince-Elric 33!", FOND_JAUNE)
                    input("")
                case "5. FOND_BLEU":
                    cprint("\nPrince-Elric 33!", FOND_BLEU)
                    input("")
                case "6. FOND_ROSE":
                    cprint("\nPrince-Elric 33!", FOND_ROSE)
                    input("")
                case "7. FOND_CYAN":
                    cprint("\nPrince-Elric 33!", FOND_CYAN)
                    input("")
                case "8. FOND_GRIS":
                    cprint("\nPrince-Elric 33!", FOND_GRIS)
                    input("")
                case "9. Exit":
                    return

    def menu_styles_predef():
        while True:
            faire_titre_section("Menu Styles Prédéfinis")
            time.sleep(0.4)
            style_def = menu_options(
                [
                    "1. ERROR",
                    "2. WARNING",
                    "3. SUCCESS",
                    "4. STYLE_TITRE",
                    "5. MENU_ACTIF",
                    "6. LOG_DISCRET",
                    "7. ALERTE_CRITIQUE",
                    "8. Exit",
                ]
            )
            match style_def:
                case "1. ERROR":
                    cprint("\nPrince-Elric 33!", ERROR)
                    input("")
                case "2. WARNING":
                    cprint("\nPrince-Elric 33!", WARNING)
                    input("")
                case "3. SUCCESS":
                    cprint("\nPrince-Elric 33!", SUCCESS)
                    input("")
                case "4. STYLE_TITRE":
                    cprint("\nPrince-Elric 33!", STYLE_TITRE)
                    input("")
                case "5. MENU_ACTIF":
                    cprint("\nPrince-Elric 33!", MENU_ACTIF)
                    input("")
                case "6. LOG_DISCRET":
                    cprint("\nPrince-Elric 33!", LOG_DISCRET)
                    input("")
                case "7. ALERTE_CRITIQUE":
                    cprint("\nPrince-Elric 33!", ALERTE_CRITIQUE)
                    input("")
                case "8. Exit":
                    return

    while True:
        faire_titre_section("ANSI colors Menu!")
        time.sleep(0.4)
        color_ch = menu_options(
            [
                "1. Styles de texte",
                "2. Couleurs classiques",
                "3. Couleurs haute intensité",
                "4. Couleurs de fond",
                "5. Styles prédéfinis",
                "6. Exit",
            ]
        )
        match color_ch:
            case "1. Styles de texte":
                menu_styles_txt()
            case "2. Couleurs classiques":
                menu_couleurs_classiques()
            case "3. Couleurs haute intensité":
                menu_couleurs_intenses()
            case "4. Couleurs de fond":
                menu_color_fond()
            case "5. Styles prédéfinis":
                menu_styles_predef()
            case "6. Exit":
                return


def match_color(color):
    match color:
        case "BARR2":
            color = BARR2
        case "SURLIGN2_BLANC":
            color = SURLIGN2_BLANC
        case "GRAS":
            color = GRAS
        case "ITALIC":
            color = ITALIC
        case "SOULIGN2":
            color = SOULIGN2
        case "NOIR_INVISIBLE":
            color = NOIR_INVISIBLE
        case "RESET":
            color = RESET
        case "CYAN":
            color = CYAN
        case "ROSE":
            color = ROSE
        case "BLEU":
            color = BLEU
        case "JAUNE":
            color = JAUNE
        case "VERT":
            color = VERT
        case "GRIS":
            color = GRIS
        case "ROUGE":
            color = ROUGE
        case "CYAN_FLASH":
            color = CYAN_FLASH
        case "ROSE_FLASH":
            color = ROSE_FLASH
        case "BLEU_FLASH":
            color = BLEU_FLASH
        case "JAUNE_FLASH":
            color = JAUNE_FLASH
        case "VERT_FLASH":
            color = VERT_FLASH
        case "ROUGE_FLASH":
            color = ROUGE_FLASH
        case "FOND_GRIS":
            color = FOND_GRIS
        case "FOND_CYAN":
            color = FOND_CYAN
        case "FOND_ROSE":
            color = FOND_ROSE
        case "FOND_BLEU":
            color = FOND_BLEU
        case "FOND_JAUNE":
            color = FOND_JAUNE
        case "FOND_VERT":
            color = FOND_VERT
        case "FOND_ROUGE":
            color = FOND_ROUGE
        case "FOND_NOIR":
            color = FOND_NOIR
        case "ALERTE_CRITIQUE":
            color = ALERTE_CRITIQUE
        case "LOG_DISCRET":
            color = LOG_DISCRET
        case "MENU_ACTIF":
            color = MENU_ACTIF
        case "STYLE_TITRE":
            color = STYLE_TITRE
        case "SUCCESS":
            color = SUCCESS
        case "WARNING":
            color = WARNING
        case "ERROR":
            color = ERROR
    return color


def info(fonction: str):
    match fonction:
        case "clear()":
            clear()
            cprint("Nécessite OS", LOG_DISCRET)
            time.sleep(0.5)
            clear()
            slow_type(
                "La fonction clear() Nettoie le terminal\nEn effet, par exemple on affiche des choses puis...",
                tps_btw_letters=0.025,
            )
            input("")
            clear()
            slow_type(
                "Le tout est effacé du terminal et repart de zéro.\n",
                tps_btw_letters=0.025,
            )
            input("")

        case "cprint()":
            clear()
            slow_type(
                "La fonction cprint(texte, color)  affiche des textes dans le terminal avec une certaine couleur ANSI.\n",
                tps_btw_letters=0.025,
            )
            slow_type(
                "Vous pouvez consulter le menu des couleurs pour en savoir +\n",
                tps_btw_letters=0.025,
            )
            choix = input("Ouvrir le menu des Couleurs ANSI?:   ")
            if choix in continuer:
                menu_ANSI()
            while True:
                clear()
                color = input("Enter a color for the text:  ").strip()
                if color not in colors:
                    cprint("Invallid enter!", ERROR)
                    time.sleep(0.6)
                    continue
                color = match_color(color)
                texte = input("Enter a text, (if nothing -> Prince-Elric 33!)").strip()
                if not texte:
                    texte = "Prince-Elric 33!"
                cprint(texte, color)
                input("")
                return

        case "slow_type()":

            def color_change():
                color_chang = input("Change color (y/n)?:     ")
                if color_chang in continuer:
                    while color_chang not in colors:
                        color_chang = input("Which one?:  ")
                        if color_chang not in colors:
                            cprint("Incorrect input!", ERROR)
                            time.sleep(0.5)
                            clear_lines(2)
                    return color_chang
                return False

            clear()
            cprint("Nécessite TIME", LOG_DISCRET)
            time.sleep(0.5)
            clear()
            slow_type(
                "la fonction, slow_type(...)\n Elle est omniprésente ici, elle sert même tout simplement à afficher le texte ici présent.\nElle simule un effet de frappe caractère par caractère.",
                tps_btw_letters=0.03,
            )
            print("")
            input("")
            slow_type("Here how it works (8):   ", tps_btw_letters=0.03)
            input("")
            print("")
            print(
                f"{ROSE_FLASH}slow_type{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET},{RESET} {JAUNE}tps_total{RESET}{LOG_DISCRET}={RESET}{VERT}0{RESET}{LOG_DISCRET},{RESET} {JAUNE}tps_btw_letters{RESET}{LOG_DISCRET}={RESET}{VERT}0{RESET}{LOG_DISCRET},{RESET} {JAUNE}color{RESET}{LOG_DISCRET}={RESET}{BLEU}LOG_DISCRET{RESET}{LOG_DISCRET}){RESET}\n"
            )
            time.sleep(0.5)
            slow_type(
                "On entre d'abord le texte, puis selon ce qu'on veut soit un tps_total ou pour chaque lettre:\n Si c'est par lettre on applique une latence entre chaque caractères sinon on calcule le temps moyen de latence en fonction de la longueur du texte.\n",
                tps_btw_letters=0.035,
            )
            time.sleep(1)
            slow_type(
                "Par défaut la couleur est LOG_DISCRET mais elle peut totalement être redéfini\n",
                tps_btw_letters=0.03,
            )
            choix = input("Tu veux la faire marcher toi-même?:  ").strip().lower()
            if choix in continuer:
                texte = input(
                    "Enter the text, (if nothing -> Prince-Elric 33!):  "
                ).strip()
                if not texte:
                    texte = "Prince-Elric 33!"
                choix_tempo = menu_options(["tps_total", "tps_by_letter"])
                if choix_tempo == "tps_total":
                    tps_total = valid_input("float", phrase="enter a total time")
                    couleur = color_change()
                    if couleur:
                        couleur = match_color(couleur)
                        clear()
                        slow_type(texte, tps_total, color=couleur)
                        input("\n")
                        return
                    clear()
                    slow_type(texte, tps_total)
                    return
                else:
                    tps_par_letter = valid_input(
                        "float", phrase="enter the time between each letter"
                    )
                    couleur = color_change()
                    if couleur:
                        couleur = match_color(couleur)
                        clear()
                        slow_type(texte, tps_btw_letters=tps_par_letter, color=couleur)
                        input("\n")
                        return
                    slow_type(texte, tps_btw_letters=tps_par_letter)
                    input("\n")
                    return

        case "loading_bar()":
            clear()
            cprint("Nécessite TIME", LOG_DISCRET)
            time.sleep(0.5)
            clear()

            slow_type(
                "Show a loading_bar of n caract with the actual step on the coast and the pourcentage of chargement, le tout dans un temps donné.\n",
                tps_btw_letters=0.035,
            )
            slow_type("Here how it works (14):   \n", tps_btw_letters=0.035)
            input("")
            print(
                f"{ROSE_FLASH}loading_bar{RESET}{LOG_DISCRET}({RESET}{JAUNE}tps{RESET}{LOG_DISCRET},{RESET} {JAUNE}symbol{RESET}{LOG_DISCRET}={RESET}{BLEU}'#'{RESET}{LOG_DISCRET},{RESET} {JAUNE}lenght{RESET}{LOG_DISCRET}={RESET}{VERT}10{RESET}{LOG_DISCRET}){RESET}\n"
            )
            slow_type(
                'The tps is the total time of the bar.\nThe symbol ("#" by default) is used in the bar.\nAnd the lenght (10 by default) désigne le nombre de symboles de la barre.\n',
                tps_btw_letters=0.035,
            )
            input("")
            slow_type("Exemple:\n", tps_btw_letters=0.035)
            loading_bar(2)
            choix = input("You want to make your own?:  ").strip().lower()
            if choix in continuer:

                tps = valid_input(
                    "float",
                    f"{ROSE_FLASH}loading_bar{RESET}{LOG_DISCRET}({RESET}{JAUNE}tps{RESET}{LOG_DISCRET}={RESET}{VERT}",
                    info=True,
                )
                symbol = str(
                    input(
                        f"{ROSE_FLASH}loading_bar{RESET}{LOG_DISCRET}({RESET}{JAUNE}tps{RESET}{LOG_DISCRET}={RESET}{VERT}{tps}{RESET}{LOG_DISCRET}, {RESET}{JAUNE}symbol{RESET}{LOG_DISCRET}={RESET}{BLEU}"
                    )
                )
                if not symbol:
                    symbol = "#"
                lenght = valid_input(
                    phrase=f"{ROSE_FLASH}loading_bar{RESET}{LOG_DISCRET}({RESET}{JAUNE}tps{RESET}{LOG_DISCRET}={RESET}{VERT}{tps}{RESET}{LOG_DISCRET}, {RESET}{JAUNE}symbol{RESET}{LOG_DISCRET}={RESET}{BLEU}'{symbol}'{RESET}{LOG_DISCRET}, {RESET}{JAUNE}lenght{RESET}{LOG_DISCRET}={RESET}{VERT}",
                    info=True,
                )
                if not lenght:
                    lenght = 10
                slow_type("Here your build\n", tps_btw_letters=0.035)
                print(
                    f"{ROSE_FLASH}loading_bar{RESET}{LOG_DISCRET}({RESET}{JAUNE}{tps}{RESET}{LOG_DISCRET},{RESET} {JAUNE}{symbol}{RESET}{LOG_DISCRET},{RESET} {JAUNE}{lenght}{RESET}{LOG_DISCRET}){RESET}\n"
                )
                input("")
                loading_bar(tps, symbol, lenght)
                input("")
                return
            return

        case "clear_lines()":
            clear()
            cprint("Nécessite SYS, RANDOM", LOG_DISCRET)
            time.sleep(0.5)
            clear()
            slow_type(
                "La fonction clear_lines(...) permet comme la fonction clear() de supprimer des lignes du terminal.\nCependant ici c'est un nombre donné des lignes et pas tout le terminal.\n",
                tps_btw_letters=0.035,
            )
            slow_type("Here how it works (3):\n")
            input("")
            print(
                f"{ROSE_FLASH}clear_lines{RESET}{LOG_DISCRET}({RESET}{JAUNE}n{RESET}{LOG_DISCRET}={RESET}{VERT}4{RESET}{LOG_DISCRET}){RESET}\n"
            )
            slow_type(
                "The parameter n (1 by default) désigne le nb de lignes à suppr.\n",
                tps_btw_letters=0.035,
            )
            print("")
            slow_type("Exemple:\n", 0.5)
            input("")
            clear()
            for _ in range(10):
                print(random_password(25), end="\n")
            print("")
            n = valid_input(
                info=True,
                phrase=f"{ROSE_FLASH}clear_lines{RESET}{LOG_DISCRET}({RESET}{JAUNE}n{RESET}{LOG_DISCRET}={RESET}{VERT}",
            )
            clear_lines(n + 2)
            input("")

        case "faire_titre_section()":
            clear()
            cprint("Nécessite RIEN", LOG_DISCRET)
            time.sleep(0.5)
            clear()
            slow_type(
                "La fonction faire_titre_section(...)  fait une ligne de symbols et centre le texte avant de refaire une ligne de symbols de n longueur\n",
                tps_btw_letters=0.035,
            )
            slow_type("Here how it works (5):\n", tps_btw_letters=0.035)
            input("")
            print(
                f"{ROSE_FLASH}faire_titre_section{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET},{RESET} {JAUNE}symbole{RESET}{LOG_DISCRET}={RESET}{BLEU}'-'{RESET}{LOG_DISCRET},{RESET} {JAUNE}largeur{RESET}{LOG_DISCRET}={RESET}{VERT}60{RESET}{LOG_DISCRET}){RESET}\n"
            )
            slow_type(
                'The texte parameter is simply the text that will be written on the middle.\nThe symbole parameter ("-" by default) désigne what will be repeted on the line sur et dessous le texte.\nThe largeur parameter (60 by default) is the lenght of the line and on how much the text will be centred.\n',
                tps_btw_letters=0.035,
            )
            slow_type("Exemple:\n", 0.5)
            input("")
            faire_titre_section("Prince-Elric 33!")
            input("")
            clear()
            choix = input("Do you make to make your own? (y/n):  ").strip().lower()
            if choix in continuer:
                clear()
                text = (
                    input(
                        f"{ROSE_FLASH}faire_titre_section{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET}={RESET}{BLEU}"
                    )
                    .strip()
                    .lower()
                    .rstrip(")")
                )
                if not text:
                    text = "Prince-Elric 33!"
                symbole = (
                    input(
                        f"{ROSE_FLASH}faire_titre_section{RESET}{LOG_DISCRET}({RESET}{JAUNE}text{RESET}{LOG_DISCRET}={RESET}{BLEU}'{text}'{RESET}{LOG_DISCRET},{RESET} {JAUNE}symbole{RESET}{LOG_DISCRET}={RESET}{BLEU}"
                    )
                    .strip()
                    .lower()
                    .rstrip(")")
                )
                if not symbole:
                    symbole = "-"
                lenght = valid_input(
                    info=True,
                    phrase=f"{ROSE_FLASH}faire_titre_section{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET}={RESET}{BLEU}'{text}'{RESET}{LOG_DISCRET},{RESET} {JAUNE}symbole{RESET}{LOG_DISCRET}={RESET}{BLEU}'{symbole}'{RESET}{LOG_DISCRET},{RESET} {JAUNE}largeur{RESET}{LOG_DISCRET}={RESET}{VERT}",
                )
                if not lenght:
                    lenght = 60
                clear()
                slow_type("Here your build:\n", tps_btw_letters=0.027)
                print(
                    f"{ROSE_FLASH}faire_titre_section{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET}={RESET}{BLEU}'{text}'{RESET}{LOG_DISCRET},{RESET} {JAUNE}symbole{RESET}{LOG_DISCRET}={RESET}{BLEU}'{symbole}'{RESET}{LOG_DISCRET},{RESET} {JAUNE}largeur{RESET}{LOG_DISCRET}={RESET}{VERT}{lenght}{RESET}{LOG_DISCRET}){RESET}\n"
                )
                input("")
                faire_titre_section(text, symbole, lenght)
                print("")
                input("")
            return

        case "menu_options()":
            clear()
            cprint("Nécessite MSVCRT", LOG_DISCRET)
            time.sleep(0.5)
            clear()

            slow_type(
                "The menu_options(...) is used tens times in this code to create a real architecture of the code.\nWith this focntion we can easely navigate into diff section and make choice very visuals.\n",
                tps_btw_letters=0.03,
            )
            slow_type("Here how it works (25):  \n")
            input("")
            print(
                f"{ROSE_FLASH}menu_options{RESET}{LOG_DISCRET}({RESET}{JAUNE}options{RESET}{LOG_DISCRET}){RESET}\n"
            )
            slow_type(
                "The options parameter is a list of every disponibles options\n",
                tps_btw_letters=0.03,
            )
            choix = input("Do you want to make your own? (y/n):     ").strip().lower()
            if choix in continuer:
                options = []
                while True:
                    opt = (
                        input(
                            f'Add an option ({len(options)} already)("q" to quit):   '
                        )
                        .strip()
                        .lower()
                    )
                    if opt in exit:
                        break
                    options.append(f"{len(options)+1}. {opt.capitalize()}")
                options.append(f"{len(options)+1}. Exit")
                menu_options(options)


        case "enlever_accents()":
            clear()
            cprint("Nécessite UNICODEDATA", LOG_DISCRET)
            time.sleep(0.5)
            clear()

            slow_type("The enlever_accents(...) fonction just make what she means, on an entered string she deletes the special things and return\n", tps_btw_letters=0.035)
            slow_type("Here how it works (5):   ")
            input('')
            print('')
            print(f"{ROSE_FLASH}enlever_accents{RESET}{LOG_DISCRET}({RESET}{JAUNE}texte{RESET}{LOG_DISCRET}){RESET}\n")
            stringg = input("Enter a texte with accents...    ")
            if not stringg:
                stringg = 'azerghbéfdhàùô'
                print(stringg)
            print(enlever_accents(stringg))
            input('')

        case "formate_collections()":
            pass
        case "fullmaj()":
            pass
        case "formate_number()":
            pass
        case "random_password()":
            pass
        case "random_username()":
            pass
        case "random_string()":
            pass
        case "abreviation()":
            pass
        case "seq()":
            pass

        case "copier_txt()":
            pass
        case "detect_shutdown()":
            pass
        case "shutdown_A()":
            pass
        case "hach_word()":
            pass
        case "shutdown()":
            pass
        case "start_timer()":
            pass
        case "stop_timer()":
            pass
        case "human_time()":
            pass
        case "valid_input()":
            pass

        case "ecrire_log()":
            pass
        case "log_info()":
            pass
        case "log_warning()":
            pass
        case "log_error":
            pass

        case "afk_mouse()":
            pass

        case "cesar_code()":
            pass
        case "brute_force()":
            pass
        case "morse()":
            pass
        case "fibonacci()":
            pass

        case "pendu_game()":
            pass
        case "papier_scissor_game()":
            pass
        case "number_guess_game()":
            pass
        case "code_names_game()":
            pass
        case "pile_face_game()":
            pass
        case "word_guess_game()":
            pass
        case "dice()":
            pass

        case "trouver_nom()":
            pass
        case "fonct_mots()":
            pass
        case "kaneki_count()":
            pass

        case _:
            cprint("Invallid enter", ERROR)
            input('')


def menu_principal():
    def menu_CONSTANTES():
        while True:
            faire_titre_section("CONSTANTES Menu!")
            time.sleep(0.4)
            constante = menu_options(["1. ANSI colors", "2. Listes", "3. Exit"])
            match constante:
                case "1. ANSI colors":
                    menu_ANSI()
                case "2. Listes":
                    print(f"\nContinue = {continuer}")
                    print(f"Exit     = {exit}")
                    input("")
                    menu_CONSTANTES()
                case "3. Exit":
                    return

    def DONN2ES():
        clear()
        loading_bar(0.67)
        filtred_6_min, words_10 = list(
            filter(lambda x: True if len(x) >= 6 else False, mots_921)
        ), list(random.choices(mots_921, k=10))
        slow_type(
            f"mots_921 is a list of french word which is composed of {len(mots_921)} words\n -> ({len(filtred_6_min)}) words of minimum 6 letters.",
            tps_btw_letters=0.030,
        )
        print("\n")
        slow_type(
            f"Here some exemple of words you can find in it: \n{formate_collections(words_10)}",
            tps_btw_letters=0.030,
        )
        print("\n")
        while True:
            enter = input("")
            if enter.lower().strip() in continuer:
                clear_lines(4)
                words_10 = list(random.choices(mots_921, k=10))
                slow_type(
                    f"Here some exemple of words you can find in it: \n{formate_collections(words_10)}",
                    tps_btw_letters=0.030,
                )
                print("\n")
                continue
            elif enter.lower().strip() == "re":
                DONN2ES()
            break

    def menu_fonct():

        def menu_terminal():
            while True:
                faire_titre_section(" Menu de Fonctions de terminal")
                time.sleep(0.5)
                fonct_term = menu_options(
                    [
                        "1. clear()",
                        "2. cprint(texte, color)",
                        "3. slow_type(texte, tps_total=0, tps_btw_letters=0, color=LOG_DISCRET)",
                        "4. loading_bar(tps, symbol='#', lenght=10)",
                        "5. clear_lines(n=1)",
                        "6. faire_titre_section(texte, symbole='-', largeur=60)",
                        "7. menu_options(options)",
                        "8. Exit",
                    ]
                )
                match fonct_term:
                    case "1. clear()":
                        info("clear()")
                    case "2. cprint(texte, color)":
                        info("cprint()")
                    case "3. slow_type(texte, tps_total=0, tps_btw_letters=0, color=LOG_DISCRET)":
                        info("slow_type()")
                    case "4. loading_bar(tps, symbol='#', lenght=10)":
                        info("loading_bar()")
                    case "5. clear_lines(n=1)":
                        info("clear_lines()")
                    case "6. faire_titre_section(texte, symbole='-', largeur=60)":
                        info("faire_titre_section()")
                    case "7. menu_options(options)":
                        info("menu_options()")
                    case "8. Exit":
                        return

        def menu_text():
            while True:
                faire_titre_section(" Menu de Fonctions de Text")
                time.sleep(0.5)
                fonct_text = menu_options(
                    [
                        "1. enlever_accents(texte: str)",
                        "2. formate_collections(*args)",
                        "3. fullmaj(txt)",
                        "4. format_number(n)",
                        "5. random_password(n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False)",
                        "6. random_username(n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True)",
                        "7. random_string(n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False)",
                        "8. abreviation(word='')",
                        "9. seq(txt='')",
                        "10. Exit",
                    ]
                )
                match fonct_text:
                    case "1. enlever_accents(texte: str)":
                        info("enlever_accents()")
                    case "2. formate_collections(*args)":
                        pass
                    case "3. fullmaj(txt)":
                        pass
                    case "4. format_number(n)":
                        pass
                    case "5. random_password(n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False)":
                        pass
                    case "6. random_username(n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True)":
                        pass
                    case "7. random_string(n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False)":
                        pass
                    case "8. abreviation(word='')":
                        pass
                    case "9. seq(txt='')":
                        pass
                    case "10. Exit":
                        return

        def menu_system():
            while True:
                faire_titre_section(" Menu de Fonctions de system")
                time.sleep(0.5)
                fonct_sys = menu_options(
                    [
                        "1. copier_txt(texte)",
                        "2. detect_shutdown()",
                        "3. shutdown_A()",
                        "4. hach_word(word)",
                        "5. shutdown(temps=40, kill=False)",
                        "6. start_timer(nom='default', entrées=False)",
                        "7. stop_timer(nom='default', entrées=False)",
                        "8. human_time(n)",
                        "9. valid_input(type='int', phrase='')",
                        "10. Exit",
                    ]
                )
                match fonct_sys:
                    case "1. copier_txt(texte)":
                        pass
                    case "2. detect_shutdown()":
                        pass
                    case "3. shutdown_A()":
                        pass
                    case "4. hach_word(word)":
                        pass
                    case "5. shutdown(temps=40, kill=False)":
                        pass
                    case "6. start_timer(nom='default', entrées=False)":
                        pass
                    case "7. stop_timer(nom='default', entrées=False)":
                        pass
                    case "8. human_time(n)":
                        pass
                    case "9. valid_input(type='int', phrase='')":
                        pass
                    case "10. Exit":
                        return

        def menu_journal():
            while True:
                faire_titre_section(" Menu de Fonctions de journalisation")
                time.sleep(0.5)
                fonct_journal = menu_options(
                    [
                        "1. ecrire_log(message, type_log='INFO', chemin)",
                        "2. log_info(message, type_log='INFO', chemin)",
                        "3. log_warning(message, type_log='WARNING', chemin)",
                        "4. log_error(message, type_log='ERROR', chemin)",
                        "5. Exit",
                    ]
                )
                match fonct_journal:
                    case "1. ecrire_log(message, type_log='INFO', chemin)":
                        pass
                    case "2. log_info(message, type_log='INFO', chemin)":
                        pass
                    case "3. log_warning(message, type_log='WARNING', chemin)":
                        pass
                    case "4. log_error(message, type_log='ERROR', chemin)":
                        pass
                    case "5. Exit":
                        return

        def menu_automat():
            while True:
                faire_titre_section(" Menu de Fonctions d'Automatisation")
                time.sleep(0.5)
                fonct_auto = menu_options(
                    [
                        "1. afk_mouse(n=0, kill=False)",
                        "2. Exit",
                    ]
                )
                match fonct_auto:
                    case "1. afk_mouse(n=0, kill=False)":
                        pass
                    case "2. Exit":
                        return

        def menu_crypto():
            while True:
                faire_titre_section(" Menu de Fonctions de Crypto")
                time.sleep(0.5)
                fonct_crypto = menu_options(
                    [
                        "1. cesar_code()",
                        "2. brute_force()",
                        "3. morse(txt='')",
                        "4. fibonacci()",
                        "5. Exit",
                    ]
                )
                match fonct_crypto:
                    case "1. cesar_code()":
                        pass
                    case "2. brute_force()":
                        pass
                    case "3. morse(txt='')":
                        pass
                    case "4. fibonacci()":
                        pass
                    case "5. Exit":
                        return

        def menu_specifik():
            while True:
                faire_titre_section(" Menu de Fonctions de Spécifiques")
                time.sleep(0.5)
                fonct_sys = menu_options(
                    [
                        "1. trouver_nom(objet)",
                        "2. fonct_mots()",
                        "3. kanekicount(number, base)",
                        "4. Exit",
                    ]
                )
                match fonct_sys:
                    case "1. trouver_nom(objet)":
                        pass
                    case "2. fonct_mots()":
                        pass
                    case "3. kanekicount(number, base)":
                        pass
                    case "4. Exit":
                        return

        while True:
            faire_titre_section("Sections de Fonctions disponibles")
            time.sleep(0.4)
            section = menu_options(
                [
                    "1. Terminal",
                    "2. Text",
                    "3. System",
                    "4. Journalisation (Logging)",
                    "5. Automatisation",
                    "6. Crypto",
                    "7. Jeux",
                    "8. Outils Spécifiques au Projet",
                    "9. Exit",
                ]
            )
            match section:
                case "1. Terminal":
                    menu_terminal()
                case "2. Text":
                    menu_text()
                case "3. System":
                    menu_system()
                case "4. Journalisation (Logging)":
                    menu_journal()
                case "5. Automatisation":
                    menu_automat()
                case "6. Crypto":
                    menu_crypto()
                case "7. Jeux":
                    menu_game()
                case "8. Outils Spécifiques au Projet":
                    menu_specifik()
                case "9. Exit":
                    return

    while True:
        principal = menu_options(
            ["1. Show CONSTANTES", "2. Show DONNÉES", "3. Show FONCTIONS", "4. Exit"]
        )
        match principal:
            case "1. Show CONSTANTES":
                menu_CONSTANTES()
            case "2. Show DONNÉES":
                DONN2ES()
            case "3. Show FONCTIONS":
                # menu le + imp avec les fonct
                menu_fonct()
            case "4. Exit":
                return


faire_titre_section("Tools Menu!")
time.sleep(0.4)
menu_principal()


# info("faire_titre_section()")
