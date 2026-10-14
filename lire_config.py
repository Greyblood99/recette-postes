import json
from pathlib import Path
from powershell import executer_powershell
from configuration import lire_configuration
from profil import lire_profil
from sondes import obtenir_ram, obtenir_disque, obtenir_nom_pc
from comparaison import verifier_min, verifier_nom_pc



profils, pv = lire_configuration()

print(f"Profils : {profils}")
print(f"PV : {pv}")


profil = lire_profil()
print(profil["nom"])


nom_pc = obtenir_nom_pc()
# nom_pc = executer_powershell("hostname")
print(nom_pc)



ram_pc = obtenir_ram()
disque_pc = obtenir_disque()

# def verifier_ram(ram_pc, ram_min):
#     if ram_pc>= ram_min:
#         return "Conforme"
#     else:
#         return "Écart"

# def verifier_disque(disque_pc, disque_min):
#     if disque_pc >= disque_min:
#         return "Conforme"
#     else:
#         return "Écart"


# def verifier_nom_pc(nom_obtenu, nom_attendu):
#     if nom_obtenu == nom_attendu:
#         return "Conforme"
#     else:
#         return "Écart"



    
print(f"RAM du PC : {ram_pc} Go")
print(f"RAM minimale : {profil['memoire_min']} Go")
print(f"Disque libre du PC : {disque_pc} Go")
print(f"Disque minimum : {profil['disque_min']} Go")


# if ram_pc >= profil["memoire_min"]:
#     print("Conforme")
# else:
#     print("Non conforme")


verdict_ram = verifier_min(
    ram_pc,
    profil["memoire_min"]
)
print(f"mémoire ram : {verdict_ram}")
verdict_disque = verifier_min(
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
    "verdict": verdict_ram,
    "gravite": "majeur"
}
resultat_disque = {
    "controle": "Disque",
    "attendu": profil["disque_min"],
    "obtenu": disque_pc,
    "verdict": verdict_disque,
    "gravite": "majeur"
}

resultat_nom_pc = {
    "controle": "Nom du poste",
    "attendu": profil["nom_pc"],
    "obtenu": nom_pc,
    "verdict": verdict_nom_pc,
    "gravite": "majeur"
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

