import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import math

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        t2 = x.derecha

        x.derecha = y
        y.izquierda = t2

        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))

        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        t2 = y.izquierda

        y.izquierda = x
        x.derecha = t2

        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        else:
            return nodo

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        balance = self.balance(nodo)

        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotacion_derecha(nodo)

        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotacion_izquierda(nodo)

        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def buscar(self, valor):
        recorrido = []
        encontrado = self._buscar(self.raiz, valor, recorrido)
        return encontrado, recorrido

    def _buscar(self, nodo, valor, recorrido):
        if nodo is None:
            return False

        recorrido.append(nodo.valor)

        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor, recorrido)

        return self._buscar(nodo.derecha, valor, recorrido)

    def minimo(self, nodo):
        actual = nodo

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)

        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)

        else:
            if nodo.izquierda is None:
                return nodo.derecha

            elif nodo.derecha is None:
                return nodo.izquierda

            temp = self.minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)

        if nodo is None:
            return nodo

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        balance = self.balance(nodo)

        if balance > 1 and self.balance(nodo.izquierda) >= 0:
            return self.rotacion_derecha(nodo)

        if balance > 1 and self.balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        if balance < -1 and self.balance(nodo.derecha) <= 0:
            return self.rotacion_izquierda(nodo)

        if balance < -1 and self.balance(nodo.derecha) > 0:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierda, resultado)
            self._postorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    def contar_nodos(self):
        return self._contar(self.raiz)

    def _contar(self, nodo):
        if nodo is None:
            return 0

        return 1 + self._contar(nodo.izquierda) + self._contar(nodo.derecha)

    def obtener_lista(self):
        return self.preorden()

    def cargar_desde_lista(self, lista):
        self.raiz = None

        for valor in lista:
            self.insertar(valor)

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Software Educativo - Árboles AVL")
        self.root.geometry("1300x750")
        self.root.configure(bg="black")

        self.arbol = ArbolAVL()

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.root,
            text="SOFTWARE EDUCATIVO DE ÁRBOLES AVL",
            font=("Arial", 22, "bold"),
            bg="black",
            fg="white",
            pady=10
        )
        titulo.pack(fill=tk.X)

        panel = tk.Frame(self.root, bg="black", pady=10)
        panel.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(panel, text="OPERACIONES", bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(panel, text="Insertar", command=self.insertar, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Buscar", command=self.buscar, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Eliminar", command=self.eliminar, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Preorden", command=self.mostrar_preorden, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Inorden", command=self.mostrar_inorden, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Postorden", command=self.mostrar_postorden, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Guardar", command=self.guardar_arbol, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        tk.Button(panel, text="Cargar", command=self.cargar_arbol, bg="#00BFFF", fg="black", width=15, height=2).pack(side=tk.LEFT, padx=5)

        contenedor = tk.Frame(self.root)
        contenedor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(contenedor, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        panel_info = tk.Frame(contenedor, width=300, bg="black")
        panel_info.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(
            panel_info,
            text="INFORMACIÓN",
            font=("Arial", 16, "bold"),
            bg="black",
            fg="#00BFFF",
            pady=10
        ).pack(fill=tk.X)

        self.info = tk.Label(
            panel_info,
            text="",
            justify=tk.LEFT,
            anchor="nw",
            font=("Arial", 12),
            bg="black"
        )
        self.info.pack(fill=tk.BOTH, padx=10, pady=10)

        tk.Label(
            panel_info,
            text="HISTORIAL",
            font=("Arial", 14, "bold"),
            bg="black",
            fg="#00BFFF",
            pady=5
        ).pack(fill=tk.X)

        self.historial = tk.Text(panel_info, height=20, font=("Consolas", 10), bg="#111111", fg="#00FF99")
        self.historial.pack(fill=tk.BOTH, padx=10, pady=10)

        self.actualizar_info()

    def obtener_valor(self):
        try:
            valor = tk.simpledialog.askinteger("Ingresar valor", "Ingrese un número:")
            return valor
        except:
            messagebox.showerror("Error", "Ingrese un número válido")
            return None

    def insertar(self):
        valor = self.obtener_valor()

        if valor is not None:
            self.arbol.insertar(valor)
            self.registrar(f"Insertado: {valor}")
            self.dibujar_arbol()
            self.actualizar_info()

    def buscar(self):
        valor = self.obtener_valor()

        if valor is not None:
            encontrado, recorrido = self.arbol.buscar(valor)

            self.registrar(f"Búsqueda de {valor}: {'Encontrado' if encontrado else 'No encontrado'}")
            self.registrar(f"Recorrido: {recorrido}")

            if encontrado:
                messagebox.showinfo("Resultado", f"Valor {valor} encontrado")
            else:
                messagebox.showwarning("Resultado", f"Valor {valor} no encontrado")

    def eliminar(self):
        valor = self.obtener_valor()

        if valor is not None:
            self.arbol.eliminar(valor)
            self.registrar(f"Eliminado: {valor}")
            self.dibujar_arbol()
            self.actualizar_info()

    def mostrar_preorden(self):
        recorrido = self.arbol.preorden()
        self.registrar(f"Preorden: {recorrido}")
        messagebox.showinfo("Preorden", str(recorrido))

    def mostrar_inorden(self):
        recorrido = self.arbol.inorden()
        self.registrar(f"Inorden: {recorrido}")
        messagebox.showinfo("Inorden", str(recorrido))

    def mostrar_postorden(self):
        recorrido = self.arbol.postorden()
        self.registrar(f"Postorden: {recorrido}")
        messagebox.showinfo("Postorden", str(recorrido))

    def dibujar_arbol(self):
        self.canvas.delete("all")

        if self.arbol.raiz:
            ancho = self.canvas.winfo_width()
            self.dibujar_nodo(self.arbol.raiz, ancho / 2, 50, ancho / 4)

    def dibujar_nodo(self, nodo, x, y, espacio):
        if nodo is None:
            return

        radio = 20

        if nodo.izquierda:
            nx = x - espacio
            ny = y + 80

            self.canvas.create_line(x, y, nx, ny, width=2)
            self.dibujar_nodo(nodo.izquierda, nx, ny, espacio / 2)

        if nodo.derecha:
            nx = x + espacio
            ny = y + 80

            self.canvas.create_line(x, y, nx, ny, width=2)
            self.dibujar_nodo(nodo.derecha, nx, ny, espacio / 2)

        self.canvas.create_oval(
            x - radio,
            y - radio,
            x + radio,
            y + radio,
            fill="#00BFFF",
            outline="white",
            width=2
        )

        self.canvas.create_text(
            x,
            y,
            text=str(nodo.valor),
            font=("Arial", 11, "bold")
        )

    def actualizar_info(self):
        raiz = self.arbol.raiz.valor if self.arbol.raiz else "Vacío"
        altura = self.arbol.altura(self.arbol.raiz)
        cantidad = self.arbol.contar_nodos()

        texto = (
            f"Tipo de Árbol: AVL\n\n"
            f"Raíz: {raiz}\n\n"
            f"Altura: {altura}\n\n"
            f"Cantidad de nodos: {cantidad}\n"
        )

        self.info.config(text=texto)

    def registrar(self, mensaje):
        self.historial.insert(tk.END, mensaje + "\n")
        self.historial.see(tk.END)

    def guardar_arbol(self):
        archivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json")]
        )

        if archivo:
            datos = {
                "valores": self.arbol.obtener_lista()
            }

            with open(archivo, "w") as f:
                json.dump(datos, f)

            messagebox.showinfo("Guardar", "Árbol guardado correctamente")

    def cargar_arbol(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("JSON", "*.json")]
        )

        if archivo:
            with open(archivo, "r") as f:
                datos = json.load(f)

            self.arbol.cargar_desde_lista(datos["valores"])
            self.dibujar_arbol()
            self.actualizar_info()

            messagebox.showinfo("Cargar", "Árbol cargado correctamente")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)

    root.after(500, app.dibujar_arbol)

    root.mainloop()
