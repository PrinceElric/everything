import os, time, sys, subprocess, random, string, msvcrt, json, hashlib, unicodedata  # noqa: E401
from datetime import datetime
try:
    import pyautogui as pag
except ImportError:
    pag = None  # Évite le plantage si absent


# --- Réinitialisation automatique du fichier temporaire au démarrage ---
PATH_TEMP = r"C:\Users\elric\Desktop\vs code\all that\tempo diary.md"
try:
    with open(PATH_TEMP, "w", encoding="utf-8") as f:
        f.write("")  # On écrase avec du vide UNE SEULE FOIS au début !
except:  # Si le dossier existe pas encore, pas de crash  # noqa: E722
    pass

# --- Couleurs ANSI de Base ---
RESET = "\033[0m"
GRAS = "\033[1m"
GRIS = "\033[2m"
ITALIC = "\033[3m"
SOULIGN2 = "\033[4m"
SURLIGN2_BLANC = "\033[7m"
NOIR_INVISIBLE = "\033[8m"
BARR2 = "\033[9m"
ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU = "\033[34m"
ROSE = "\033[35m"
CYAN = "\033[36m"
SURLIGN2_ROUGE = "\033[41m"
SURLIGN2_VERT = "\033[42m"
SURLIGN2_JAUNE = "\033[43m"
SURLIGN2_BLEU = "\033[44m"
SURLIGN2_ROSE = "\033[45m"
SURLIGN2_CYAN = "\033[46m"

# --- NOUVEAU : Couleurs Flashy (Haute Intensité) ---
ROUGE_FLASH = "\033[91m"
VERT_FLASH = "\033[92m"
JAUNE_FLASH = "\033[93m"
BLEU_FLASH = "\033[94m"
ROSE_FLASH = "\033[95m"
CYAN_FLASH = "\033[96m"

# --- Couleurs de Fond Directes (Sans inverser) ---
FOND_NOIR = "\033[40m"
FOND_ROUGE = "\033[41m"
FOND_VERT = "\033[42m"
FOND_JAUNE = "\033[43m"
FOND_BLEU = "\033[44m"
FOND_ROSE = "\033[45m"
FOND_CYAN = "\033[46m"
FOND_GRIS = "\033[100m"  # Fond sombre discret

# --- Super Fusions  ---
ERROR = ROUGE_FLASH + GRAS + SOULIGN2
WARNING = JAUNE_FLASH + ITALIC
SUCCESS = VERT_FLASH + GRAS

# --- Combinaisons Thématiques ---
STYLE_TITRE = "\033[30m" + FOND_CYAN + GRAS  # Texte Noir sur Fond Cyan
MENU_ACTIF = "\033[97m" + FOND_BLEU + GRAS  # Texte Blanc sur Fond Bleu
LOG_DISCRET = GRIS + ITALIC  # Gris et penché
ALERTE_CRITIQUE = "\033[97m" + FOND_ROUGE + GRAS  # Texte Blanc sur Fond Rouge


