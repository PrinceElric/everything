from functools import reduce  # noqa: E402
from math import pow
import countries as state
from tools import *  # noqa: F403
def nv1():
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
    a = 0
    # Exercices : Niveau 1
    ## Expliquez la différence entre map, filter et reduce.
    # Expliquez la différence entre une fonction d'ordre supérieur, une fermeture et un décorateur.
    # Définissez une fonction d'appel avant map, filter ou reduce, voir les exemples.
    # Utilisez une boucle for pour afficher chaque pays de la liste des pays.

    # map applique a toutes les valeurs d'une liste une fonciton et renvoi une liste
    # filter ne renvoi que les elements qui sont retournés True par la fnction
    # reduce aplique la fonciton a a et b et renduit en a et chang la liste pour repeter l'operation

    for p in names:
        a += 1
        if a == len(names):
            continue
        else:
            print(p, end = ' - ')
    print(names[len(names)-1])
    

def nv2():
    countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Countriess = state.countries
    ## Utilisez la carte pour créer une nouvelle liste en mettant chaque pays en majuscules dans la liste des pays.
    ## Utilisez la carte pour créer une nouvelle liste en remplaçant chaque nombre par son carré dans la liste des nombres.
    ## Utilisez la fonction map pour convertir chaque nom en majuscules dans la liste des noms.
    ## Utilisez le filtre pour exclure les pays contenant le mot « terre ».
    ## Utilisez le filtre pour exclure les pays dont le nom comporte exactement six caractères.
    ## Utilisez le filtre pour exclure les pays dont le nom contient six lettres ou plus dans la liste des pays.
    ## Utilisez le filtre pour exclure les pays commençant par la lettre « E ».
    ## Enchaînez deux ou plusieurs itérateurs de liste (par exemple, arr.map(callback).filter(callback).reduce(callback))
    ## Déclarez une fonction appelée get_string_lists qui prend une liste comme paramètre et renvoie une liste contenant uniquement des chaînes de caractères.
    ## Utilisez la fonction reduce pour additionner tous les nombres de la liste de nombres.
    ## Déclarez une fonction appelée categorize_countries qui renvoie une liste de pays ayant un modèle commun (vous pouvez trouver la liste des pays dans ce dépôt sous le nom countries.js(eg 'land', 'ia', 'island', 'stan')).
    ## Créez une fonction renvoyant un dictionnaire, où les clés représentent les premières lettres des pays et les valeurs le nombre de noms de pays commençant par cette lettre.
    ## Déclarez une fonction get_first_ten_countries - elle renvoie une liste des dix premiers pays de la liste countries.js dans le dossier data.
    ## Déclarez une fonction get_last_ten_countries qui renvoie les dix derniers pays de la liste countries.

    print(list(map(lambda x: x.upper(), countries)))
    print(list(map(lambda x: pow(x, 2), numbers)))
    print(list(map(lambda x: x.upper(), names)))
    print(list(filter(lambda x: False if 'land' in x else True, countries)))
    print(list(filter(lambda x: True if len(x) != 6 else False, countries)))
    print(list(filter(lambda x: True if not len(x) >= 6 else False, countries)))
    print(list(filter(lambda x: False if x[0] == 'E' else True, countries)))
    print(list(filter(lambda x: True if len(x) != 6 else False, list(filter(lambda e: False if e[0] == 'E' else True, countries)))))

    def get_string_lists(*args):
        return list(map(lambda x: str(x), *args))
    def add(x, y):
        return int(x) + int(y)
    print(reduce(add, numbers))
    
    def categorize_countries():
        clear()  # noqa: F405
        print(list(filter(lambda x: 'land' in x, Countriess)))
        print(list(filter(lambda x: 'stan' in x, Countriess)))
        
    def accumuler(acc, f):
        acc[f[0]] = acc.get(f[0], 0) + 1
        return acc
    print(reduce(accumuler, Countriess, {}))
    
    def get_first_ten_countries():
        print(list(filter(lambda x: Countriess.index(x) < 10, Countriess)))
    def get_last_ten_countries():
        print(list(filter(lambda x: Countriess.index(x) > len(Countriess) - 10, Countriess)))
    clear()  # noqa: F405
    get_last_ten_countries()
nv2()