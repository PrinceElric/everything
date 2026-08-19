"""
===============================================================================
                        DOCUMENTATION DU FICHIER TOOLS.PY
===============================================================================

Ce fichier regroupe un ensemble de fonctions utilitaires destinées à simplifier
le développement de scripts Python. Il fournit des outils pour l'affichage
dans le terminal, la génération de données, la manipulation de chaînes de
caractères, la journalisation, l'automatisation ainsi que diverses opérations
sur le système.

-------------------------------------------------------------------------------
1. DÉPENDANCES ET PRÉREQUIS
-------------------------------------------------------------------------------

Bibliothèques standards utilisées :
    - os
    - time
    - sys
    - subprocess
    - random
    - string
    - msvcrt
    - json
    - hashlib
    - unicodedata
    - itertools
    - datetime
    - mots_francais

Bibliothèque externe (optionnelle) :
    - pyautogui
      Utilisée uniquement pour les fonctions d'automatisation de la souris.

      Installation :
          pip install pyautogui

-------------------------------------------------------------------------------
2. INITIALISATION
-------------------------------------------------------------------------------

Au chargement du module :

    • Le fichier temporaire "tempo diary.md" est automatiquement réinitialisé.

Variables globales :

    • PATH_TEMP
        Chemin du fichier temporaire.

    • _timers
        Dictionnaire utilisé par les fonctions de chronométrage.

-------------------------------------------------------------------------------
3. CONSTANTES
-------------------------------------------------------------------------------

Le module fournit de nombreuses constantes ANSI permettant de personnaliser
l'affichage dans le terminal :

    • Styles de texte
        GRAS
        ITALIC
        SOULIGN2
        ...

    • Couleurs classiques
        ROUGE
        VERT
        JAUNE
        BLEU
        NOIR
        BLANC
        ...

    • Couleurs haute intensité
        ROUGE_FLASH
        VERT_FLASH
        JAUNE_FLASH
        BLEU_FLASH
        NOIR_FLASH
        BLANC_FLASH
        ...

    • Couleurs de fond
        FOND_ROUGE
        FOND_BLEU
        FOND_BLANC
        ...

    • Styles prédéfinis
        ERROR
        WARNING
        SUCCESS
        STYLE_TITRE
        MENU_ACTIF
        ALERTE_CRITIQUE


Le module propose également des listes pour sortir des input des programmes:

• Continuer

• Exit

• Others

• families
• values
• deck_of_cards

-------------------------------------------------------------------------------
4. DONNÉES
-------------------------------------------------------------------------------

mots_921

    Liste contenant aux alentours de 19000 mots français utilisée par certaines fonctions du
    module.

-------------------------------------------------------------------------------
5. FONCTIONS DISPONIBLES
-------------------------------------------------------------------------------

--- Terminal ---

• clear()
    Efface le terminal Windows.

• cprint(texte, color)
    Affiche un texte avec une couleur ANSI.

• slow_type(texte, tps_total=0, tps_btw_letters=0, color=LOG_DISCRET)
    Simule un effet de frappe caractère par caractère.

• loading_bar(tps, symbol="#", lenght=10)
    Affiche une barre de progression animée.

• clear_lines(n=1)
    Efface les dernières lignes du terminal.

• faire_titre_section(texte, symbole='-', largeur=60)
    Affiche un titre centré et décoré.

• menu_options(options)
    Affiche un menu interactif navigable au clavier.


-------------------------------------------------------------------------------

--- Text ---

• enlever_accents(texte: str)
    Supprime les accents d'une chaîne.

• formate_collections(*args)
    Améliore l'affichage des listes, tuples et ensembles.

• fullmaj(txt)
    Convertit un texte selon une table de correspondance personnalisée.

• format_number(n)
    Formate un nombre avec un séparateur de milliers.

• random_password(n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False)
    Génère un mot de passe aléatoire.

• random_username(n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True)
    Génère un nom d'utilisateur aléatoire.

• random_string(n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False)
    Génère une chaîne aléatoire personnalisable.

• abreviation(word="")
    return word abrevated, first letter + len + last letter

• seq(txt="")
    return the max continue chaine of a carac in txt

• arc_en_ciel(txt, mode="normal")
    Affiche un texte avec des couleurs aléatoires pour chaque caractère.


-------------------------------------------------------------------------------

--- System ---

• copier_txt(texte)
    Copie un texte dans le presse-papiers Windows.

• detect_shutdown()
    Annule plusieurs fois une extinction programmée.

• shutdown_A()
    Exécute "shutdown -a".

• hach_word(word)
    Retourne le hash SHA-256 d'une chaîne.

• shutdown(temps=40, kill=False)
    shutdown le PC avec multiples parfeux et eggs, pwrd, escape and just death

• start_timer(nom="default", entrées=False)
    Démarre un chronomètre.

• stop_timer(nom="default", entrées=False)
    Arrête un chronomètre et affiche le temps écoulé.

• human_time(n)
    Convertit des secondes en HHh:MMmin:SSs.

• valid_input(type="int", phrase="")
    Force une saisie valide du type demandé.


-------------------------------------------------------------------------------

--- Journalisation (Logging) ---

• ecrire_log(message, type_log, chemin_fichier)
    Écrit un message horodaté dans un fichier Markdown.

• log_info(...)
    Écrit un message de niveau INFO.

• log_warning(...)
    Écrit un message de niveau WARNING.

• log_error(...)
    Écrit un message de niveau ERROR.

-------------------------------------------------------------------------------

--- Automatisation ---

• afk_mouse(n, kill)
    Déplace automatiquement la souris et effectue des clics.

-------------------------------------------------------------------------------

--- Crypto ---

• cesar()
    Lance un menu interactif pour chiffrer et déchiffrer du texte avec le chiffre de César.

• brute_force(password='')
    Force un mot de passe en testant les longueurs au fur et à mesure.

• morse(txt='')
    Renvoi l'entrée en morse.


-------------------------------------------------------------------------------

--- Math ---

• factoriel(n: int) -> int
    Retourne le factoriel d'un nombre entier n.

• elements_communs(liste1: list, liste2: list) -> list
    Retourne la liste des éléments communs entre deux listes.

• fibonacci()
    Répète la sequ de fibonacci et offre des options de séléctions de données.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Jeux ---

• pendu_game(mode="normal")
    Lance le jeu du pendu.
• paper_scissor_game()
    Lance le jeu du papier-ciseaux avec capacité de triche.
• number_guess_game(minimum=0, maximum=100)
    Lance le jeu du nombre à deviner avec capa de triche.
• code_names_game()
    Lance le jeu du code names.
• pile_face_game(load=True)
    Just pile/face game! great animation and cheat capa->J
• word_guess_game(mode="nul", lenght_word_min=6, max_guesses=10)
    The word_guess_game were you input word and make color on letter -> /help
• dice(face=6, n=1)
    Simule n lances de dés à n_faces faces.
• Tictac_toe_game()
    Simule le jeu du morpion avec diff styles de jeux.
• Red_or_Black_game(mode="normal", cheat=True)
    red or black game of gambling
• Roulette_game(animationn=True, cheat=True)
    roulette game of gambling
• menu_game()
    Lance le menu de jeux.


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Outils Spécifiques au Projet ---

• trouver_nom(objet)
    Recherche le nom global associé à un objet.

• fonct_mots()
    Permet de rechercher et d'ajouter des mots à la liste mots_921.

• kanekicount(number, base)
    Soustrait une valeur de base jusqu'à atteindre zéro.

• def match_color(color):
    Renvoie la couleur ANSI correspondante à un nom donné.


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Executables ---

• clear()

• loading_bar(0.4, symbol="*", lenght=10, exe=True)

• start_timer()


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Divers ---

•
===============================================================================
"""

