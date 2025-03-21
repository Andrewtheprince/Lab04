import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
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
                   alignment=ft.MainAxisAlignment.CENTER)
        )

        # Add your stuff here

        self._tendinaLingua = ft.Dropdown(label="Selezionare lingua", width=500, options=[ft.dropdown.Option("Italiano"), ft.dropdown.Option("Inglese"), ft.dropdown.Option("Spagnolo")])
        self._row1 = ft.Row(controls=[self._tendinaLingua], alignment=ft.MainAxisAlignment.CENTER)





        self.page.add(self._row1)

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

