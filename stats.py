def calculer_moyenne(notes):
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

def afficher_statistiques(notes):
    print(f"Nombre de notes : {len(notes)}")
    print(f"Note maximale   : {max(notes) if notes else 0}")
    print(f"Note minimale   : {min(notes) if notes else 0}")
    print(f"Moyenne         : {calculer_moyenne(notes):.2f}")