# -------------------------------------------------------------------------------
# 1. DÉPENDANCES ET PRÉREQUIS
# -------------------------------------------------------------------------------

import os, time, sys, subprocess, random, string, msvcrt, json, hashlib, unicodedata, itertools  # noqa: E401
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
try:
    from mots_francais import mots
except Exception:
    mots = []
    json_path = os.path.join(current_dir, "mots_francais.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, encoding="utf-8") as f:
                mots = json.load(f)
        except Exception:
            mots = []
try:
    import pyautogui as pag
except ImportError:
    pag = None  # Évite le plantage si absent


def load_config(chemin="config.json"):
    """Charge la configuration JSON en toute sécurité. Renvoie un dict vide si échec."""
    if not os.path.exists(chemin):
        return {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


config = load_config()


def save_config(data, chemin="config.json"):
    """Sauvegarde les données dans un fichier JSON. Renvoie un booléen de succès."""
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception:
        return False


# -------------------------------------------------------------------------------
# 2. INITIALISATION
# -------------------------------------------------------------------------------

# --- Réinitialisation automatique du fichier temporaire au démarrage ---
PATH_TEMP = r"C:\Users\elric\Desktop\vs code\all that\tempo diary.md"
try:
    with open(PATH_TEMP, "w", encoding="utf-8") as f:
        f.write("")  # On écrase avec du vide
except:  # Si le dossier existe pas encore, pas de crash  # noqa: E722
    pass

# -------------------------------------------------------------------------------
# 3. CONSTANTES
# -------------------------------------------------------------------------------

# --- Styles de texte ---
RESET = "\033[0m"
GRAS = "\033[1m"
ITALIC = "\033[3m"
SOULIGN2 = "\033[4m"
SURLIGN2_BLANC = "\033[7m"
NOIR_INVISIBLE = "\033[8m"
BARR2 = "\033[9m"

# --- Couleurs classiques ---
GRIS = "\033[2m"
ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU = "\033[34m"
NOIR = "\033[30m"
BLANC = "\033[37m"
ROSE = "\033[35m"
CYAN = "\033[36m"

# --- Couleurs Haute Intensité ---
ROUGE_FLASH = "\033[91m"
VERT_FLASH = "\033[92m"
JAUNE_FLASH = "\033[93m"
BLEU_FLASH = "\033[94m"
NOIR_FLASH = "\033[90m"
BLANC_FLASH = "\033[97m"
ROSE_FLASH = "\033[95m"
CYAN_FLASH = "\033[96m"

# --- Couleurs de Fond ---
FOND_NOIR = "\033[40m"
FOND_ROUGE = "\033[41m"
FOND_VERT = "\033[42m"
FOND_JAUNE = "\033[43m"
FOND_BLEU = "\033[44m"
FOND_ROSE = "\033[45m"
FOND_CYAN = "\033[46m"
FOND_GRIS = "\033[100m"  # Fond sombre discret
FOND_BLANC = "\033[107m"  # Fond blanc haute luminosité

# --- Super Fusions  ---
ERROR = ROUGE_FLASH + GRAS + SOULIGN2
WARNING = JAUNE_FLASH + ITALIC
SUCCESS = VERT_FLASH + GRAS
STYLE_TITRE = "\033[30m" + FOND_CYAN + GRAS  # Texte Noir sur Fond Cyan
MENU_ACTIF = "\033[97m" + FOND_BLEU + GRAS  # Texte Blanc sur Fond Bleu
LOG_DISCRET = GRIS + ITALIC  # Gris et penché
ALERTE_CRITIQUE = "\033[97m" + FOND_ROUGE + GRAS  # Texte Blanc sur Fond Rouge


continuer = ("continue", "c", "cont", "go", "next", "1", "y", "yes", "o", "oui")
exit = ("exit", "ex", "quitter", "quit", "q", "n", "no", "non")
others = ("other", "o", "autre")
colors = (
    "BARR2",
    "SURLIGN2_BLANC",
    "NOIR_INVISIBLE",
    "SOULIGN2",
    "ITALIC",
    "GRAS",
    "RESET",
    "CYAN",
    "ROSE",
    "BLEU",
    "JAUNE",
    "VERT",
    "GRIS",
    "ROUGE",
    "NOIR",
    "BLANC",
    "CYAN_FLASH",
    "ROSE_FLASH",
    "BLEU_FLASH",
    "JAUNE_FLASH",
    "VERT_FLASH",
    "ROUGE_FLASH",
    "NOIR_FLASH",
    "BLANC_FLASH",
    "FOND_GRIS",
    "FOND_CYAN",
    "FOND_ROSE",
    "FOND_BLEU",
    "FOND_JAUNE",
    "FOND_VERT",
    "FOND_ROUGE",
    "FOND_NOIR",
    "ALERTE_CRITIQUE",
    "LOG_DISCRET",
    "MENU_ACTIF",
    "STYLE_TITRE",
    "SUCCESS",
    "WARNING",
    "ERROR",
)

families = ("♣", "♠", "♦", "♥")
values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
deck_of_cards = [f"{value}{color}" for color in families for value in values]

# -------------------------------------------------------------------------------
# 4. DONNÉES
# -------------------------------------------------------------------------------

mots_921 = list(mots)


# -------------------------------------------------------------------------------
# 5. FONCTIONS DISPONIBLES
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

# --- Terminal ---


def clear():
    """Nettoie le terminal"""
    os.system("cls")


def cprint(texte, color):
    """Affiche texte coloré puis réinitialise style."""
    if "§" in texte and "!" in texte:  # balises de repère
        texte = texte.replace("§", color).replace("!", RESET, count=1)
        print(texte)
        return
    print(f"{color}{texte}{RESET}")


def slow_type(texte, tps_total=0, tps_btw_letters=0.03, color=LOG_DISCRET):
    """Print string character by character with tiny delay. and color if you want"""
    for letter in texte:
        if tps_total:
            temps_de_latence = tps_total / len(texte)
            time.sleep(float(temps_de_latence))
            print(f"{color}{letter}{RESET}", end="", flush=True)
        elif tps_btw_letters:
            time.sleep(float(tps_btw_letters))
            print(f"{color}{letter}{RESET}", end="", flush=True)


def loading_bar(tps, symbol="#", lenght=10, exe=False):
    """Barre de progression avec étapes X/Y et pourcentage exact."""
    pourc1 = 100 / lenght
    for i in range(1, lenght + 1):
        pourcentage = i * pourc1
        barre = symbol * i
        vide = "." * (lenght - i)

        clear_lines()
        cprint(f"[{barre}{vide}]    {i}/{lenght}  ({pourcentage:.1f}%)", LOG_DISCRET)
        time.sleep(tps / lenght)

    clear_lines()
    slow_type(
        f"[{symbol * lenght}]    {lenght}/{lenght} (100.0%)",
        tps_total=0.4,
        color=VERT_FLASH,
    )
    time.sleep(0.3)
    if exe:
        clear()
    else:
        clear_lines()


def clear_lines(n=1):
    """Efface un nombre de lignes donné dans le terminal."""
    for _ in range(n):
        sys.stdout.write("\033[1F\033[2K")
    sys.stdout.flush()


def faire_titre_section(texte, symbole="-", largeur=60, color="STYLE_TITRE"):
    """mettre texte et symbole, funct centre et fait une ligne de symbole de size largeur"""
    texte_grand = texte.upper()
    clear()
    print(symbole * largeur)
    print(f"{match_color(color)}{texte_grand.center(largeur)}{RESET}")
    print(symbole * largeur)


def menu_options(options, titre="=== MENU INTERACTIF ==="):
    """enter a list of options, show a interactif select menu, return the option chose"""
    index, taille = 0, len(options)

    while True:
        clear()
        if not "=" in titre:
            titre = f"=== {titre.upper()} ==="
        print(titre)
        # Afficher options
        for i in range(taille):
            if i == index:
                print(f"{MENU_ACTIF} > {options[i]} {RESET}")
            else:
                print(f"   {options[i]}")

        # Attendre touche
        touche: bytes = msvcrt.getch()

        # Si touche spéciale (comme les vraies flèches)
        if touche in (b"\x00", b"\xe0"):
            touche = msvcrt.getch()  # Lire deuxième code
            if touche == b"H":  # Flèche Haut
                index = (index - 1) % taille
            elif touche == b"P":  # Flèche Bas
                index = (index + 1) % taille
        elif touche == b"\r":  # Touche Entrée
            return options[index]


# -------------------------------------------------------------------------------


# --- Text ---
def enlever_accents(texte: str) -> str:
    """remove accents and things like that from the text and return"""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", texte)
        if unicodedata.category(c) != "Mn"
    )


def formate_collections(*args):
    """formate a collection into a str without the coast and komma-> ' '"""
    if isinstance(*args, list):
        return str(*args).replace("[", "").replace("]", "").replace("'", "")
    elif isinstance(*args, tuple):
        return str(*args).replace("(", "").replace(")", "").replace("'", "")
    elif isinstance(*args, set):
        return str(*args).replace("{", "").replace("}", "").replace("'", "")
    else:
        return str(*args).replace('"', '').replace("'", "")


def fullmaj(txt):
    """remake txt like the shift was turned on the other mode"""
    a = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + "1234567890"
        + "&é\"'(-è_çà)=^$ù*,;:!"
        + "°+¨£%µ?./§"
    )
    b = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + "&é\"'(-è_çà"
        + "1234567890°+¨£%µ?./§"
        + ")=^$ù*,;:!"
    )

    def MAJ(txt):
        texte_exit = ""
        for i in txt:
            if i == " ":
                texte_exit += " "
                continue
            c = a.index(i)
            d = b[c]
            texte_exit += d
        return texte_exit

    return MAJ(txt)