mots_921 = [
    "abeille", "abricot", "absinthe", "acacia", "académie", "acier", "acompte", "acteur", "action", "adresse",
    "adulte", "aéronef", "aéroport", "affiche", "agathe", "agenda", "agent", "agile", "aigle", "aiguille",
    "aimant", "air", "airelle", "aisance", "alarme", "albatros", "album", "alchimie", "alerte", "algue",
    "alignement", "alliance", "allumette", "alouette", "alpage", "alpha", "altitude", "aluminium", "alvéole", "amande",
    "amarante", "amazone", "ambassade", "ambre", "ambulance", "améthyste", "amiral", "amitié", "amorce", "ampoule",
    "amulette", "ananas", "ancêtre", "ancre", "andromède", "âne", "anémone", "ange", "angora", "animal",
    "anneau", "année", "annuaire", "anomalie", "antenne", "antibiotique", "antilope", "antre", "anxiété", "apache",
    "appareil", "appartement", "appel", "applaudissement", "apport", "appentis", "apprenti", "approche", "aptitude", "aquarium",
    "aquarelle", "aqueduc", "araignée", "arbitre", "arc", "arcade", "arceau", "archipel", "architecture", "archive",
    "arbre", "arbuste", "ardoise", "arène", "argent", "argile", "argument", "aride", "armoire", "armure",
    "arôme", "arpenteur", "arrêt", "arrivée", "arrosoir", "art", "artère", "article", "artifice", "artichaut",
    "artisan", "artiste", "asbeste", "ascenseur", "asphalte", "asphyxie", "aspic", "aspirateur", "asperge", "assaut",
    "assiette", "association", "assonance", "astéroïde", "astre", "astrologie", "astronaute", "astronome", "astuce", "atelier",
    "atlas", "athlète", "atmosphère", "atoll", "atome", "atout", "attache", "attaque", "attente", "attention",
    "attraction", "aubépine", "auberge", "audace", "audience", "auditorium", "auge", "aurore", "auteur", "autruche",
    "avalanche", "avance", "avanie", "avatar", "avenir", "aventure", "avenue", "averse", "aveugle", "avion",
    "avocat", "avoine", "avril", "axe", "axiome", "azalée", "azimut", "azote", "azur", "bâton",
    "badigeonnage", "bagage", "bagarre", "bague", "baguette", "baie", "baignoire", "bail", "baiser", "baisse",
    "balai", "balance", "balcon", "baleine", "balise", "baliste", "balle", "bulletin", "ballon", "bambou",
    "banane", "banc", "bandage", "banderole", "banjo", "banne", "bannière", "banque", "banquet", "baobab",
    "baquet", "bar", "baragouin", "baraque", "barbare", "barbe", "barbeau", "barbecue", "barbillon", "barboteuse",
    "barbouillage", "baril", "bariolage", "baron", "barque", "barrage", "barre", "barrette", "barrière", "baryton",
    "basalte", "bascule", "basilic", "basilique", "bassin", "bassine", "baste", "bastion", "bataille", "bataillon",
    "bateau", "batelage", "batelier", "bâtiment", "bâtisse", "batiste", "bâtonnet", "battage", "battement", "batterie",
    "baume", "bavardage", "bave", "bavette", "bavoir", "bazar", "beauté", "bec", "bécane", "bêche",
    "bécot", "beffroi", "bégonia", "béguine", "beige", "belette", "bélier", "belle", "belvédère", "bémol",
    "bénéfice", "benjoin", "benne", "béquille", "berceau", "berge", "berger", "bergamote", "berline", "bermuda",
    "besace", "besogne", "besoin", "bestiole", "bétail", "bête", "béton", "betterave", "beurre", "bévue",
    "biais", "biberon", "bible", "bibliographie", "bibliothèque", "bicarbonate", "biceps", "bicyclette", "bidon", "bielle",
    "bien", "bienfait", "bière", "bifteck", "bifurcation", "bijou", "bijoutier", "bilan", "bilboquet", "bile",
    "billet", "bille", "billon", "binaire", "binette", "bingo", "binocle", "biographie", "biologie", "biopsie",
    "biotope", "bipède", "bique", "biscotte", "biscuit", "bise", "biseau", "bison", "bistrot", "bitume",
    "bivouac", "bizarre", "blafard", "blâme", "blanquet", "blé", "blaireau", "blâme", "blancheur", "blason",
    "blasphème", "blatte", "blazer", "blessure", "bleu", "bleuet", "blindage", "blister", "blizzard", "bloc",
    "blocage", "blocus", "blond", "blondinet", "blouse", "blouson", "blues", "bluff", "blutage", "boa",
    "bobine", "bocal", "bocage", "bocal", "bogue", "bohémien", "boire", "bois", "boisé", "boisson",
    "boîte", "boiterie", "boîtier", "bol", "bolide", "bombardement", "bombe", "bombance", "bonace", "bonbon",
    "bond", "bonde", "bonheur", "boniche", "boniment", "bonite", "bonjour", "bonne", "bonnet", "bonsoir",
    "bonté", "bonus", "boomerang", "bootlegger", "borax", "bord", "bordeaux", "bordel", "bordure", "borée",
    "borgne", "borne", "bosquet", "bosse", "bosselage", "bosselure", "botanique", "botte", "bottillon", "bottine",
    "bouc", "boucan", "bouche", "bouchée", "boucher", "bouchon", "boucle", "bouclier", "bouddha", "bouderie",
    "boudin", "boue", "bouée", "bouffée", "bouffon", "bouge", "bougie", "bouillon", "bouleau", "boule",
    "bouledogue", "boulet", "boulette", "boulevard", "bouleversement", "boulon", "boulanger", "bouquet", "bouquin", "bourbe",
    "bourbon", "bourde", "bourdon", "bourg", "bourgeon", "bourrasque", "bourre", "bourreau", "bourrique", "bourse",
    "boursouflure", "bousculade", "bouse", "boussole", "bout", "boutique", "bouton", "bouture", "bouvier", "bovidé",
    "bowling", "boxe", "boxeur", "boyau", "boycott", "bracelet", "braconnier", "braise", "brame", "brancard",
    "branche", "branchie", "brande", "brandy", "branle", "braquage", "bras", "brasero", "brassard", "brasse",
    "brasserie", "brasseur", "brassière", "bravade", "bravo", "bravoure", "break", "brebis", "brèche", "bredouillage",
    "bref", "bréviaire", "breuvage", "brevet", "bribe", "bricolage", "bride", "bridge", "brie", "briefing",
    "brigade", "brigand", "brillant", "brillantine", "brique", "brioche", "bribe", "brique", "briquet", "bris",
    "brise", "briscard", "brisure", "broc", "brocanteur", "brocard", "broche", "brochet", "brochette", "brochure",
    "brocoli", "brodequin", "broderie", "bronchite", "bronze", "brosse", "brouette", "brouhaha", "brouillard", "brouille",
    "brouillon", "broussaille", "brousse", "broutille", "broyage", "bruit", "brûlure", "brume", "brun", "brune",
    "brusquerie", "brut", "brutalité", "buisson", "bulbe", "bulle", "bureau", "cabane", "cactus", "cadeau",
    "cadenas", "café", "cage", "caillou", "calculatrice", "caméléon", "caméra", "camion", "campagne", "canard",
    "canapé", "canne", "canon", "cape", "capitaine", "carotte", "carte", "carton", "cascade", "casque",
    "castor", "caverne", "cèdre", "ceinture", "célèbre", "cerf", "cerise", "cerveau", "chaîne", "chaise",
    "chaleur", "chameau", "champignon", "chanson", "chantier", "chapeau", "chargeur", "chat", "château", "chaudron",
    "chaussette", "chemin", "cheminée", "chêne", "chenille", "cheval", "chien", "chimie", "chimpanzé", "chocolat",
    "ciel", "cigogne", "citadelle", "citron", "clairière", "clé", "cloche", "clou", "cobra", "coccinelle",
    "coffre", "colline", "colombe", "comète", "compas", "concert", "confiture", "corail", "corbeau", "corde",
    "couronne", "couteau", "crabe", "cratère", "crayon", "cristal", "crocodile", "croissant", "cuillère", "cuir",
    "cygne", "cylindre", "damier", "danse", "diamant", "dinosaure", "diplôme", "disque", "dollar", "dôme",
    "dragon", "drapeau", "drone", "écharpe", "échelle", "éclair", "éclipse", "écorce", "écureuil", "église",
    "élastique", "éléphant", "émeraude", "enclume", "encre", "épée", "éponge", "épouvantail", "escargot", "escalier",
    "espadon", "espoir", "essence", "étoile", "étudiant", "éventail", "explorateur", "fabrique", "falaise", "famille",
    "fantôme", "farine", "feu", "feuille", "feutre", "ficelle", "figue", "fil", "fjord", "flamme",
    "flèche", "fleur", "fleuve", "flocon", "flûte", "forêt", "forge", "four", "fourchette", "fraise",
    "framboise", "frégate", "fromage", "fusée", "galaxie", "garage", "gardien", "gazelle", "géant", "gemme",
    "girafe", "glace", "glacier", "gobelet", "gomme", "gorille", "goutte", "grain", "gravité", "grenouille",
    "griffe", "grue", "guitare", "hache", "hamac", "harpe", "hélicoptère", "hibou", "hippopotame", "hôpital",
    "horizon", "horloge", "hublot", "huile", "iceberg", "igloo", "île", "immeuble", "incendie", "indigo",
    "infirmier", "insecte", "internet", "iris", "jaguar", "jardin", "jasmin", "jet", "jongleur", "journal",
    "juge", "jungle", "kangourou", "kayak", "kiwi", "koala", "labyrinthe", "lac", "lampe", "lanterne",
    "laser", "lavande", "légende", "léopard", "lettre", "levier", "liberté", "licorne", "lierre", 'lion', 'liste', 'livre',
    "loup", "loupe", "lune", "lutin", "machine", "magicien", "maison", "mammouth", "mangue",
    "marais", "marbre", "marteau", "masque", "médaillon", "médecin", "melon", "mer", "mercure", "message",
    "météore", "métro", "micro", "miroir", "montagne", "montre", "moteur", "moulin", "mur", "musée",
    "musique", "navire", "neige", "ninja", "nuage", "océan", "olive", "ombre", "orage", "orchidée",
    "ordinateur", "oreiller", "orignal", "ours", "outil", "palette", "palmier", "paon", "papillon", "parachute",
    "parapluie", "parfum", "paris", "parquet", "pastèque", "patate", "patin", "patrouille", "paume", "pêche",
    "peinture", "pelouse", "pendule", "perle", "perroquet", "phare", "phénix", "photo", "piano", "pieuvre",
    "pilote", "pin", "pirate", "piscine", "pistolet", "plage", "planète", "plante", "pluie", "poire",
    "poisson", "pomme", "pont", "porcelaine", "porte", "portefeuille", "prairie", "prisme", "prison", "projecteur",
    "pyramide", "python", "quille", "radio", "raisin", "ravin", "requin", "restaurant", "rivière", "robot",
    "rocher", "rose", "roue", "rubis", "ruche", "sabre", "sac", "salade", "sapin", "satellite",
    "saxophone", "science", "scorpion", "serpent", "serveur", "singe", "sirène", "skieur", "société", "soleil",
    "sommet", "souris", "sphinx", "spirale", "statue", "stylo", "sucre", "table", "tableau", "tambour",
    "tempête", "temple", "tennis", "terre", "tigre", "tomate", "tornade", "tortue", "tour", "tracteur",
    "train", "trampoline", "trésor", "triangle", "trompette", "trône", "tunnel", "turbine", "uniforme", "univers",
    "usine", "vague", "valise", "vampire", "vase", "vélo", "verre", "viaduc", "violon", "virus",
    "vitrine", "volcan", "voleur", "voiture", "wagon", "yacht", "yak", "zèbre", "zeppelin", "zinc"
]

