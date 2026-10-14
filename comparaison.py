

def verifier_min(valeur_obtenue, valeur_attendue):

    if valeur_obtenue is None:
        return "Indéterminé"

    if valeur_obtenue >= valeur_attendue:
        return "Conforme"

    return "Écart"

def verifier_nom_pc(nom_obtenu, nom_attendu):
    if nom_obtenu is None:
        return "Indéterminé"
    if nom_obtenu == nom_attendu:
        return "Conforme"
    
    return "Écart"