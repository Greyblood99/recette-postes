import json
from pathlib import Path

def lire_profil():
    projet = Path(__file__).parent
    chemin_profil = projet/"profil_test.json"
    fichier = open(chemin_profil)
    profil= json.load(fichier)
    return profil