from powershell import executer_powershell

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

def obtenir_nom_pc():
    return executer_powershell("hostname")
    