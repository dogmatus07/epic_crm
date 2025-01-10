from rich.console import Console

console = Console()

def welcome_message():
    console.print("Bienvenue dans EPIC CRM", style="bold green")
    console.print("Utilisez les commandes disponibles pour gérer votre CRM", style="bold blue")
    