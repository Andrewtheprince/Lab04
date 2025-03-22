import flet as ft
from flet.core.types import MainAxisAlignment


class View(object):
    def __init__(self, page: ft.Page):
        self._btnAvvia = None
        self._txtIn = None
        self._tendinaModalita = None
        self._txtOut = None
        self._row1 = None
        self._tendinaLingua = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        self._tendinaLingua = ft.Dropdown(label="Selezionare lingua", width=600, options=[ft.dropdown.Option("italian"), ft.dropdown.Option("english"), ft.dropdown.Option("spanish")],
                                          on_change= lambda e: self.__controller.handleLinguaSelezionata(e)
                                          )
        row1 = ft.Row(controls=[self._tendinaLingua], alignment=ft.MainAxisAlignment.START)
        self._tendinaModalita = ft.Dropdown(label="Modalita ricerca", width=150, options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")],
                                            on_change=lambda e: self.__controller.handleModalitaSelezionata(e)
                                            )
        self._txtIn = ft.TextField(label="Inserire testo", width=300)
        self._btnAvvia = ft.ElevatedButton("Avvia controllo", on_click=self.__controller.handleSpellCheck, width=130)
        row2 = ft.Row(controls=[self._tendinaModalita, self._txtIn, self._btnAvvia], alignment=MainAxisAlignment.START, spacing=10)

        self._txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        row3 = ft.Row(controls=[self._txtOut], alignment=ft.MainAxisAlignment.START)
        self.page.add(row1, row2, row3)
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self.page.update()
