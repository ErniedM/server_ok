import os
import json

def lijst_aanmaken(lijstnaam):
    '''Aanmaken van een lege lijst'''
    if not os.path.exists(f"{lijstnaam}.json"):
        with open(f"{lijstnaam}.json", "w") as file:
            json.dump([], file)

def lijst_ophalen(lijstnaam):
    '''Ophalen van de bestaande lijst'''
    with open(f"{lijstnaam}.json", "r") as file:
        lijst = json.load(file)
        return lijst

def lijst_wegschrijven(lijstnaam, lijst):
    '''Wegschrijven/overschrijven van een lijst'''
    with open(f"{lijstnaam}.json", "w") as file:
        json.dump(lijst, file)