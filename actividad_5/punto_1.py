import math
import tkinter as tk
from tkinter import messagebox


class Notas:
    def __init__(self):

        self.listaNotas = [0.0] * 5

    def calcular_promedio(self):
        suma = 0
        for i in range(1, len(self.listaNotas)):
            suma += self.listaNotas[i]
        return suma / len(self.listaNotas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += (self.listaNotas[i] - prom) ** 2
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        menor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] < menor:
                menor = self.listaNotas[i]
        return menor

    def calcular_mayor(self):
        mayor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] > mayor:
                mayor = self.listaNotas[i]
        return mayor


class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcular_promedio(self):
        suma = sum(self.listaNotas[1:])
        return suma / len(self.listaNotas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((nota - prom) ** 2 for nota in self.listaNotas)
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        return min(self.listaNotas)

    def calcular_mayor(self):
        return max(self.listaNotas)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        self.labels = []
        self.entries = []

        for i in range(5):
            label = tk.Label(self, text=f"Nota {i+1}:")
            label.place(x=20, y=20 + i * 30)
            self.labels.append(label)

            entry = tk.Entry(self)
            entry.place(x=105, y=20 + i * 30, width=135)
            self.entries.append(entry)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=20, y=170, width=100)

        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=125, y=170, width=80)

        self.promedio_label = tk.Label(self, text="Promedio = ")
        self.promedio_label.place(x=20, y=210)

        self.desviacion_label = tk.Label(self, text="Desviación = ")
        self.desviacion_label.place(x=20, y=240)

        self.mayor_label = tk.Label(self, text="Nota mayor = ")
        self.mayor_label.place(x=20, y=270)

        self.menor_label = tk.Label(self, text="Nota menor = ")
        self.menor_label.place(x=20, y=300)

    def calcular(self):
        notas = Notas()
        try:
            for i in range(5):
                notas.listaNotas[i] = float(self.entries[i].get())

            prom = notas.calcular_promedio()
            desv = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()

            self.promedio_label.config(text=f"Promedio = {prom:.2f}")
            self.desviacion_label.config(text=f"Desviación estándar = {desv:.2f}")
            self.mayor_label.config(text=f"Valor mayor = {mayor}")
            self.menor_label.config(text=f"Valor menor = {menor}")
        except ValueError:
            messagebox.showerror(
                "Error", "Por favor, ingrese valores numéricos válidos."
            )

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
