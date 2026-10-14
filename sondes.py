from powershell import executer_powershell

def obtenir_ram():
    try:
        ram = executer_powershell(
            "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory")
        return round(int(ram) / (1024 ** 3))
    except (ValueError, TypeError):
        return None
    # ram_pc = executer_powershell(
    #     "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory")
    # ram_pc = round(int(ram_pc) / (1024 ** 3))
    # print(ram_pc)

# ram_pc = 16

def obtenir_disque():
    try:
        disque = executer_powershell(
        "(Get-PSDrive C).Free")
        return round(int(disque)/(1024**3))
    except (ValueError, TypeError):
        return None

def obtenir_nom_pc():
    return executer_powershell("hostname")


def obtenir_version_windows():
    version = executer_powershell(
        "(Get-ComputerInfo).WindowsProductName"
    )

    return version
    