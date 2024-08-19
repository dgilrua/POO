class Cuenta:
  
  def __init__(self, saldo: float, tasa_anual: float):
    self._saldo = saldo
    self._tasa_anual = tasa_anual
    self._num_consignaciones: int = 0
    self._num_retiros: int = 0
    self._comision: float = 0
    
  def consignar(self, valor: float):
    self._saldo += valor
    self._num_consignaciones += 1
  
  def retirar(self, valor: float):
    if valor > self._saldo:
      print("Fondos insuficientes")
      return
    self._saldo -= valor
    self._num_retiros += 1
   
  def calcular_interes(self):
    self.tasa_mensual = self._tasa_anual / 12
    self._saldo += self._saldo * self.tasa_mensual
  
  def extracto_mensual(self):
    self._saldo -= self._comision;
    self.calcular_interes()  
    
  def mostrar_atributos(self):
    print(f"Saldo: {self._saldo}")
    print(f"Tasa anual: {self._tasa_anual}")
    print(f"Numero de consignaciones: {self._num_consignaciones}")
    print(f"Numero de retiros: {self._num_retiros}")
    print(f"Comision: {self._comision}")
    

class CuentaAhorros(Cuenta):
        
    def __init__(self, saldo: float, tasa_anual: float):
      super().__init__(saldo, tasa_anual)
      
      self._estado = self._saldo >= 10000
    
    def _actualizar_estado(self):
      self._estado = self._saldo >= 10000
    
    def consignar(self, valor: float):
      if self._estado:
        super().consignar(valor)
        self._actualizar_estado()
      else :
        print("Cuenta inactiva")
    
    def retirar(self, valor: float):
      if self._estado:
        super().retirar(valor)
        self._actualizar_estado()
      else:
        print("Cuenta inactiva")
    
    def extracto_mensual(self):
      if self._num_retiros > 4:
        self._comision = (self._num_retiros - 4) * 1000
      super().extracto_mensual()
      self._actualizar_estado()
    
    def mostrar_atributos(self):
      print(f"Saldo: {self._saldo}")
      print(f"comision: {self._comision}")
      print(f"numero de transacciones: {self._num_consignaciones + self._num_retiros}")
      
      
class CuentaCorriente(Cuenta):
  
  def __init__ (self, saldo: float, tasa_anual: float):
    super().__init__(saldo, tasa_anual)
    self._sobre_giro = 0
    
  def retirar(self, valor: float):
    if valor > self._saldo:
      self._sobre_giro += valor - self._saldo
      self._saldo = 0
    else:
      super().retirar(valor)
  
  def consignar(self, valor: float):
    if self._sobre_giro > 0:
      if valor >= self._sobre_giro:
        valor -= self._sobre_giro
        self._sobre_giro = 0
      else:
        self._sobre_giro -= valor
        valor = 0
    super().consignar(valor)
  
  def extracto_mensual(self):
    super().extracto_mensual()
  
  def mostrar_atributos(self):
    print(f"Saldo: {self._saldo}")
    print(f"Comision: {self._comision}")
    print(f"Numero de transacciones: {self._num_consignaciones + self._num_retiros}")
    print(f"Sobre giro: {self._sobre_giro}")
    

print("Cuenta de ahorros")
cuenta_ahorros = CuentaAhorros(10000, 0.05)
cuenta_ahorros.consignar(1000)
cuenta_ahorros.consignar(1000)
cuenta_ahorros.consignar(1000)
cuenta_ahorros.consignar(1000)
cuenta_ahorros.consignar(1000)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.retirar(200)
cuenta_ahorros.extracto_mensual()
cuenta_ahorros.mostrar_atributos()

print("\nCuenta corriente")
cuenta_corriente = CuentaCorriente(10000, 0.05)
cuenta_corriente.consignar(1000)
cuenta_corriente.consignar(1000)
cuenta_corriente.consignar(1000)
cuenta_corriente.consignar(1000)
cuenta_corriente.consignar(1000)
cuenta_corriente.retirar(1000)
cuenta_corriente.retirar(1000)
cuenta_corriente.retirar(1000)
cuenta_corriente.retirar(1000)
cuenta_corriente.retirar(1000)
cuenta_corriente.retirar(15000)
cuenta_corriente.consignar(1000)
cuenta_corriente.extracto_mensual()
cuenta_corriente.mostrar_atributos()
