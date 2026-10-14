import configparser
from pathlib import Path


def lire_configuration():
    lecteur = configparser.ConfigParser()
    projet = Path(__file__).parent
    chemin_config = projet/"config.ini"
    lecteur.read(chemin_config)

    profils = lecteur.get("projet", "profils")
    pv = lecteur.get("projet", "pv")

    return profils, pv