def clear():
    os.system('cls')

def copier_txt(texte):
    """copie texte dans presse-papier, need subprocess"""
    subprocess.run(["clip"], input=texte, text=True, check=True)


def trouver_nom(objet):
    for nom, valeur in globals().items():
        if valeur is objet:
            return nom
    return None

def fonct_mots():
    global mots_921
    nom = trouver_nom(mots_921)
    print(f"{nom} = {len(mots_921)}")
    if nom != "mots_" + str(len(mots_921)):
        print(f"{ERROR}Problem with the name of {nom}{RESET}")
    word = "science"
    while True:  # noqa: F821
        word = input("Enter a word:    ").lower()
        if word == "clear":
            clear()
            fonct_mots()
        elif word == 'quit':
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
            elif accept_enter.lower() == 'quit':
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

# --- Fonctions ---
def cprint(texte, color):
    """Affiche texte coloré puis réinitialise style."""
    print(f"{color}{texte}{RESET}")


def detect_shutdown():
    """shutdown -a twice with sleep of 0.4 btw the two"""
    for _ in range(2):
        os.system("shutdown -a")
        time.sleep(0.4)


def shutdown_A():
    os.system("shutdown -a")


def hach_word(word):
    return hashlib.sha256(word.encode()).hexdigest()

def shutdown(temps=40, kill=False):
    """Arrêt du PC avec protection par mot de passe et bien d'autres."""
    def load_config(chemin="config.json"):
        """Charge la configuration JSON en toute sécurité. Renvoie un dict vide si échec."""
        if not os.path.exists(chemin):
            return {}
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save_config(data, chemin="config.json"):
        """Sauvegarde les données dans un fichier JSON. Renvoie un booléen de succès."""
        try:
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False
        copier_txt("shutdown -a")
    config = load_config()
    password_reel = config["password"]
    def launch_shutdown(temps):
        shutdown_A()
        clear()
        os.system(f"shutdown -s -t {temps}")

    def temps_stay():
        return timer - (time.time() - debut)

    def force_shutdown(timer=6, mode_normal=True, password=''):  # noqa: F821
        
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
            pass          # mot de passe spécial
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
    clear()
    print(f"{SUCCESS}Arrêt annulé.{RESET}")
    detect_shutdown()
    clear()

