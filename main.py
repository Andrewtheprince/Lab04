import flet as ft

from controller import SpellChecker
from view import View


def main(page: ft.Page):
    # Setup model, view, control according to MVC pattern
    v = View(page)
    c = SpellChecker(v)
    v.setController(c)
    v.add_content()

ft.app(target=main)