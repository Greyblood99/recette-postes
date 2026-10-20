from comparaison import calculer_verdict

liste = [
    {"controle": "RAM", "verdict": "Conforme", "gravite": "majeur"},
    {"controle": "Disque", "verdict": "Indéterminé", "gravite": "majeur"},
]
print(calculer_verdict(liste))