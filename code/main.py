import sys
import os
from server_manipulatie import server_toevoegen, server_verwijderen, servers_tonen
from lijst_manipulatie import lijst_aanmaken, lijst_ophalen, lijst_wegschrijven
from crontab_manipulatie import schedule_check_toevoegen, scheduled_check_verwijderen
from html_print_service import print_html_in_console

def command_line(server_lijst):
    '''Command line parameters verwerken'''
    if sys.argv[2] == "1":
        server_lijst=server_toevoegen(server_lijst)
    elif sys.argv[2] == "2":
        server_lijst=server_verwijderen(server_lijst)
    elif sys.argv[2] == "3":
        servers_tonen()
    else:
        print("Ongeldige command line parameter")
    return server_lijst

def terminal(server_lijst):
    '''Terminal menu keuzes verwerken'''
    while True:
        os.system("clear")
        print("1. Server toevoegen")
        print("2. Server verwijderen")
        print("3. Servers tonen")
        print("4. Stoppen")
        keuze = input("Keuze: ")   
        if keuze == "1":
            server_toevoegen(server_lijst)
        elif keuze == "2":
            server_verwijderen(server_lijst)
        elif keuze == "3":
            os.system("clear")
            servers_tonen(server_lijst)
            input("druk op enter om verder te gaan")
        elif keuze == "4":
            break
        else:
            print("Ongeldige keuze")
    return server_lijst

def main():
    '''Main functie: Ingave en uitvoering'''
    lijstnaam1 = "server_lijst"
    lijstnaam2 = "check_lijst"
    lijst_aanmaken(lijstnaam1)
    lijst_aanmaken(lijstnaam2)
    if len(sys.argv) == 1: # Terminal input verwerken indien er geen extra argumenten worden meegegeven
        lijst_wegschrijven(lijstnaam1, terminal(lijst_ophalen(lijstnaam1)))
    elif len(sys.argv) > 2 and sys.argv[1] == "M": # Command line parameters verwerken indien er een M (management) wordt meegegeven en een cijfer (1,2 of 3)   
        lijst_wegschrijven(lijstnaam1, command_line(lijst_ophalen(lijstnaam1)))
    elif len(sys.argv) == 2 and sys.argv[1] == "M": # Terminal input verwerken indien er eenkel een M (management) wordt meegegeven
        lijst_wegschrijven(lijstnaam1, terminal(lijst_ophalen(lijstnaam1)))
    elif len(sys.argv) > 2 and sys.argv[1] == "C": # Command line parameters verwerken indien er een C (check) wordt meegegeven en een cijfer (1,2 of 3)
        if sys.argv[2] == "1":
            schedule_check_toevoegen("s127280", "ping_service.py", 1)
        elif sys.argv[2] == "2":
            scheduled_check_verwijderen("s127280", "ping_service.py")
        elif sys.argv[2] == "3":
            print_html_in_console()
    else:
        print("Ongeldige command line parameter")

if __name__ == "__main__":
    main()