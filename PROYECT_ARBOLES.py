import flet as ft

def main(page: ft.Page):
    page.title = "TUTORIAL DE ÁRBOLES"
    page.bgcolor = "white"
    page.window_width = 500
    page.window_height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def menu_principal(e=None):
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "MENÚ PRINCIPAL",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="black"
                    ),

                    ft.ElevatedButton(
                        "INORDER",
                        width=200,
                        on_click=inorder
                    ),

                    ft.ElevatedButton(
                        "PREORDER",
                        width=200,
                        on_click=preorder
                    ),

                    ft.ElevatedButton(
                        "POSTORDER",
                        width=200,
                        on_click=postorder
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def inorder(e):
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "INORDER",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="blue"
                    ),

                    ft.Text(
                        "Izquierdo → Raíz → Derecho",
                        size=20,
                        color="black"
                    ),

                    ft.ElevatedButton(
                        "REGRESAR",
                        on_click=menu_principal
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def preorder(e):
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "PREORDER",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="green"
                    ),

                    ft.Text(
                        "Raíz → Izquierdo → Derecho",
                        size=20,
                        color="black"
                    ),

                    ft.ElevatedButton(
                        "REGRESAR",
                        on_click=menu_principal
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def postorder(e):
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "POSTORDER",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="red"
                    ),

                    ft.Text(
                        "Izquierdo → Derecho → Raíz",
                        size=20,
                        color="black"
                    ),

                    ft.ElevatedButton(
                        "REGRESAR",
                        on_click=menu_principal
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    menu_principal()

ft.app(target=main)
# hola