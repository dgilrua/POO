from typing import List

class Equipo:
    total_tiempo = 0.0

    def __init__(self, nombre: str, país: str):
        self.nombre = nombre
        self.país = país
        Equipo.total_tiempo = 0
        self.lista_ciclistas = []

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_país(self) -> str:
        return self.país

    def set_país(self, país: str):
        self.país = país

    def anadir_ciclista(self, ciclista):
        self.lista_ciclistas.append(ciclista)

    def listar_equipo(self):
        for ciclista in self.lista_ciclistas:
            print(ciclista.get_nombre())

    def buscar_ciclista(self):
        nombre_ciclista = input()
        for ciclista in self.lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                print(ciclista.get_nombre())

    def calcular_total_tiempo(self):
        for ciclista in self.lista_ciclistas:
            Equipo.total_tiempo += ciclista.get_tiempo_acumulado()

    def imprimir(self):
        print(f"Nombre del equipo = {self.nombre}")
        print(f"País = {self.país}")
        print(f"Total tiempo del equipo = {Equipo.total_tiempo}")

from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador: int, nombre: str):
        self._identificador = identificador
        self._nombre = nombre
        self._tiempo_acumulado = 0

    @abstractmethod
    def imprimir_tipo(self) -> str:
        pass

    def get_identificador(self) -> int:
        return self._identificador

    def set_identificador(self, identificador: int):
        self._identificador = identificador

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_tiempo_acumulado(self) -> int:
        return self._tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo_acumulado: int):
        self._tiempo_acumulado = tiempo_acumulado

    def imprimir(self):
        print(f"Identificador = {self._identificador}")
        print(f"Nombre = {self._nombre}")
        print(f"Tiempo Acumulado = {self._tiempo_acumulado}")

class Velocista(Ciclista):
    def __init__(self, identificador: int, nombre: str, potencia_promedio: float, velocidad_promedio: float):
        super().__init__(identificador, nombre)
        self._potencia_promedio = potencia_promedio
        self._velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self) -> float:
        return self._potencia_promedio

    def set_potencia_promedio(self, potencia_promedio: float):
        self._potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self) -> float:
        return self._velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio: float):
        self._velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio = {self._potencia_promedio}")
        print(f"Velocidad promedio = {self._velocidad_promedio}")

    def imprimir_tipo(self) -> str:
        return "Es un velocista"

class Escalador(Ciclista):
    def __init__(self, identificador: int, nombre: str, aceleracion_promedio: float, grado_rampa: float):
        super().__init__(identificador, nombre)
        self._aceleracion_promedio = aceleracion_promedio
        self._grado_rampa = grado_rampa

    def get_aceleracion_promedio(self) -> float:
        return self._aceleracion_promedio

    def set_aceleracion_promedio(self, aceleracion_promedio: float):
        self._aceleracion_promedio = aceleracion_promedio

    def get_grado_rampa(self) -> float:
        return self._grado_rampa

    def set_grado_rampa(self, grado_rampa: float):
        self._grado_rampa = grado_rampa

    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio = {self._aceleracion_promedio}")
        print(f"Grado de rampa = {self._grado_rampa}")

    def imprimir_tipo(self) -> str:
        return "Es un escalador"

class Contrarrelojista(Ciclista):
    def __init__(self, identificador: int, nombre: str, velocidad_maxima: float):
        super().__init__(identificador, nombre)
        self._velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self) -> float:
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: float):
        self._velocidad_maxima = velocidad_maxima

    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima = {self._velocidad_maxima}")

    def imprimir_tipo(self) -> str:
        return "Es un contrarrelojista"

def main():
    equipo1 = Equipo("Sky", "Estados Unidos")
    
    velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
    escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
    contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)
    
    equipo1.anadir_ciclista(velocista1)
    equipo1.anadir_ciclista(escalador1)
    equipo1.anadir_ciclista(contrarrelojista1)
    
    velocista1.set_tiempo_acumulado(365)
    escalador1.set_tiempo_acumulado(385)
    contrarrelojista1.set_tiempo_acumulado(370)
    
    equipo1.calcular_total_tiempo()
    equipo1.imprimir()
    equipo1.listar_equipo()

if __name__ == "__main__":
    main()
