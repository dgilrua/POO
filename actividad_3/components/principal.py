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
    self.escudo_un = util_img.leer_imagen("actividad_3\img\escudo_un.png", (350,400))
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
    
    tk.Label(self.cuerpo_principal, text="Numero mayor entre 2", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el primer numero", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.numero1 = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.numero1.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el segundo numero", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.numero2 = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.numero2.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.calcular_numero_mayor, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
     
  def calcular_numero_mayor(self):
      try:
        numero1 = int(self.numero1.get())
        numero2 = int(self.numero2.get())
        if numero1 > numero2:
          self.resultado.config(text=f"El numero mayor es {numero1}")
        elif numero2 > numero1:
          self.resultado.config(text=f"El numero mayor es {numero2}")
        else:
          self.resultado.config(text=f"Los numeros son iguales")
      except ValueError:
        self.resultado.config(text="Ingrese un numero valido")
      self.resultado.pack()  
    
  def punto_10(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Precio de la matricula", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el numero de matricula", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.num = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.num.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el nombre del estudiante", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.nom = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.nom.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el patrimonio del estudiante", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.pat = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.pat.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el estrato del estudiante", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.estrato = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.estrato.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.precio_matricula, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
  def precio_matricula(self):
    try: 
      num = self.num.get()
      nom = self.nom.get()
      pat = int(self.pat.get())
      estrato = int(self.estrato.get())
      precio_matricula = 50000
      
      if pat > 2000000 and estrato > 3:
        precio_matricula = precio_matricula + 0.03*pat
      self.resultado.config(text=f"El número de matrícula es: {num}\nEl nombre del estudiante es: {nom}\nEl precio de la matrícula que debe pagar el estudiante es: $ {precio_matricula}")
    except ValueError:
      self.resultado.config(text="Los campos no pueden estar vacios")
    self.resultado.pack()

  def punto_18(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Salarios de un empleado", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el código del empleado", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.cod = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.cod.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el nombre del empleado", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.nom = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.nom.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la cantidad de horas trabajadas en el mes", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.htm = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.htm.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el valor de la hora trabajada", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.ht = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.ht.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese la retención en la fuente", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.rf = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.rf.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.calcular_salario, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
    
  def calcular_salario(self):
    try:
      cod = self.cod.get()
      nom = self.nom.get()
      htm = int(self.htm.get())
      ht = int(self.ht.get())
      rf = float(self.rf.get())
      
      sb = htm * ht
      sn = sb - (sb * rf)
      self.resultado.config(text=f"El código del empleado es: {cod}\nEl nombre del empleado es: {nom}\nEl salario bruto es: $ {sb}\nEl salario neto es: $ {sn}")
    except ValueError:
      self.resultado.config(text="Los campos no pueden estar vacios")
    self.resultado.pack()
  
  def punto_19(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Informacion de un triangulo", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el lado del triangulo", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.lado = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.lado.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.informacion_triangulo, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )

    
  def informacion_triangulo(self):
    try:
      lado = float(self.lado.get())
      altura = (sqrt(3) / 2) * lado
      perimetro = lado * 3
      area = (lado * altura) / 2
      
      self.resultado.config(text=f"La altura es: {altura} cm\nEl perímetro es: {perimetro} cm\nEl área es: {area} cm^2")
    except ValueError:
      self.resultado.config(text="Ingrese un número válido")
    self.resultado.pack()
  
  def punto_22(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Informacion deacuerdo a salario", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el nombre del empleado", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.nombre = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.nombre.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el precio por hora", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.precio_hora = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.precio_hora.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese las horas trabajadas", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.horas = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.horas.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.filtrar_informacion, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
        
  def filtrar_informacion(self):
    try:
      nombre = self.nombre.get()
      precio_hora = float(self.precio_hora.get())
      horas = float(self.horas.get())
      
      salario = precio_hora * horas
      
      if salario >= 4500000:
        self.resultado.config(text=f"Nombre: {nombre}\nSalario: {salario}")
        
      else:
        self.resultado.config(text=f"Nombre: {nombre}")  
        
    except ValueError:
      self.resultado.config(text="Ingrese un número válido")
      
    self.resultado.pack()
  
  def punto_23(self):
    self.limpiar_cuerpo_principal()
      
    tk.Label(self.cuerpo_principal, text="Solucion ecuacion segundo grado", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el valor de a", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.a = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.a.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el valor de b", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.b = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.b.pack()
    
    tk.Label(self.cuerpo_principal, text="Ingrese el valor de c", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL ).pack()
    self.c = tk.Entry(self.cuerpo_principal ,font=("Roboto", 15))
    self.c.pack()
    
    tk.Button(self.cuerpo_principal, text="Calcular", command=self.solucion_ecn_segundo_grado, font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL).pack()
    
    self.resultado = tk.Label(self.cuerpo_principal, text="", pady=20 ,font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL )
    
  def solucion_ecn_segundo_grado(self):
    
    try:
      a = float(self.a.get())
      b = float(self.b.get())
      c = float(self.c.get())
    
      discriminante = b**2 - 4*a*c
      if discriminante > 0:
        x1 = (-b + sqrt(discriminante)) / (2*a)
        x2 = (-b - sqrt(discriminante)) / (2*a)
        self.resultado.config(text=f"Las soluciones son: {x1} y {x2}")
        
      elif discriminante == 0:
        x = -b / (2*a)
        self.resultado.config(text=f"La solución es: {x}")
        
      else:
        self.resultado.config(text="No tiene solución en los numeros reales")
        
    except ValueError:
      self.resultado.config(text="Ingrese un número válido")
    
    self.resultado.pack()
    
  