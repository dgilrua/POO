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
    self.logo_menu = util_img.leer_imagen("actividad_3_parte_2\img\menu.png", (30,30))
    self.escudo_un = util_img.leer_imagen("actividad_3_parte_2\img\escudo_un.png", (350,400))
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
    self.title("Actividad 3 parte 2")
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

    buttons_info = [
        ("Circulo", self.button7, self.punto_7),
        ("Cuadrado", self.button10, self.punto_10),
        ("Rectangulo", self.button18, self.punto_18),
        ("Triangulo", self.button19, self.punto_19),
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
    
    tk.Label(self.cuerpo_principal, text="Informacion de un circulo", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el radio", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.radio = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.radio.pack()
  
    
    tk.Button(self.cuerpo_principal, text="Calcular area", command=self.calcular_area_circulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular perimetro", command=self.calcular_perimetro_circulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado_area_circulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_perimetro_circulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
     
  def calcular_area_circulo(self):
    radio = float(self.radio.get())
    calc = pi*pow(radio,2)
    self.resultado_area_circulo.config(text=f"El área del circulo es: {calc} cm^2")
    self.resultado_area_circulo.pack()
    
  def calcular_perimetro_circulo(self):
    radio = float(self.radio.get())
    calc = 2*pi*radio
    self.resultado_perimetro_circulo.config(text=f"El perímetro del circulo es: {calc} cm")  
    self.resultado_perimetro_circulo.pack()
    
  def punto_10(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Informacion de un cuadrado", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el lado", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.lado = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.lado.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular area", command=self.calcular_area_cuadrado, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular perimetro", command=self.calcular_perimetro_cuadrado, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado_area_cuadrado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_perimetro_cuadrado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
  def calcular_area_cuadrado(self):
    lado = float(self.lado.get())
    calc = pow(lado,2)
    self.resultado_area_cuadrado.config(text=f"El área del cuadrado es: {calc} cm^2")
    self.resultado_area_cuadrado.pack()
    
  def calcular_perimetro_cuadrado(self):
    lado = float(self.lado.get())
    calc = lado*4
    self.resultado_perimetro_cuadrado.config(text=f"El perímetro del cuadrado es: {calc} cm")
    self.resultado_perimetro_cuadrado.pack()

  def punto_18(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Informacion de un rectangulo", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la base", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.base_rectangulo = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.base_rectangulo.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la altura", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.altura_rectangulo = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.altura_rectangulo.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular area", command=self.calcular_area_rectangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular perimetro", command=self.calcular_perimetro_rectangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado_area_rectangulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_perimetro_rectangulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
  def calcular_area_rectangulo(self):
    base = float(self.base_rectangulo.get())
    altura = float(self.altura_rectangulo.get())
    calc = base*altura
    self.resultado_area_rectangulo.config(text=f"El área del rectangulo es: {calc} cm^2")
    self.resultado_area_rectangulo.pack()
    
  def calcular_perimetro_rectangulo(self):
    base = float(self.base_rectangulo.get())
    altura = float(self.altura_rectangulo.get())
    calc = (base*2)+(altura*2)
    self.resultado_perimetro_rectangulo.config(text=f"El perímetro del rectangulo es: {calc} cm")
    self.resultado_perimetro_rectangulo.pack()
    
  
  def punto_19(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Informacion de un triangulo", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la base", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.base_triangulo = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.base_triangulo.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la altura", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.altura_triangulo = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.altura_triangulo.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular el area", command=self.calcular_area_triangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular la hipotenusa", command=self.calcular_hipotenusa, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular el tipo de triangulo", command=self.tipo_triangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    tk.Button(self.cuerpo_principal, text="Calcular el perimetro", command=self.calcular_perimetro_triangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado_area_triangulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_hipotenusa = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_tipo_triangulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    self.resultado_perimetro_triangulo = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )

    
  def calcular_area_triangulo(self):
    base = float(self.base_triangulo.get())
    altura = float(self.altura_triangulo.get())
    calc = (base*altura)/2
    self.resultado_area_triangulo.config(text=f"El área del triangulo es: {calc} cm^2")
    self.resultado_area_triangulo.pack()
    
  def calcular_hipotenusa(self) -> float:
    base = float(self.base_triangulo.get())
    altura = float(self.altura_triangulo.get())
    calc = sqrt(pow(base,2)+pow(altura,2))
    self.resultado_hipotenusa.config(text=f"La hipotenusa del triangulo es: {calc} cm")
    self.resultado_hipotenusa.pack()
    return calc
    
  def calcular_perimetro_triangulo(self):
    base = float(self.base_triangulo.get())
    altura = float(self.altura_triangulo.get())
    hipotenusa = self.calcular_hipotenusa()
    calc = base+altura+hipotenusa
    self.resultado_perimetro_triangulo.config(text=f"El perímetro del triangulo es: {calc} cm")
    self.resultado_perimetro_triangulo.pack()
    
  def tipo_triangulo(self):
    base = float(self.base_triangulo.get())
    altura = float(self.altura_triangulo.get())
    hipotenusa = self.calcular_hipotenusa()
    if base == altura and base == hipotenusa:
      self.resultado_tipo_triangulo.config(text=f"El triangulo es equilatero")
    elif base == altura or base == hipotenusa or altura == hipotenusa:
      self.resultado_tipo_triangulo.config(text=f"El triangulo es isosceles")
    else:
      self.resultado_tipo_triangulo.config(text=f"El triangulo es escaleno")
    self.resultado_tipo_triangulo.pack()
    
  