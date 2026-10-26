from configuration import lire_configuration
from profil import lire_profil

from sondes import (
    obtenir_ram,
    obtenir_disque,
    obtenir_nom_pc,
    obtenir_version_windows,
    obtenir_pare_feu
)

from comparaison import (
    verifier_min,
    verifier_egalite,
    verifier_pare_feu,
    calculer_verdict,
    creer_resultat
)

# Configuration
profils, pv = lire_configuration()

print(f"Profils : {profils}")
print(f"PV : {pv}")

# Profil
profil = lire_profil()

print(profil["nom"])

# Informations du poste
nom_pc = obtenir_nom_pc()
version_windows = obtenir_version_windows()
pare_feu = obtenir_pare_feu()

print(nom_pc)
print(version_windows)
print(type(version_windows))
print(pare_feu)

# Catalogue des contrôles minimums
catalogue = [
    {
        "libelle": "RAM",
        "gravite": "majeur",
        "sonde": obtenir_ram,
        "cle": "memoire_min"
    },
    {
        "libelle": "Disque",
        "gravite": "majeur",
        "sonde": obtenir_disque,
        "cle": "disque_min"
    }
]

resultats = []

# Contrôles RAM et Disque
for controle in catalogue:

    obtenu = controle["sonde"]()

    attendu = profil[controle["cle"]]

    verdict = verifier_min(
        obtenu,
        attendu
    )

    resultat = creer_resultat(
        controle["libelle"],
        attendu,
        obtenu,
        verdict,
        controle["gravite"]
    )

    resultats.append(resultat)

# Contrôle nom du poste
verdict_nom_pc = verifier_egalite(
    nom_pc,
    profil["nom_pc"]
)

resultat_nom_pc = creer_resultat(
    "Nom du poste",
    profil["nom_pc"],
    nom_pc,
    verdict_nom_pc,
    "majeur"
)

resultats.append(resultat_nom_pc)

# Contrôle version Windows
verdict_windows = verifier_egalite(
    version_windows,
    profil["version_windows"]
)

resultat_windows = creer_resultat(
    "Version Windows",
    profil["version_windows"],
    version_windows,
    verdict_windows,
    "bloquant"
)

resultats.append(resultat_windows)

# Contrôle pare-feu
verdict_pare_feu = verifier_pare_feu(
    pare_feu
)

resultat_pare_feu = creer_resultat(
    "Pare-feu",
    "3 profils actifs",
    pare_feu,
    verdict_pare_feu,
    "bloquant"
)

resultats.append(resultat_pare_feu)

# Affichage des résultats
print("\n- Résultats des contrôles -")

nb_conformes = 0

for resultat in resultats:

    if resultat["verdict"] == "Conforme":
        nb_conformes += 1

    print(
        f"{resultat['controle']} | "
        f"Attendu : {resultat['attendu']} | "
        f"Obtenu : {resultat['obtenu']} | "
        f"Verdict : {resultat['verdict']}"
    )

# Verdict global
verdict_global = calculer_verdict(
    resultats
)

print(
    f"\nContrôles conformes : "
    f"{nb_conformes}/{len(resultats)}"
)

print(f"\nVerdict global : {verdict_global}")
