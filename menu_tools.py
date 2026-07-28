from tools import *
import time, random


def info(fonction: str):
    match fonction:
        case "clear()":
            pass
        case "cprint()":
            pass
        case "slow_type()":
            pass
        case "loading_bar()":
            pass
        case "clear_lines()":
            pass
        case "faire_titre_section()":
            pass
        case "menu_options()":
            pass
        
        case "enlever_accents()":
            pass
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
            cprint('Invallid enter', ERROR)


def menu_principal():
    def menu_CONSTANTES():
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
                        pass
                    case "2. cprint(texte, color)":
                        pass
                    case "3. slow_type(texte, tps_total=0, tps_btw_letters=0, color=LOG_DISCRET)":
                        pass
                    case "4. loading_bar(tps, symbol='#', lenght=10)":
                        pass
                    case "5. clear_lines(n=1)":
                        pass
                    case "6. faire_titre_section(texte, symbole='-', largeur=60)":
                        pass
                    case "7. menu_options(options)":
                        pass
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
                        "9. seq(txt='')" "10. Exit",
                    ]
                )
                match fonct_text:
                    case "1. enlever_accents(texte: str)":
                        pass
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
