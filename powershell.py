import subprocess

def executer_powershell(commande):
    try:
        resultat = subprocess.run(
        ["powershell", "-Command", commande],
        capture_output=True,
        text=True,
        timeout= 5
        )
    except subprocess.TimeoutExpired:
        return None
    return resultat.stdout.strip()