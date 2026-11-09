"""
Application de gestion des etudiants et modules
Module DevOps - TP 1
"""

def afficher_accueil():
    print("========================================")
    print("   Application de Gestion TP DevOps     ")
    print("========================================")

def authentifier(username, password):
    """Fonctionnalite d'authentification utilisateur."""
    users = {"admin": "secret123", "rabah": "devops2026"}
    return users.get(username) == password

def main():
    afficher_accueil()
    print("[Module Connexion Active]")
    user = input("Nom d'utilisateur : ")
    pwd = input("Mot de passe : ")
    if authentifier(user, pwd):
        print(f"Bienvenue, {user} ! Authentification reussie.")
    else:
        print("Erreur : identifiants incorrects.")

if __name__ == "__main__":
    main()
