"""
Challenge Sécurité : Crack the Password
Ce script simule une interface de connexion sécurisée avec un mot de passe codé en dur.
Votre défi est de découvrir le mot de passe sans modifier ce script.
Utilisez une méthode de force brute ou toute autre technique que vous jugez appropriée.
"""

def verify_password(input_password):
    real_password = "secretPassword123"  # Mot de passe à découvrir.
    # Simulation d'un processus de vérification complexe.
    return hash(input_password) == hash(real_password)

if __name__ == "__main__":
    attempts = 0
    while attempts < 5:
        user_input = input("Entrez le mot de passe: ")
        if verify_password(user_input):
            print("Accès autorisé. Bienvenue !")
            break
        else:
            print("Accès refusé. Essayez encore.")
            attempts += 1
    if attempts == 5:
        print("Nombre d'essais dépassé. Accès bloqué.")
