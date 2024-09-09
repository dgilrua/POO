import tkinter as tk
from tkinter import messagebox
import math


class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_superficie(self, superficie):
        self.superficie = superficie

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio**2

    def calcular_superficie(self):
        area_lado_a = 2 * math.pi * self.radio * self.altura
        area_lado_b = 2 * math.pi * self.radio**2
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio**3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio**2


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        volumen = (self.base**2 * self.altura) / 3.0
        return volumen

    def calcular_superficie(self):
        area_base = self.base**2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado


class VentanaCilindro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Cilindro")
        self.geometry("380x210")  # Aumentado el tamaño de la ventana
        self.resizable(False, False)
        self.eval("tk::PlaceWindow . center")

    def inicio(self):
        self.radio = tk.Label(self, text="Radio (cms):")
        self.radio.place(x=20, y=20, width=160, height=23)  # Aumentado el ancho
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=190, y=20, width=160, height=23)  # Aumentado el ancho

        self.altura = tk.Label(self, text="Altura (cms):")
        self.altura.place(x=20, y=50, width=160, height=23)  # Aumentado el ancho
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=190, y=50, width=160, height=23)  # Aumentado el ancho

        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_cilindro)
        self.calcular.place(x=190, y=80, width=160, height=23)  # Aumentado el ancho

        self.volumen = tk.Label(self, text="Volumen (cm3):")
        self.volumen.place(x=20, y=110, width=160, height=23)  # Aumentado el ancho

        self.superficie = tk.Label(self, text="Superficie (cm2):")
        self.superficie.place(x=20, y=140, width=160, height=23)  # Aumentado el ancho

    def calcular_cilindro(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            self.volumen.config(
                text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}"
            )
            self.superficie.config(
                text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de numero")


class VentanaEsfera(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Esfera")
        self.geometry("380x200")  # Aumentado el tamaño de la ventana
        self.resizable(False, False)
        self.eval("tk::PlaceWindow . center")

    def inicio(self):
        self.radio = tk.Label(self, text="Radio (cms):")
        self.radio.place(x=20, y=20, width=160, height=23)  # Aumentado el ancho

        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=190, y=20, width=160, height=23)  # Aumentado el ancho

        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_esfera)
        self.calcular.place(x=190, y=50, width=160, height=23)  # Aumentado el ancho

        self.volumen = tk.Label(self, text="Volumen (cm3):")
        self.volumen.place(x=20, y=90, width=160, height=23)  # Aumentado el ancho

        self.superficie = tk.Label(self, text="Superficie (cm2):")
        self.superficie.place(x=20, y=120, width=160, height=23)  # Aumentado el ancho

    def calcular_esfera(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.volumen.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.superficie.config(
                text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPiramide(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Pirámide")
        self.geometry("380x240")  # Aumentado el tamaño de la ventana
        self.resizable(False, False)
        self.eval("tk::PlaceWindow . center")

    def inicio(self):
        self.base = tk.Label(self, text="Base (cms):")
        self.base.place(x=20, y=20, width=160, height=23)  # Aumentado el ancho
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=190, y=20, width=160, height=23)  # Aumentado el ancho

        self.altura = tk.Label(self, text="Altura (cms):")
        self.altura.place(x=20, y=50, width=160, height=23)  # Aumentado el ancho
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=190, y=50, width=160, height=23)  # Aumentado el ancho

        self.apotema = tk.Label(self, text="Apotema (cms):")
        self.apotema.place(x=20, y=80, width=160, height=23)  # Aumentado el ancho
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=190, y=80, width=160, height=23)  # Aumentado el ancho

        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_piramide)
        self.calcular.place(x=190, y=110, width=160, height=23)  # Aumentado el ancho

        self.volumen = tk.Label(self, text="Volumen (cm3):")
        self.volumen.place(x=20, y=140, width=160, height=23)  # Aumentado el ancho

        self.superficie = tk.Label(self, text="Superficie (cm2):")
        self.superficie.place(x=20, y=170, width=160, height=23)  # Aumentado el ancho

    def calcular_piramide(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())

            piramide = Piramide(base, altura, apotema)

            self.volumen.config(
                text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}"
            )
            self.superficie.config(
                text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Figuras")
        self.geometry("400x160")  # Aumentado el tamaño de la ventana
        self.resizable(False, False)
        self.eval("tk::PlaceWindow . center")

    def inicio(self):
        self.cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.cilindro.place(x=20, y=50, width=120, height=23)  # Aumentado el ancho

        self.esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.esfera.place(x=150, y=50, width=120, height=23)  # Aumentado el ancho

        self.piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        self.piramide.place(x=280, y=50, width=120, height=23)  # Aumentado el ancho

    def abrir_esfera(self):
        esfera = VentanaEsfera()
        esfera.mainloop()

    def abrir_cilindro(self):
        cilindro = VentanaCilindro()
        cilindro.mainloop()

    def abrir_piramide(self):
        piramide = VentanaPiramide()
        piramide.mainloop()


class Principal:
    @staticmethod
    def main():
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.resizable(False, False)
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()