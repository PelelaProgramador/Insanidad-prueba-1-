from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, marca, peso, aro, precio):  # Agrega precio como un atributo
        super().__init__(marca, peso)
        self.__aro = aro
        self.precio = precio  # Guarda el precio como un atributo de la bicicleta

    def calcular_despacho(self):
        peso_despacho = self.peso * 400
        return Transporte.COSTO_DESPACHO_BASE + peso_despacho

    def imprimir_caracteristicas(self):
        super().imprimir_caracteristicas()
        print(f"Aro: {self.__aro}")
        costo_despacho = self.calcular_despacho()
        print(f"Costo de despacho: ${costo_despacho:.2f}")
        print(f"Precio: ${self.precio:.2f}")  # Muestra el precio en las características

