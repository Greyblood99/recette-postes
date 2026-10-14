import configparser
import json
from powershell import executer_powershell

def lire_configuration():
    lecteur = configparser.ConfigParser()
    lecteur.read("config.ini")

    profils = lecteur.get("projet", "profils")
    pv = lecteur.get("projet", "pv")

    return profils, pv

profils, pv = lire_configuration()

print(f"Profils : {profils}")
print(f"PV : {pv}")

def lire_profil():
    fichier = open("profil_test.json")
    profil= json.load(fichier)
    return profil
profil = lire_profil()
print(profil["nom"])



nom_pc = executer_powershell("hostname")

print(nom_pc)

def obtenir_ram():
    ram = executer_powershell(
            "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory")
    return round(int(ram) / (1024 ** 3))
    # ram_pc = executer_powershell(
    #     "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory")
    # ram_pc = round(int(ram_pc) / (1024 ** 3))
    # print(ram_pc)

# ram_pc = 16

def obtenir_disque():
    disque = executer_powershell(
        "(Get-PSDrive C).Free"
    )
    return round(int(disque)/(1024**3))

ram_pc = obtenir_ram()
disque_pc = obtenir_disque()

def verifier_ram(ram_pc, ram_min):
    if ram_pc>= ram_min:
        return "Conforme"
    else:
        return "Non conforme"

def verifier_disque(disque_pc, disque_min):
    if disque_pc >= disque_min:
        return "Conforme"
    else:
        return "Non conforme"


def verifier_nom_pc(nom_obtenu, nom_attendu):
    if nom_obtenu == nom_attendu:
        return "Conforme"
    else:
        return "Non conforme"



    
print(f"RAM du PC : {ram_pc} Go")
print(f"RAM minimale : {profil['memoire_min']} Go")
print(f"Disque libre du PC : {disque_pc} Go")
print(f"Disque minimum : {profil['disque_min']} Go")


# if ram_pc >= profil["memoire_min"]:
#     print("Conforme")
# else:
#     print("Non conforme")


verdict_ram = verifier_ram(
    ram_pc,
    profil["memoire_min"]
)
print(f"mémoire ram : {verdict_ram}")
verdict_disque = verifier_disque(
    disque_pc, profil["disque_min"]
)
print(f"mémoire disque : {verdict_disque}")

verdict_nom_pc = verifier_nom_pc(
    nom_pc,
    profil["nom_pc"]
)

resultat_ram = {
    "controle": "RAM",
    "attendu": profil["memoire_min"],
    "obtenu": ram_pc,
    "verdict": verdict_ram
}
resultat_disque = {
    "controle": "Disque",
    "attendu": profil["disque_min"],
    "obtenu": disque_pc,
    "verdict": verdict_disque
}

resultat_nom_pc = {
    "controle": "Nom du poste",
    "attendu": profil["nom_pc"],
    "obtenu": nom_pc,
    "verdict": verdict_nom_pc
}

print(resultat_ram)
print(resultat_disque)
# resultat = executer_powershell("Get-Date")

# print(resultat)

resultats = []
resultats.append(resultat_ram)
resultats.append(resultat_disque)
resultats.append(resultat_nom_pc)




print("\n- Résultats des contrôles -")

nb_conformes = 0
for resultat in resultats:
    
    if resultat["verdict"] == "Conforme":
        nb_conformes += 1
    print(f"{resultat['controle']} | "
        f"Attendu : {resultat['attendu']} | "
        f"Obtenu : {resultat['obtenu']} | "
        f"Verdict : {resultat['verdict']}"
        )
print(f"\nContrôles conformes : {nb_conformes}/{len(resultats)}")

