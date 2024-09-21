import tkinter as tk
from tkinter import messagebox, simpledialog


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre},{self.telefono},{self.email}"


class GestorContactos:
    def __init__(self, archivo="contactos.txt"):
        self.archivo = archivo
        self.contactos = []
        self.cargar_contactos()

    def cargar_contactos(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, telefono, email = linea.strip().split(",")
                    self.contactos.append(Contacto(nombre, telefono, email))
        except FileNotFoundError:
            pass

    def guardar_contactos(self):
        with open(self.archivo, "w") as f:
            for contacto in self.contactos:
                f.write(f"{contacto}\n")

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        self.guardar_contactos()

    def eliminar_contacto(self, indice):
        del self.contactos[indice]
        self.guardar_contactos()

    def actualizar_contacto(self, indice, contacto):
        self.contactos[indice] = contacto
        self.guardar_contactos()


class AplicacionContactos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Contactos")
        self.geometry("400x300")
        self.gestor = GestorContactos()
        self.crear_widgets()

    def crear_widgets(self):
        self.lista_contactos = tk.Listbox(self, width=50)
        self.lista_contactos.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_contacto).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_contacto).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(
            frame_botones, text="Actualizar", command=self.actualizar_contacto
        ).pack(side=tk.LEFT, padx=5)

        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_contactos.delete(0, tk.END)
        for contacto in self.gestor.contactos:
            self.lista_contactos.insert(
                tk.END, f"{contacto.nombre} - {contacto.telefono} - {contacto.email}"
            )

    def agregar_contacto(self):
        nombre = simpledialog.askstring("Agregar Contacto", "Nombre:")
        if nombre:
            telefono = simpledialog.askstring("Agregar Contacto", "Teléfono:")
            email = simpledialog.askstring("Agregar Contacto", "Email:")
            nuevo_contacto = Contacto(nombre, telefono, email)
            self.gestor.agregar_contacto(nuevo_contacto)
            self.actualizar_lista()

    def eliminar_contacto(self):
        seleccion = self.lista_contactos.curselection()
        if seleccion:
            indice = seleccion[0]
            self.gestor.eliminar_contacto(indice)
            self.actualizar_lista()
        else:
            messagebox.showwarning(
                "Eliminar Contacto", "Por favor, seleccione un contacto para eliminar."
            )

    def actualizar_contacto(self):
        seleccion = self.lista_contactos.curselection()
        if seleccion:
            indice = seleccion[0]
            contacto_actual = self.gestor.contactos[indice]
            nombre = simpledialog.askstring(
                "Actualizar Contacto", "Nombre:", initialvalue=contacto_actual.nombre
            )
            if nombre:
                telefono = simpledialog.askstring(
                    "Actualizar Contacto",
                    "Teléfono:",
                    initialvalue=contacto_actual.telefono,
                )
                email = simpledialog.askstring(
                    "Actualizar Contacto", "Email:", initialvalue=contacto_actual.email
                )
                contacto_actualizado = Contacto(nombre, telefono, email)
                self.gestor.actualizar_contacto(indice, contacto_actualizado)
                self.actualizar_lista()
        else:
            messagebox.showwarning(
                "Actualizar Contacto",
                "Por favor, seleccione un contacto para actualizar.",
            )


if __name__ == "__main__":
    app = AplicacionContactos()
    app.mainloop()
