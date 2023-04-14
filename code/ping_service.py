def ping_check():
    import json
    from jinja2 import Template
    from ping3 import ping
    from lijst_manipulatie import lijst_aanmaken, lijst_ophalen, lijst_wegschrijven

    # Loggen van ping resultaten
    lijstnaam1 = "server_lijst"
    lijstnaam2 = "check_lijst"
    lijst_aanmaken(lijstnaam1)
    lijst_aanmaken(lijstnaam2)
    server_lijst=lijst_ophalen(lijstnaam1)
    check_lijst=lijst_ophalen(lijstnaam2)
    for server in server_lijst:
        response = ping(server)
        if response == False:
            check_lijst.append(f"{server} is offline")
        else:
            check_lijst.append(f"{server} is online")
    lijst_wegschrijven(lijstnaam2, check_lijst)

    # Ophalen van HTML template
    with open('html_template.html') as file:
        template_html = file.read()

    # Renderen van HTML template met check_lijst data
    template = Template(template_html)
    with open(f"{lijstnaam2}.json") as file:
        data = json.load(file)
    html = template.render(data=data)

    # Wegschrijven van HTML bestand
    with open(f"{lijstnaam2}.html", "w") as file:
        file.write(html)

def main():
    ping_check()

if __name__ == "__main__":
    main()
