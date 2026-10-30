[README.md](https://github.com/user-attachments/files/34184796/README.md)
# Recette des postes – EXPERTY

Application de bureau (Python + Tkinter) qui vérifie l'état d'un poste Windows fraîchement
déployé, le compare à un **profil de référence** (fichier JSON), affiche un tableau
Conforme / Écart / Indéterminé, propose des corrections automatiques et édite un
**procès-verbal de recette** horodaté au format PDF.

Projet BTS SIO option SLAM – « 3.1 SLAM – Projet Recette des postes ».

## Ce que fait l'outil

- 25 contrôles répartis en 7 domaines (identité, matériel, système, sécurité, logiciels,
  environnement, journaux), dont 14 corrigeables automatiquement.
- Le profil décide de tout : changer une valeur dans `profils/*.json` change le résultat
  de la recette, sans toucher au code.
- Rien n'est modifié sans clic sur « Corriger » puis confirmation. Chaque correction est
  journalisée et vérifiée en relisant le contrôle.
- Verdict global : Conforme, Conforme avec réserves, Non conforme.

## Prérequis

- Windows 11, droits administrateur.
- Python 3 (développement uniquement : l'exécutable n'en a pas besoin).
- Tout test qui modifie le système se fait dans une machine virtuelle.

## Installation (développement)

```powershell
py -m pip install -r requirements.txt
```

## Lancer

```powershell
py main.py                          # interface graphique (PowerShell administrateur)
py main_console.py                  # liste les profils disponibles
py main_console.py POSTE-COMPTABLE  # recette en console
py test_verdict.py                  # test du calcul du verdict
```

## Organisation du code

| Fichier | Rôle |
|---|---|
| `main.py` | point d'entrée graphique |
| `interface.py` | fenêtre Tkinter, thread de travail et file de messages |
| `moteur.py` | parcourt le catalogue et produit un résultat par contrôle |
| `catalogue.py` | description des 25 contrôles (gravité, sonde, comparaison, correction) |
| `sondes.py` | lecture de l'état du poste (ne juge pas, ne corrige pas) |
| `comparaison.py` | comparaison attendu / constaté et verdict global |
| `corrections.py` | les 14 corrections automatiques |
| `powershell.py` | **fonction unique** d'appel à PowerShell |
| `profil.py` | lecture et validation du profil, empreinte SHA-256 |
| `configuration.py` | lecture de `config.ini` |
| `journal.py`, `session.py` | journal de session, session et reprise après redémarrage |
| `proces_verbal.py` | génération du PDF (reportlab) |
| `systeme.py` | petites fonctions Windows utilisées par l'interface |

Les sondes et les corrections ne connaissent pas Tkinter ; l'interface ne contient aucune
commande système.

## Configuration et profils

- `config.ini` : dossiers (profils, PV, journal), dossier des clés BitLocker, opérateur par
  défaut, délais maximaux des commandes. Placé à côté de l'application.
- `profils/` : `POSTE-COMPTABLE.json` (profil du banc d'essai), `POSTE-ACCUEIL.json`,
  `POSTE-DIRECTION.json`.
- Le format des profils est décrit dans la documentation technique (partie B).

## Banc d'essai

`scripts/degradation.ps1` dégrade volontairement la machine virtuelle (10 écarts
documentés). Procédure : restaurer l'instantané « conforme », lancer le script en
PowerShell administrateur, redémarrer, prendre l'instantané « dégradé ».

## Empaquetage

```powershell
py -m PyInstaller --onefile --noconsole --uac-admin --name RecettePostes main.py
```

Copier ensuite `config.ini` et le dossier `profils` à côté de `dist\RecettePostes.exe`
(ils ne sont pas embarqués : ils restent modifiables sans recompilation).

## Sécurité

- Aucun mot de passe dans le dépôt. Les clés de récupération BitLocker (dossier `cles/`),
  les journaux et les PV sont exclus par `.gitignore`.
- L'application ne désinstalle jamais de logiciel, n'active jamais BitLocker, ne supprime
  jamais de compte et ne désactive jamais Windows Update.
