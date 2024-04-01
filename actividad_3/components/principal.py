import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.window_config as window_config
import util.util_image as util_img
from math import pi, pow, sqrt
import numpy as np

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.logo_menu = util_img.leer_imagen("actividad_3\img\menu.png", (30,30))
    self.escudo_un = util_img.leer_imagen("actividad_3\img\escudo_un.png", (400,400))
    self.config_window()
    self.paneles()
    self.controles_barra_superior() 
    self.controles_menu_lateral()
    self.controles_cuerpo()
    self.informacion_inicial()
    self.bind_hover_events(self.buttonTitle)
    self.bind_hover_events(self.buttonMenuLateral)
    
  def config_window(self):
    #Configuracion ventana
    self.title("Actividad 3")
    w,h= 1280, 720
    window_config.centrar_ventana(self,w,h)
    
  def paneles(self):
    self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
    self.barra_superior.pack(side=tk.TOP, fill='both')      
    
    self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=250)
    self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
    
    self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, pady=30)
    self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
  def controles_barra_superior(self):
    # Configuración de la barra superior
    font_awesome = font.Font(family='FontAwesome', size=12)
    
    self.buttonMenuLateral = tk.Button(self.barra_superior, image=self.logo_menu ,font=font_awesome, command=self.toggle_panel,
                                        bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", padx=10, cursor="hand1")
    self.buttonMenuLateral.pack(side=tk.LEFT)

    self.buttonTitle = tk.Button(self.barra_superior, text="Programacion orientada a objetos", fg="white", cursor="hand1")
    self.buttonTitle.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=30, bd=0, command=self.informacion_inicial)
    self.buttonTitle.pack(side=tk.LEFT)


    self.labelTitulo = tk.Label(self.barra_superior, text="Universidad nacional de colombia")
    self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=30)
    self.labelTitulo.pack(side=tk.RIGHT)
    
  def controles_menu_lateral(self):
    # Configuración del menú lateral
    ancho_menu = 20
    alto_menu = 2
    font_awesome = font.Font(family='FontAwesome', size=15)
    
    self.button7 = tk.Button(self.menu_lateral)        
    self.button10 = tk.Button(self.menu_lateral)        
    self.button18 = tk.Button(self.menu_lateral)
    self.button19 = tk.Button(self.menu_lateral)        
    self.button22 = tk.Button(self.menu_lateral)
    self.button23 = tk.Button(self.menu_lateral)

    buttons_info = [
        ("Punto 7", self.button7, self.punto_7),
        ("Punto 10", self.button10, self.punto_10),
        ("Punto 18", self.button18, self.punto_18),
        ("Punto 19", self.button19, self.punto_19),
        ("Punto 22", self.button22, self.punto_22),
        ("Punto 23", self.button23, self.punto_23)
    ]

    for text, button, action in buttons_info:
        self.configurar_boton_menu(button, text,font_awesome, ancho_menu, alto_menu, action)  
        
  def informacion_inicial(self):
    # Información inicial en el cuerpo principal
    self.limpiar_cuerpo_principal()
    label = tk.Label(self.cuerpo_principal, image=self.escudo_un, bg=COLOR_CUERPO_PRINCIPAL)
    label.pack(side=tk.TOP)
    label = tk.Label(self.cuerpo_principal, text="\nUniversidad Nacional de Colombia\n\nProgramación Orientada a Objetos - Actividad 3\n\n Daniel Esteban Alvarez - David Gil Rua", bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 20))
    label.pack(side=tk.TOP)                  
    
  def controles_cuerpo(self):
      # Imagen en el cuerpo principal
      label = tk.Label(self.cuerpo_principal,
                        bg=COLOR_CUERPO_PRINCIPAL)
      label.place(x=0, y=0, relwidth=1, relheight=1)
      
  def configurar_boton_menu(self, button, text, font_awesome, ancho_menu, alto_menu, action):
        button.config(text=f"{text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, command=action, padx=10) 
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

  def bind_hover_events(self, button):
      # Asociar eventos Enter y Leave con la función dinámica
      button.bind("<Enter>", lambda event: self.on_enter(event, button))
      button.bind("<Leave>", lambda event: self.on_leave(event, button))

  def on_enter(self, event, button):
      # Cambiar estilo al pasar el ratón por encima
      button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

  def on_leave(self, event, button):
      # Restaurar estilo al salir el ratón
      button.config(bg=COLOR_MENU_LATERAL, fg='white')

  def toggle_panel(self):
      # Alternar visibilidad del menú lateral
      if self.menu_lateral.winfo_ismapped():
          self.menu_lateral.pack_forget()
      else:
          self.menu_lateral.pack(side=tk.LEFT, fill='y')
          
  def limpiar_cuerpo_principal(self):
    for widget in self.cuerpo_principal.winfo_children():
      widget.destroy()        
  
  def punto_7(self):
    self.limpiar_cuerpo_principal()
    
    # Columna 1: Etiqueta y botón
    etiqueta_columna_1 = tk.Label(self.cuerpo_principal, text="Columna 1")
    etiqueta_columna_1.grid(row=0, column=1, sticky=tk.W)

    boton_columna_1 = tk.Button(self.cuerpo_principal, text="Botón 1")
    boton_columna_1.grid(row=1, column=0, sticky=tk.W)

    # Columna 2: Entrada de texto y lista
    entrada_columna_2 = tk.Entry(self.cuerpo_principal)
    entrada_columna_2.grid(row=0, column=0, sticky=tk.E)

    lista_columna_2 = tk.Listbox(self.cuerpo_principal)
    lista_columna_2.grid(row=1, column=1, sticky=tk.E)
    
    tk.Label(self.cuerpo_principal, text="Primer punto", font=("Roboto", 20)).pack()
    
    self.cuerpo_principal.config(bg=COLOR_CUERPO_PRINCIPAL, padx=350)
    
  def punto_10(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Segundo punto").pack(side=tk.TOP)
    
  def punto_18(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Tercer punto").pack(side=tk.TOP)
  
  def punto_19(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Cuarto punto").pack(side=tk.TOP)
  
  def punto_22(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Quinto punto").pack(side=tk.TOP)
  
  def punto_23(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Sexto punto").pack(side=tk.TOP)
    
  