def format_number(n):
    """Formate un nombre en le sequencant en pattern de 3"""
    return f"{n:,}".replace(",", "'")


def random_password(
    n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False
):
    """make a password of size n with or without Maj, digit and punct°"""
    char, txt_password = string.ascii_lowercase, ""
    if Maj:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    if punctuation:
        char += string.punctuation
    if space:
        char += " "
    if tiret_bas:
        char += "_"
    while True:
        try:
            txt_password = "".join(random.choices(char, k=n))
            return txt_password
        except:  # noqa: E722
            pass


def random_username(
    n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True
):
    "" "based on the original random_password, chages the parameter to make a username valid''"
    return random_password(n, Maj, digits, punctuation, space, tiret_bas)


def random_string(
    n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False
):
    "" "based on the original random_password, chages the parameter to make a valid normal string''"
    return random_password(n, Maj, digits, punctuation, space, tiret_bas)


def abreviation(word=""):
    """return word abrevated, first letter + len + last letter"""
    if not word:
        word = str(input("Enter a word!:    ")).lower().strip()
    if not word.isalpha() and " " not in word:
        cprint("Invalid enter!", ERROR)
        abreviation()
    if len(word.split()) != len(word):
        texte = ""
        for i in word.split():
            texte += i[0] + str(len(i)) + i[len(i) - 1] + " "
        return texte
    if len(word) > 2:
        return word[0] + str(len(word)) + word[len(word) - 1]
    else:
        return word


