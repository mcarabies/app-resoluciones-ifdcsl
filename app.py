import flet
from flet import Page, View, AppBar,ElevatedButton, Text, colors, Row, Container, Column, Icon, icons, IconButton
from windows.profesorados import Profesorados
from windows.instrumentos import Instrumentos

def main (page:Page):
    page.window_height = 600
    page.window_width = 1200
    page.window_resizable = False
    profesorados = Profesorados()
    instrumentos = Instrumentos()
    #page.add(profesorados)
    #page.add(instrumentos)
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title=Text("Creador de Resoluciones - APP"), 
                        bgcolor=colors.SURFACE_VARIANT,
                        ),
                    Row([
                        ElevatedButton("Profesorados", on_click=lambda _: page.go("/profesorados")),
                        ElevatedButton("Instrumentos", on_click=lambda _: page.go("/instrumentos"))
                    ]),
                    
                ],
            )
        )
        if page.route == "/profesorados":
            page.views.append(
                View(
                    "/profesorados",
                    [
                        AppBar(
                            leading=IconButton(icons.HOME_SHARP, on_click=lambda _: page.go("/")),
                            title=Text("Profesorados"),
                            bgcolor=colors.SURFACE_VARIANT,
                            ),
                        Column([profesorados])
                    ],
                )
            )
        elif page.route == "/instrumentos":
            page.views.append(
                View(
                    "/instrumentos",
                    [
                        AppBar(
                            leading=IconButton(icons.HOME_SHARP, on_click=lambda _: page.go("/")),
                            title=Text("Instrumentos"),
                            bgcolor=colors.SURFACE_VARIANT
                            ),
                        Column([instrumentos])
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    
flet.app(target=main)