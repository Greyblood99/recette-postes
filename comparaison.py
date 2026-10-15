

def verifier_min(valeur_obtenue, valeur_attendue):

    if valeur_obtenue is None:
        return "Indéterminé"

    if valeur_obtenue >= valeur_attendue:
        return "Conforme"

    return "Écart"

def verifier_egalite(valeur_obtenue, valeur_attendue):
    
    if valeur_obtenue is None:
        return "Indéterminé"
    if valeur_obtenue == valeur_attendue:
        return "Conforme"
    
    return "Écart"

def verifier_pare_feu(valeur):

    if valeur is None:
        return "Indéterminé"

    lignes = valeur.splitlines()

    if lignes == ["True", "True", "True"]:
        return "Conforme"

    return "Écart"



def calculer_verdict(resultats):

    presence_indetermine = False
    presence_ecart_majeur = False
    presence_ecart_mineur = False

    for resultat in resultats:
        
        if resultat["verdict"] == "indéterminé":
            presence_indetermine = True

        elif resultat["verdict"] == "Écart":

            if resultat["gravite"] == "mineur":
                presence_ecart_mineur = True

            elif resultat["gravite"] in ["majeur","bloquant"]:
                presence_ecart_majeur = True

    if presence_indetermine:
        return "Non conforme - contrôle non vérifié"
    
    if presence_ecart_majeur:
        return "Non conforme"

    
    if presence_ecart_mineur:
        return "Conforme avec réserves"

    return "Conforme"