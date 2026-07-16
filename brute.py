import itertools
import string
import time

def brute_force(target_password, max_length=6):
    # Les caractères possibles : lettres minuscules, majuscules et chiffres
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    print("🔍 Recherche du mot de passe en cours...")
    print(f"Caractères utilisés : {len(characters)} (lettres + chiffres)")
    
    attempts = 0
    start_time = time.time()
    
    # On teste toutes les longueurs de 1 jusqu'à max_length
    for length in range(1, max_length + 1):
        print(f"\nTest des combinaisons de longueur {length}...")
        
        # itertools.product génère toutes les combinaisons possibles
        for combo in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(combo)
            
            if guess == target_password:
                elapsed = time.time() - start_time
                print(f"\n✅ Mot de passe trouvé : '{guess}'")
                print(f"   Tentatives : {attempts:,}")
                print(f"   Temps écoulé : {elapsed:.2f} secondes")
                return guess
    
    print("❌ Mot de passe non trouvé dans la limite fixée.")
    return None

# --- Programme principal ---
password = input("Entre un mot de passe court à deviner : ")

if len(password) > 6:
    print("⚠️  Attention : un mot de passe trop long peut prendre très longtemps !")

brute_force(password, max_length=len(password))
input('')