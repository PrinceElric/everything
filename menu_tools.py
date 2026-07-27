from tools import *
import time


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

    while True:
        principal = menu_options(
            ["1. Show CONSTANTES", "2. Show DONNÉES", "3. Show FONCTIONS", "4. Exit"]
        )
        match principal:
            case "1. Show CONSTANTES":
                menu_CONSTANTES()
            case "2. Show DONNÉES":
                # menu de mots_921 avec des infos...
                pass
            case "3. Show FONCTIONS":
                # menu le + imp avec les fonct
                pass
            case "4. Exit":
                return


faire_titre_section("Tools Menu!")
time.sleep(0.4)
menu_principal()
