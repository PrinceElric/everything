import itertools, string  # noqa: E401
from tools import start_timer, stop_timer # noqa: E401

def brute_force(target_password, max_length=6):
    # Les caractères possibles : lettres minuscules, majuscules et chiffres
    characters, attempts = string.ascii_lowercase + string.ascii_uppercase + string.digits, 0
    start_timer()
    
    
    for length in range(1, max_length + 1):  # On teste toutes les longueurs de 1 jusqu'à max_length
        print(f"\nTest des combinaisons de longueur {length}...")
        
        
        for combo in itertools.product(characters, repeat=length):
            attempts += 1   # itertools.product génère toutes les combinaisons possibles
            guess = ''.join(combo)
            
            if guess == target_password:
                print(f"\n✅ Mot de passe trouvé : '{guess}'")
                print(f"   Tentatives : {attempts:,}")
                print(f"   Temps écoulé : {print(f'{stop_timer():.2f}')} secondes")
                return guess
    
    print("❌ Mot de passe non trouvé dans la limite fixée.")
    return None

password = input("Entre un mot de passe court à deviner : ")

brute_force(password, max_length=len(password))
input('')