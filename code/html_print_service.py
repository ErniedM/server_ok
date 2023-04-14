import html2text
from rich.style import Style
from rich.text import Text
from rich.console import Console

def print_html_in_console():
    '''Printen van HTML naar de console'''
    # Ophalen van de HTML template
    with open("check_lijst.html") as file:
        html = file.read()
    # Converteren van de HTML naar tekst d.m.v. de html2text module
        text = html2text.html2text(html)
    # Definieren van de stijlen van de tekst d.m.v. de rich module
        online_style = Style(color='green')
        offline_style = Style(color='red')
    # Definieren van de tekst met de juiste stijl met de rich module
        status_texts = []
        for line in text.split('\n'):
            if 'online' in line:
                status_texts.append(Text(line.replace('online', '[green]online[/green]'), style=online_style))
            elif 'offline' in line:
                status_texts.append(Text(line.replace('offline', '[red]offline[/red]'), style=offline_style))
            else:
                status_texts.append(Text(line))
    # Printen van de tekst naar de console met de rich module
    console = Console()
    console.print('\n'.join(str(text) for text in status_texts))