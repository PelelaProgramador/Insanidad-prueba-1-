from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Transporte, Tecnologia):
    def __init__(self, marca, peso, aro, velocidad, eficiencia,precio):
        # Inicializamos las clases padres
        Transporte.__init__(self, marca, peso)
        Tecnologia.__init__(self, marca, "", eficiencia, precio)  # Elimina la inicialización del precio aquí

        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    # Método para calcular el costo de despacho específico para Scooter
    def calcular_despacho(self):
        if self.__peso <= 10:
            costo_despacho = 4000 + (300 * self.__peso)
        else:
            costo_despacho = 4000 + (400 * self.__peso)
        return costo_despacho

    # Método para imprimir las características de Scooter
    def imprimir_caracteristicas(self):
        Transporte.imprimir_caracteristicas(self)  # Llama al método de Transporte para imprimir sus características
        descuento = Tecnologia.calcular_descuento(self)  # Llama al método de Tecnología para calcular el descuento
        costo_despacho = self.calcular_despacho()

        print(f"Aro: {self.__aro}")
        print(f"Velocidad (en km/h): {self.__velocidad}")
        print(f"Costo de despacho: ${costo_despacho:.2f}")
        print(f"Descuento aplicado: {descuento}%")
        
        # Calcula el precio final después de aplicar el descuento y el costo de despacho
        precio_final = self.precio - (self.precio * (descuento / 100)) + costo_despacho
        print(f"Precio final con descuento y despacho: ${precio_final:.2f}")



