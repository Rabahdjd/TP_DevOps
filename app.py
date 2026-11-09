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
    print("1. Se connecter avec un compte")
    print("2. Continuer en mode invite")
    choix = input("Votre choix (1/2) : ").strip()

    if choix == "1":
        user = input("Nom d'utilisateur : ")
        pwd = input("Mot de passe : ")
        if authentifier(user, pwd):
            print(f"Bienvenue, {user} ! Authentification reussie.")
        else:
            print("Erreur : identifiants incorrects.")
    else:
        session_id = "GUEST-9999"
        print(f"Connecte avec le statut invite : {session_id}")
        print("Acces restreint au catalogue.")

if __name__ == "__main__":
    main()
