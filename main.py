import flet as ft
from src import EditNoteView

def meta_properties(page: ft.Page):
    page.title = 'Note Taker (powered by flet)'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

def main(page: ft.Page):
    meta_properties(page)
    page.add(EditNoteView())

ft.app(main)
