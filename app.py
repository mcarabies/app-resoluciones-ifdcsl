import flet
from flet import Page
from windows.profesorados import Profesorados
from windows.instrumentos import Instrumentos

def main (page:Page):
    page.window_height = 600
    page.window_width = 1200
    page.window_resizable = False
    profesorados = Profesorados()
    instrumentos = Instrumentos()
    page.add(profesorados)
    page.add(instrumentos)

    
flet.app(target=main)