def seq(txt=""):
    """return the max continue chaine of a carac in txt"""
    if not txt:
        txt = input()
    max_len = 1
    cur_len = 1

    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 1

    return max_len


def arc_en_ciel(txt, mode="normal"):
    """print txt with random color for each letter, mode can be normal, gras, italic, underline, surligne or ansi"""
    textee = []
    for i in txt:
        if i == " ":
            textee.append(" ")
            continue
        if mode == "normal":
            textee.append(f"\033[38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "gras":
            textee.append(f"\033[1;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "italic":
            textee.append(f"\033[3;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "underline":
            textee.append(f"\033[4;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "surligne":
            textee.append(f"\033[48;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "ansi":
            textee.append(f"{match_color(random.choice(colors))}{i}{RESET}")

    return "".join(textee)


def first(var):
    return var[0]

def last(var):
    return var[len(var) - 1]

# -------------------------------------------------------------------------------

# --- System ---


def copier_txt(texte):
    """copie texte dans presse-papier, subprocess"""
    subprocess.run(["clip"], input=texte, text=True, check=True)


def detect_shutdown():
    """shutdown -a two times with sleep of 0.4 btw the two"""
    for _ in range(2):
        os.system("shutdown -a")
        time.sleep(0.4)


def shutdown_A():
    """shutdown -a"""
    os.system("shutdown -a")


def hach_word(word):
    """genere the hach of a word and return a 64 carac string in hexadecimal"""
    return hashlib.sha256(word.encode()).hexdigest()


def shutdown(temps=40, kill=False):
    """Arrêt du PC avec protection par mot de passe et bien d'autres."""
    global config
    configuration = config.copy()

    if not configuration:
        configuration = {
            "password": "199e4be985e52e949b9628336ec91b740b03d6911c0096a5156370f118ea6405"
        }
    password_reel = configuration["password"]

    def launch_shutdown(temps):
        shutdown_A()
        clear()
        os.system(f"shutdown -s -t {temps}")

    def temps_stay():
        return timer - (time.time() - debut)

    def force_shutdown(timer=6, mode_normal=True, password=""):

        launch_shutdown(timer)
        print(f"{ALERTE_CRITIQUE}shutdown executed{RESET}")
        timer_final, cancelled = max(0, timer - 1.5), False
        if mode_normal:
            if password == "":
                shutdown()
        while timer_final >= 0:
            print(f"{ALERTE_CRITIQUE}\rtime left {timer_final:.2f}s{RESET}", end="")
            time.sleep(0.01)
            timer_final -= 0.01
            if mode_normal and timer_final < 1 and password == " ":
                print(f"{SUCCESS}\rtime left {timer_final:.2f}s{RESET}", end="")
                shutdown_A()
                cancelled = True
                break
        if not cancelled:
            for _ in range(10):
                os.system("start")
        elif mode_normal:
            cmd = subprocess.Popen(
                "cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            cmd.kill()
            try:
                number = int(
                    input(f"\n{SUCCESS}Which number to finish ?:{RESET}\n>>>  ")
                )
            except:  # noqa: E722
                print("GO TO HELL!")
                launch_shutdown(0)
            else:
                if number not in [3, 7]:
                    print("GO TO HELL!")
                    launch_shutdown(0)

    shutdown_A()
    clear()
    if kill:
        copier_txt('shutdown -a')
        force_shutdown(mode_normal=False)
        return

    print(f"{ALERTE_CRITIQUE}Attention, votre PC va s'éteindre dans 1 minute!{RESET}")
    time.sleep(0.5)

    timer = temps
    os.system(f"shutdown -s -t {timer}")
    print(f"{GRAS}shutdown executed{RESET}")
    debut = time.time()
    cmd = subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(0.7)
    cmd.kill()
    print(f"{WARNING}Arrêt planifié. {RESET}")
    hide_password = "*******160$"
    print(f"password is {hide_password}")
    password = input("what is the password ?\n").strip()

    if hach_word(password) == password_reel:
        shutdown_A()
        print(f"{SUCCESS}operation cancelled with {temps_stay():.3f}s left{RESET}")
    else:
        clear()
        print(f"{ERROR}WRONG PASSWORD{RESET}\n")

        now = temps_stay()
        t = now - 3
        while now >= t and now > 0:
            print(f"\r{ERROR}{now:.2f}s left{RESET}", end="")
            now -= 0.01
            time.sleep(0.01)

        clear()
        print(f"password is {hide_password}")
        password = input("\nOne more chance:  ")
        if password == " ":
            pass  # mot de passe spécial
        else:
            password = password.strip()
            if password:
                password = hach_word(password)

        if password == password_reel:
            shutdown_A()
            print(f"{SUCCESS}operation cancelled with {temps_stay():.2f}s left{RESET}")
        else:
            print(f"{ALERTE_CRITIQUE}WRONG AGAIN!!\nJUST GO TO HELL GUY!{RESET}")
            time.sleep(0.5)
            clear()

            force_shutdown(password=password)
            print("")
    cmd = subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(0.7)
    cmd.kill()
    clear()
    print(f"{SUCCESS}Arrêt annulé.{RESET}")
    detect_shutdown()
    clear()


# shutdown(kill=True)

_timers = {}


def start_timer(nom="default", entrees=False):
    """Démarre ou réinitialise un chrono avec un nom donné."""
    global _timers
    start = time.process_time() if not entrees else time.perf_counter()
    _timers[nom] = start


def stop_timer(nom="default", entrees=False):
    """Arrête chrono et affiche/renvoie le temps écoulé."""
    global _timers
    if nom not in _timers:
        print(f"{ERROR}Erreur : Chrono '{nom}' non démarré.{RESET}")
        return None

    fin = time.process_time() if not entrees else time.perf_counter()
    duree = fin - _timers[nom]
    # print(f"[{nom}] {duree:.6f} s")
    return duree


def human_time(seconds: float) -> str:
    """Convertit un temps en secondes vers un format lisible."""
    if seconds is None or seconds <= 0:
        return "0s"

    if seconds < 1:
        return f"{seconds * 1000:.2f} ms"

    units = [
        ("d", 86400),
        ("h", 3600),
        ("m", 60),
        ("s", 1),
    ]

    parts = []
    total_seconds = int(seconds)

    for unit, unit_seconds in units:
        if total_seconds >= unit_seconds:
            value = total_seconds // unit_seconds
            total_seconds %= unit_seconds
            parts.append(f"{value}{unit}")

    return " ".join(parts)


def valid_input(type="int", phrase="", info=False):
    """Demande une entrée d'un type précis et boucle tant que l'entrée est invalide."""
    if type == "str":
        phrase = phrase or "enter a string"
        return input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()

    elif type in ["int", "float"]:
        phrase = phrase or "enter a number"
        while True:
            if info:
                entree = input(f"{phrase}").strip().rstrip(")")
            else:
                entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()
            try:
                return int(entree) if type == "int" else float(entree)
            except ValueError:
                print(f"{ERROR}Incorrect enter, try again{RESET}")
                time.sleep(0.5)
                clear_lines(2)

    elif type == "bool":
        phrase = phrase or "enter True/Yes or False/No"
        if info:
            entree = input(f"{phrase}").strip().rstrip(")").lower()
        else:
            entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip().lower()
        return entree in continuer

    print(f"{ERROR}INCORRECT TYPE!!!{RESET}")
    return None


# -------------------------------------------------------------------------------

# --- Journalisation (Logging) ---


def ecrire_log(
    message,
    type_log="INFO",
    chemin_fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md",
):
    """Graver message avec date et étiquette [INFO/WARNING/ERROR]"""
    type_log = type_log.upper()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne_log = f"[{date_str}] [{type_log}] {message}\n"

    if (
        chemin_fichier in ["données", "donnée", "donnee", "donnees"]
        or chemin_fichier == r"C:\Users\elric\Desktop\vs code\all that\données.md"
    ):
        chemin_fichier = r"C:\Users\elric\Desktop\vs code\all that\données.md"
    elif chemin_fichier in ["temp", "tempo", "diary", "temporaire"]:
        chemin_fichier = r"C:\Users\elric\Desktop\vs code\all that\tempo diary.md"

    elif "\\" not in chemin_fichier and not chemin_fichier.endswith(".md"):
        print(f"{ERROR}Fichier name not valid : {chemin_fichier}{RESET}")
        return

    with open(chemin_fichier, "a", encoding="utf-8") as f:
        f.write(ligne_log)


def log_info(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "INFO", fichier)


def log_warning(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "WARNING", fichier)


def log_error(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "ERROR", fichier)


# -------------------------------------------------------------------------------

# --- Automatisation ---


def afk_mouse(n=0, kill=False):
    """move mouse randomly and click, forever or in range n (len or digit)"""
    pag.FAILSAFE = False

    def main():
        x = random.randint(0, 1920)
        y = random.randint(0, 1200)
        pag.moveTo(x, y, 0.5)
        time.sleep(0.5)
        pag.click()

    def kill_terminal():
        x, y = 1745, 666
        pag.moveTo(x, y, 0.5)
        time.sleep(0.5)
        pag.click()

    if not kill:
        if not n:
            while True:
                main()
        else:
            try:
                n = int(n)
            except:  # noqa: E722
                n = len(n)
            finally:
                for _ in range(n):
                    main()
    else:
        kill_terminal()


# -------------------------------------------------------------------------------

# --- Crypto ---


def cesar_code():
    """Encrypt a text with Cesar! Multiple options into"""
    letzte, sequ_of_possibl, alpha = "", {}, string.ascii_lowercase

    def math(txt, n, decrypt=True):
        nonlocal alpha
        text = ""
        for i in txt:
            if i in alpha:
                a = alpha.find(i)
                if decrypt:
                    a = (a - n) % len(alpha)
                else:
                    a = (a + n) % len(alpha)
                text += alpha[a]
            elif i.isascii() and i.lower() != i:
                i_lower = i.lower()
                a = alpha.find(i_lower)
                if decrypt:
                    a = (a - n) % len(alpha)
                else:
                    a = (a + n) % len(alpha)
                text += alpha[a].upper()
            elif i.isdigit():
                if decrypt:
                    a = (int(i) - n) % 10
                else:
                    a = (int(i) + n) % 10
                text += str(a)
            elif i == " ":
                text += " "
            else:
                text += i
        return text

    def encrypt():
        nonlocal letzte, alpha
        txt = input("enter a text to encrypt:  \n")
        n = int(
            input(
                "enter a key of encryption *NOTE! This is using the Ceaser cipher (or 0 to make it random)\n"
            )
        )
        if n == 0:
            n = random.randint(1, len(alpha) - 1)
        if txt == "":
            txt = "".join(random.choices(alpha, k=50))
        elif "last" in txt:
            txt = letzte
        apr = math(txt, n, decrypt=False)
        letzte = apr
        print(f"here the text : {txt} in Cesar with key of {n}:\n {apr}")

    def decrypt(txt):
        nonlocal letzte
        n = int(input("enter a key of decryption \n"))
        if "last" in txt:
            txt = letzte
        apr = math(txt, n, decrypt=True)
        letzte = apr
        print(f"the text :  {txt} decrypted in key {n} is : \n {apr}")

    def decrypt_without_key(txt, sign="elric"):
        nonlocal letzte, sequ_of_possibl
        if "last" in txt:
            txt = letzte
        for n in range(1, len(alpha) + 1):
            apr = math(txt, n, decrypt=True)
            if sign in apr:
                sequ_of_possibl[n] = apr
                letzte = apr
                break
        for cle, valeur in sequ_of_possibl.items():
            print(f"possible key :  {cle}")
            print(f"text would pass from {txt} to : {valeur}")

    while True:
        choice = menu_options(
            [
                "1. encrypt a text",
                "2. decrypt a text",
                "3. decrypt without key",
                "4. Exit",
            ]
        )
        match choice:
            case "1. encrypt a text":
                encrypt()
            case "2. decrypt a text":
                text = input("enter a text to decrypt: \n")
                decrypt(text)
            case "3. decrypt without key":
                text = input("enter a text to decrypt: \n")
                kff = input("enter the sign that you know is in this text:  \n")
                while kff == " ":
                    print("not valid sign !!")
                    kff = input(
                        "pls, enter the sign that you know is in this text:  \n"
                    )
                if kff != "":
                    decrypt_without_key(text, kff)
                else:
                    decrypt_without_key(text)
            case "4. Exit":
                cprint("thank you!", FOND_VERT)
                break
        input(">>>   ")
    input("")


def brute_force(password=""):
    """brutforce un pwrd"""

    def brute(target_password, max_length=6):
        # Les caractères possibles : lettres minuscules, majuscules et chiffres
        characters, attempts = (
            string.ascii_lowercase + string.ascii_uppercase + string.digits,
            0,
        )
        start_timer()

        for length in range(
            1, max_length + 1
        ):  # On teste toutes les longueurs de 1 jusqu'à max_length
            print(f"\nTest des combinaisons de longueur {length}...")

            for combo in itertools.product(characters, repeat=length):
                attempts += (
                    1  # itertools.product génère toutes les combinaisons possibles
                )
                guess = "".join(combo)

                if guess == target_password:
                    print(f"\nMot de passe trouvé : '{guess}'")
                    print(f"   Tentatives : {attempts:,}")
                    print(f"   Temps écoulé : {print(f'{stop_timer():.2f}')} secondes")
                    return guess
        print("Mot de passe non trouvé dans la limite fixée.")
        return None

    if not password:
        password = input("Entre un mot de passe court à deviner : ")

    brute(password, max_length=len(password))
    input("")


def morse(txt=""):
    """convert iterable to morse code"""
    if not txt:
        txt = input("enter a sequence to put in morse:\n>>>   ")
    words, morse = tuple(txt), ""
    char_to_dots = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": " ",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }

    def in_morse():
        nonlocal morse
        for abc in words:
            if abc.isalpha():
                abc = abc.upper()
                morse += char_to_dots[abc] + " "
            else:
                morse += char_to_dots[abc] + " "

    in_morse()
    print(f"text in morse :\n{morse}")
    input("")
    return morse


def A1Z26(direct: str = False, txtt="", choix=""):
    """Here the mythical encodage in A1_Z26 to in and out code.
    1. Encode to A1-Z26, 2. Decode from A1-Z26"""

    def in_A1Z26(*args):
        alphab, char = string.ascii_lowercase, ""
        for word in list(*args):
            for letter in word:
                letter = letter.lower()
                if letter not in alphab:
                    if not letter == word[-1]:
                        char += letter + "-"
                    else:
                        char += letter
                    continue
                ind = alphab.index(letter) + 1
                if not letter == word[-1]:
                    char += str(ind) + "-"
                else:
                    char += str(ind)
            char += "  "
        return char

    def out_A1Z26(*args):
        alphab = string.ascii_lowercase
        result_words = []
        for word in list(*args):
            tokens = word.split("-") if word else []
            decoded = ""
            for token in tokens:
                token = token.strip()
                if not token:
                    continue
                if token.isdigit():
                    n = int(token)
                    if 1 <= n <= 26:
                        decoded += alphab[n - 1]
                    else:
                        decoded += token
                else:
                    decoded += token
            result_words.append(decoded)
        return " ".join(result_words)

    if direct and direct == "in_A1Z26()":
        if not txtt:
            text = input("\nEnter the text to encode:  ").strip().split()
        else:
            text = txtt.strip().split()
        return in_A1Z26(text)
    elif direct and direct == "out_A1Z26()":
        if not txtt:
            text = input("\nEnter the text to decode:  ").strip().split("  ")
        else:
            text = txtt.strip().split()
        return out_A1Z26(text)

    if not choix:
        choix = menu_options(
            ["1. Encode to A1-Z26", "2. Decode from A1-Z26", "3. Exit"]
        )
    match choix:
        case "1. Encode to A1-Z26":
            if not txtt:
                text = input("\nEnter the text to encode:  ").strip().split()
            else:
                text = txtt.strip().split()
            return in_A1Z26(text)

        case "2. Decode from A1-Z26":
            if not txtt:
                text = input("\nEnter the text to decode:  ").strip().split("  ")
            else:
                text = txtt.strip().split("  ")

            return out_A1Z26(text)

        case "3. Exit":
            return


# -------------------------------------------------------------------------------

# --- Math ---


def factoriel(n: int) -> int:
    """Retourne le factoriel d'un nombre entier n."""
    import math

    return math.factorial(n)


def elements_communs(liste1: list, liste2: list) -> list:
    """Retourne la liste des éléments communs entre deux listes."""
    return list(set(liste1) & set(liste2))


def fibonacci():
    """Remake the fibonacci sequ and few data selections options"""

    def fibonacci_place(n):
        if n <= 0:
            return f"{ROUGE}the number must be greater than 0{RESET}"
        fib1, fib2, count = 1, 1, 2
        if n == 1:
            return f"the number is at the {VERT}1st or 2nd place{RESET}"
        while fib2 < n:
            fib1, fib2, count = fib2, fib1 + fib2, count + 1
        if fib2 == n:
            return f"the number is at the {VERT}{count}th place{RESET}"
        else:
            return f"{ROUGE}the number isn't in the Fibonacci sequence{RESET}"

    def fibonnacci_index_num(n):
        if n <= 0:
            return None
        fib1, fib2 = 1, 1
        if n == 1 or n == 2:
            return 1
        for _ in range(3, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

    while True:
        choice = menu_options(
            [
                "1. Find number in place n in the Fibonacci sequence",
                "2. Find if n is the sequence",
                "3. Quit",
            ]
        )
        if choice == "1. Find number in place n in the Fibonacci sequence":
            try:
                n = int(input("Enter a index of the Fibonacci sequence :\nPlace: "))
                result = fibonnacci_index_num(n)
                if result is None:
                    cprint("the index must be greater than 0!", ERROR)
                else:
                    print(
                        f"To the place {n} of the Fibonacci sequence there is the #"
                        f"{VERT}{format_number(result)}{RESET}"
                    )
            except ValueError:
                cprint("please enter a valid integer", ERROR)
            input("")
            clear()
        elif choice == "2. Find if n is the sequence":
            try:
                n = int(
                    input(
                        "Enter a number to check if he's in the sequence and at wich place:\nNumber to check:  "
                    )
                )
                print(fibonacci_place(n))
            except ValueError:
                cprint("please enter a valid integer", ERROR)
            input("")
            clear()
        elif choice == "3. Quit":
            return


# -------------------------------------------------------------------------------

# --- Jeux ---

def menu_game():
    """Le menu des jeux organisé par catégories."""
    from games import pendu_game, paper_scissor_game, number_guess_game, code_names_game, pile_face_game, word_guess_game, dice, tictactoe_game, Red_or_Black_game, roulette_game
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
                    ["1. Red or Black game", "2. Roulette_game", "3. Retour"], "Casino & Argent"
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
            case "5. Exit":
                return


# -------------------------------------------------------------------------------

# --- Outils du projet ---


def trouver_nom(objet):
    """return name of the given variable"""
    for nom, valeur in globals().items():
        if valeur is objet:
            return nom
    return None


# pas a jour du tout avec la new versions de mots_921 !!
def fonct_mots():
    """fonct for the var mots_921 which search if given name is into"""
    global mots_921
    nom = trouver_nom(mots_921)
    print(f"{nom} = {len(mots_921)}")
    if nom != "mots_" + str(len(mots_921)):
        print(f"{ERROR}Problem with the name of {nom}{RESET}")
    word = "science"
    while True:
        word = input("Enter a word:    ").lower()
        if word == "clear":
            clear()
            fonct_mots()
        elif word == "quit":
            sys.exit()
        if word in mots_921:
            print(f"{ERROR}{word} is present!{RESET}")
            continue
        else:
            print(f"{SUCCESS}{word} isn't present!{RESET}")
            accept_enter = input(f"do you want the word :  {word}, to be add?\n>>>  ")
            if accept_enter == "clear":
                clear()
                fonct_mots()
            elif accept_enter.lower() == "quit":
                sys.exit()
            if accept_enter:
                mots_921.append(word)
                mots_921 = sorted(mots_921)
                index_debut = mots_921.index(word) - 1
                index_fin = mots_921.index(word) + 2
                print(mots_921[index_debut:index_fin])
                a = str(mots_921[index_debut:index_fin])
                a = a.lstrip("[")
                a = a.rstrip("]")
                copier_txt(a)
                print(f"ligne: {65 +  index_debut // 10}")


def kanekicount(number, base):
    n = 0
    while number > base:
        number, n = number - base, n + 1
        print(f"{number}    {n}")


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
        case "NOIR_FLASH":
            color = NOIR_FLASH
        case "BLANC_FLASH":
            color = BLANC_FLASH
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
        case _:
            color = RESET
    return color


# -------------------------------------------------------------------------------

# --- Executables ---

clear()
loading_bar(0.33, symbol="*", lenght=10, exe=True)
start_timer()


# -------------------------------------------------------------------------------

# --- Divers ---

name, just_namee, a, b, password = "", "", 0, 0, ""

def name():
    global name, just_namee, a, b
    a, b, name = 0, 0, input("Enter your name: ")
    just_namee = name
    if "Elric" in name or "elric" in name:
        print("Admin is there")
        b = 1
    elif name:
        check_username(name)
    else:
        while name == "" or name == " ":
            name = input("Enter your name: ")
            a += 1
        check_username(name)
        just_namee = name
        if "Elric" in name or "elric" in name:
            print("Admin is there")
            b = 1
    if a >= 10:
        print(f"{a}, c'est bien trop, tu vas me recommencer tout ça")
        name()
    elif b == 1:
        print(f"Welcome to the game {name} sama the Master of the world")
    elif a >= 2:
        print(f"il t'en aura fallu du temps ({a})")
        print(f"Welcome to the game {name}")
    elif a == 1:
        print("enfin arrivé")
        print(f"que {a} essai, ça va")
        print(f"Welcome to the game {name}")
    else:
        print(f"Welcome to the game {name}")
    return name


def check_username(name):
    username = name
    if len(username) >= 12:
        cprint("username too long", ERROR)
        name()
    elif " " in username:
        cprint("username must not have spaces", ERROR)
        name()
    elif not username.isalpha():
        cprint("username must be alphabetical", ERROR)
        name()
    else:
        cprint("username ok", VERT_FLASH)


def fonction_password():
    global password
    password, verif = "", ""
    password = str(input("Enter your password: "))
    while password == "" or password == " ":
        password = str(input("Enter your password: "))
    if not 5 < len(password) < 15:
        print("password has a not valid length")
        fonction_password()
    if " " in password:
        print("password must not have spaces")
    else:
        verif = input(f"{just_namee}, enter a second time your password: ")
        while verif != password:
            print(f"{just_namee}, the password are not the same")
            verif = input(f"{just_namee}, reenter your password ('abc' to remake it): ")
            if verif == "abc":
                fonction_password()
            while verif == "" or verif == " ":
                verif = input(f"pls {just_namee}, reenter your password to be sure: ")
            if verif == password:
                print("password ok")
                break


def first_one():
    global name, just_namee, a, b, password
    name()
    time.sleep(0.7)
    start_password, password = "", ""
    print(f"{just_namee}, you have to define a password")
    if b == 1:
        just_namee = "Elric"
        print(f"for the user {just_namee}sama, the password is already defined:")
        password = "Elric33160"
    else:
        fonction_password()
    hide_password = password[-3:]
    for i in range(len(password) - 3):
        start_password += "*"
    print(f"\n your username is {just_namee.capitalize()}")
    print(f" your password is {start_password + hide_password}")
    input()
