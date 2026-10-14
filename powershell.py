import subprocess

def executer_powershell(commande):
    resultat = subprocess.run(
    ["powershell", "-Command", commande],
    capture_output=True,
    text=True
    )

    return resultat.stdout.strip()

nom_pc = executer_powershell("hostname")

print(nom_pc)