#shutdown(kill=True)

def format_number(n):
    """Formate un nombre en le sequencant en pattern de 3"""
    return f"{n:,}".replace(",", "'")


def slow_type(texte, tps_total=False, tps_btw_letters=False, color=""):
    """Print string character by character with tiny delay. and color if you want"""
    for letter in texte:
        if tps_total:
            temps_de_latence = tps_total / len(texte)
            time.sleep(float(temps_de_latence))
            print(f"{color}{letter}{RESET}", end="", flush=True)
        if tps_btw_letters:
            time.sleep(float(tps_btw_letters))
            print(f"{color}{letter}{RESET}", end="", flush=True)



def loading_bar(tps, symbol="#", lenght=10):
    """Barre de progression avec étapes X/Y et pourcentage exact."""
    pourc1 = 100 / lenght
    for i in range(1, lenght + 1):
        pourcentage = i * pourc1
        barre = symbol * i
        vide = "." * (lenght - i)
        
        clear()
        print(f"[{barre}{vide}]    {i}/{lenght}  ({pourcentage:.1f}%)")
        time.sleep(tps / lenght)
        
    clear()
    cprint(f"{symbol * lenght}    {lenght}/{lenght} (100.0%)", VERT_FLASH)


_timers = {}


def start_timer(nom="default", entrées=False):
    """Démarre ou réinitialise un chrono avec un nom donné."""
    global _timers
    if entrées:
        start = time.process_time()
    else:
        start = time.perf_counter()
    _timers[nom] = start
    return start


