import configparser

def lire_configuration():
    lecteur = configparser.ConfigParser()
    lecteur.read("config.ini")

    profils = lecteur.get("projet", "profils")
    pv = lecteur.get("projet", "pv")

    return profils, pv