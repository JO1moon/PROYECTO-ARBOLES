import flet as ft
import time


LOGO_URL = "Captura de pantalla 2026-05-14 213848.png"


def main(page: ft.Page):

    page.title = "Tutorial de Árboles"
    page.window_width = 900
    page.window_height = 700
    page.window_resizable = False
    page.bgcolor = "#F5F5F5"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    botones_nodos = {}

    recorrido_texto = ft.Text(
        "",
        size=24,
        weight="bold",
        color="black"
    )

    def reproducir_sonido():

        try:
            audio = ft.Audio(
                src="https://www.soundjay.com/buttons/sounds/button-09.mp3",
                autoplay=True
            )

            page.overlay.append(audio)
            page.update()

        except:
            pass

    def crear_nodo(valor):

        texto = ft.Text(
            valor,
            size=22,
            weight="bold",
            color="white"
        )

        nodo = ft.Container(
            content=ft.Column(
                [texto],
                alignment="center",
                horizontal_alignment="center"
            ),

            width=70,
            height=70,

            bgcolor="blue",

            border_radius=50
        )

        botones_nodos[valor] = nodo

        return nodo

    def dibujar_arbol():

        botones_nodos.clear()

        A = crear_nodo("A")
        B = crear_nodo("B")
        C = crear_nodo("C")
        D = crear_nodo("D")
        E = crear_nodo("E")
        F = crear_nodo("F")
        G = crear_nodo("G")

        return ft.Column(

            [
                ft.Row(
                    [A],
                    alignment="center"
                ),

                ft.Row(
                    [
                        ft.Container(width=100),
                        B,
                        ft.Container(width=140),
                        C
                    ],
                    alignment="center"
                ),

                ft.Row(
                    [
                        D,
                        ft.Container(width=40),
                        E,
                        ft.Container(width=80),
                        F,
                        ft.Container(width=40),
                        G
                    ],
                    alignment="center"
                )
            ],

            spacing=35,

            horizontal_alignment="center"
        )

    def animar(lista, titulo):

        recorrido = []

        for nodo in botones_nodos.values():
            nodo.bgcolor = "blue"

        page.update()

        for letra in lista:

            reproducir_sonido()

            botones_nodos[letra].bgcolor = "red"

            recorrido.append(letra)

            recorrido_texto.value = (
                titulo + ": " + " → ".join(recorrido)
            )

            page.update()

            time.sleep(1)

            botones_nodos[letra].bgcolor = "green"

            page.update()

    def pantalla(
        titulo,
        descripcion,
        color,
        recorrido
    ):

        page.clean()

        arbol = dibujar_arbol()

        page.add(

            ft.Column(

                [
                    ft.Text(
                        titulo,
                        size=36,
                        weight="bold",
                        color=color
                    ),

                    ft.Text(
                        descripcion,
                        size=22,
                        color="black"
                    ),

                    ft.Container(height=20),

                    arbol,

                    ft.Container(height=30),

                    recorrido_texto,

                    ft.Container(height=20),

                    ft.Row(

                        [
                            ft.ElevatedButton(
                                "INICIAR RECORRIDO",

                                width=220,
                                height=50,

                                bgcolor=color,
                                color="white",

                                on_click=lambda e:
                                animar(recorrido, titulo)
                            ),

                            ft.ElevatedButton(
                                "REGRESAR",

                                width=180,
                                height=50,

                                bgcolor="black",
                                color="white",

                                on_click=menu_principal
                            )
                        ],

                        alignment="center"
                    )
                ],

                horizontal_alignment="center"
            )
        )

        page.update()

    def inorder(e):

        pantalla(
            "INORDER",
            "Izquierdo → Raíz → Derecho",
            "blue",
            ["D", "B", "E", "A", "F", "C", "G"]
        )

    def preorder(e):

        pantalla(
            "PREORDER",
            "Raíz → Izquierdo → Derecho",
            "green",
            ["A", "B", "D", "E", "C", "F", "G"]
        )

    def postorder(e):

        pantalla(
            "POSTORDER",
            "Izquierdo → Derecho → Raíz",
            "red",
            ["D", "E", "B", "F", "G", "C", "A"]
        )

    def menu_principal(e=None):

        page.clean()

        page.add(

            ft.Column(

                [
                    ft.Image(
                        src=LOGO_URL,
                        width=220,
                        height=220
                    ),

                    ft.Text(
                        "TUTORIAL DE ÁRBOLES",
                        size=34,
                        weight="bold",
                        color="black"
                    ),

                    ft.Container(height=20),

                    ft.ElevatedButton(
                        "INORDER",

                        width=260,
                        height=55,

                        bgcolor="blue",
                        color="white",

                        on_click=inorder
                    ),

                    ft.ElevatedButton(
                        "PREORDER",

                        width=260,
                        height=55,

                        bgcolor="green",
                        color="white",

                        on_click=preorder
                    ),

                    ft.ElevatedButton(
                        "POSTORDER",

                        width=260,
                        height=55,

                        bgcolor="red",
                        color="white",

                        on_click=postorder
                    )
                ],

                horizontal_alignment="center",
                alignment="center"
            )
        )

        page.update()

    page.add(

        ft.Column(

            [
                ft.Image(
                    src=LOGO_URL,
                    width=250,
                    height=250
                ),

                ft.ProgressRing(),

                ft.Text(
                    "CARGANDO...",
                    size=24,
                    weight="bold",
                    color="black"
                )
            ],

            horizontal_alignment="center",
            alignment="center"
        )
    )

    page.update()

    time.sleep(10)

    menu_principal()

ft.app(
    target=main,
    assets_dir="assets"
)