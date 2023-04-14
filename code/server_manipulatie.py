def server_toevoegen(server_lijst):
    '''Een server toevoegen aan de serverlijst'''
    naam = input("Naam: ")
    server_lijst.append(naam)
    return server_lijst

def server_verwijderen(server_lijst):
    '''Een server verwijderen uit de serverlijst'''
    naam = input("Naam: ")
    for server in server_lijst:
        if server == naam:
            server_lijst.remove(server)
            break
    return server_lijst

def servers_tonen(server_lijst):
    '''Alle servers tonen'''
    teller=0
    while teller < len(server_lijst):
        print(f"server{teller+1}: {server_lijst[teller]}")
        teller += 1