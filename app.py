import flet
from flet import Page
from windows.profesorados import Profesorados

def main (page:Page):
    page.update()
    profesorados = Profesorados()
    page.add(profesorados)
    
flet.app(target=main)