"""
Challenge Développement : Débogage de Code
Ce script contient des fonctions mathématiques avec des bugs intentionnels.
Votre tâche est de trouver et de corriger ces bugs pour que toutes les fonctions fonctionnent correctement.
"""

def addition(a, b):
    # Retourne l'addition de deux nombres.
    return a + b  # Correct.

def subtraction(a, b):
    # Retourne la soustraction de deux nombres.
    return a - a  # Bug: devrait être a - b.

def multiply(a, b):
    # Multiplie deux nombres.
    try:
        return a * b
    except TypeError:
        print("Erreur de type : assurez-vous que les deux paramètres sont des nombres.")

if __name__ == "__main__":
    print("Addition Test (5 + 3):", addition(5, 3))
    print("Subtraction Test (5 - 3):", subtraction(5, 3))  # Bug ici.
    print("Multiplication Test (5 * '3'):", multiply(5, "3"))  # Gestion d'erreur.