def stop_timer(nom="default", entrées=False):
    """Affiche temps écoulé pour le chrono spécifié."""
    global _timers
    if nom not in _timers:
        print(f"{ERROR}Erreur : Chrono '{nom}' non démarré.{RESET}")
        return

    if entrées:
        fin = time.process_time()
    else:
        fin = time.perf_counter()

    print(f"[{nom}] {fin - _timers[nom]:.6f} s")


def human_time(n):
    """Convert big # of sec into a digit info (00h:00min:00s)"""
    h, minutes, sec = 00, 00, 00
    h = n // 3600
    n = n % 3600
    minutes = n // 60
    sec = n % 60
    print(f"{h:02d}h:{minutes:02d}min:{sec:02d}s")


def valid_input(type='int', phrase=""):
    """Demande une entrée d'un type précis et boucle tant que l'entrée est invalide."""
    if type == "str":
        phrase = phrase or "enter a string"
        return input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()
        
    elif type in ["int", "float"]:
        phrase = phrase or "enter a number"
        while True:
            entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()
            try:
                return int(entree) if type == "int" else float(entree)
            except ValueError:
                print(f"{ERROR}Incorrect enter, try again{RESET}")
                
    elif type == "bool":
        phrase = phrase or "enter True/Yes or False/No"
        entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip().lower()
        return entree in ["true", "t", "1", "y", "yes", "o", "oui"]
        
    print(f"{ERROR}INCORRECT TYPE!!!{RESET}")
    return None


def clear_lines(n=1):
    """Efface un nombre de lignes donne dans le terminal."""
    for _ in range(n):
        sys.stdout.write("\033[1F\033[2K")
    sys.stdout.flush()


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


def faire_titre_section(texte, symbole="-", largeur=60):
    """mettre texte et symbole, funct centre et fait une ligne de symbole de size largeur"""
    texte_grand = texte.upper()

    print(symbole * largeur)
    # Utilisation de STYLE_TITRE ici
    print(f"{STYLE_TITRE}{texte_grand.center(largeur)}{RESET}")
    print(symbole * largeur)


def menu_options(options):
    """enter a list of options, show a interactif select menu, return the option chose"""
    index, taille = 0, len(options)

    while True:
        clear()
        print("=== CHOISIS TA VIANDE (Z: Haut, S: Bas, Entrée: OK) ===")

        # Afficher options
        for i in range(taille):
            if i == index:
                # Utilisation de la nouvelle fusion MENU_ACTIF
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


def ecrire_log(
    message,
    type_log="INFO",
    chemin_fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md",
):
    """Graver message avec date et étiquette [INFO/WARNING/ERROR]"""
    type_log = type_log.upper()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne_log = f"[{date_str}] [{type_log}] {message}\n"

    if chemin_fichier in ["données", "donnée", "donnee", "donnees"]:
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


def afk_mouse(n=False, kill=False):
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
