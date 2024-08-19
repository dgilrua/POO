import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Listbox

class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

class ListaPersonas:
    def __init__(self):
        self.lista_personas = []

    def añadir_persona(self, persona):
        self.lista_personas.append(persona)

    def eliminar_persona(self, index):
        if 0 <= index < len(self.lista_personas):
            del self.lista_personas[index]

    def borrar_lista(self):
        self.lista_personas.clear()

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lista = ListaPersonas()
        self.title("Personas")
        self.geometry("270x350")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):

        tk.Label(self, text="Nombre:").place(x=20, y=20)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=105, y=20)

        tk.Label(self, text="Apellidos:").place(x=20, y=50)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=105, y=50)

        tk.Label(self, text="Teléfono:").place(x=20, y=80)
        self.campo_telefono = tk.Entry(self)
        self.campo_telefono.place(x=105, y=80)

        tk.Label(self, text="Dirección:").place(x=20, y=110)
        self.campo_direccion = tk.Entry(self)
        self.campo_direccion.place(x=105, y=110)

  
        tk.Button(self, text="Añadir", command=self.añadir_persona).place(x=105, y=150)
        tk.Button(self, text="Eliminar", command=self.eliminar_persona).place(x=20, y=280)
        tk.Button(self, text="Borrar Lista", command=self.borrar_lista).place(x=120, y=280)

        self.lista_nombres = Listbox(self, selectmode=tk.SINGLE)
        self.scroll_lista = Scrollbar(self, orient=tk.VERTICAL, command=self.lista_nombres.yview)
        self.lista_nombres.config(yscrollcommand=self.scroll_lista.set)
        self.lista_nombres.place(x=20, y=190, width=220, height=80)
        self.scroll_lista.place(x=240, y=190, height=80, width=20)

    def añadir_persona(self):
        nombre = self.campo_nombre.get()
        apellidos = self.campo_apellidos.get()
        telefono = self.campo_telefono.get()
        direccion = self.campo_direccion.get()

        persona = Persona(nombre, apellidos, telefono, direccion)
        self.lista.añadir_persona(persona)
        
        elemento = f"{nombre}-{apellidos}-{telefono}-{direccion}"
        self.lista_nombres.insert(tk.END, elemento)
        self.clear_entries()

    def eliminar_persona(self):
        try:
            selected_index = self.lista_nombres.curselection()[0]
            self.lista.eliminar_persona(selected_index)
            self.lista_nombres.delete(selected_index)
        except IndexError:
            messagebox.showerror("Error", "Debe seleccionar un elemento")

    def borrar_lista(self):
        self.lista.borrar_lista()
        self.lista_nombres.delete(0, tk.END)

    def clear_entries(self):
        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_telefono.delete(0, tk.END)
        self.campo_direccion.delete(0, tk.END)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
