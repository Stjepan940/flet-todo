import flet as ft

def main(page: ft.Page):
    page.title = "Aplikacija za biljeske"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tasks = ft.Column()

    def add_clicked(e):
        tasks.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Dodaj bilješku", width=300)
    add_button = ft.ElevatedButton("Add", on_click=add_clicked)
    page.add(ft.Row([new_task, add_button], alignment=ft.MainAxisAlignment.CENTER), tasks)

ft.app(target=main, view=ft.WEB_BROWSER, port=10000)
