"""
Application de gestion des etudiants et modules
Module DevOps - TP 1
"""

def afficher_accueil():
    print("========================================")
    print("   Application de Gestion TP DevOps     ")
    print("========================================")

def main():
    afficher_accueil()
    print("[Session Invité]")
    session_id = "GUEST-9999"
    print(f"Connecté avec le statut invité : {session_id}")
    print("Accès restreint au catalogue.")

if __name__ == "__main__":
    main()
