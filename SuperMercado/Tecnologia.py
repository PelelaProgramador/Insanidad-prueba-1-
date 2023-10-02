class Tecnologia:
    def __init__(self, marca, voltaje, eficiencia, precio):
        self.marca = marca
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.precio = precio

    def calcular_descuento(self):
        if self.eficiencia in ['A', 'B']:
            return 50
        elif self.eficiencia in ['C', 'D']:
            return 30
        elif self.eficiencia in ['E', 'F']:
            return 10
        else:
            return 0

    def imprimir_caracteristicas(self):
        print(f"Marca: {self.marca}")
        print(f"Voltaje: {self.voltaje}")
        print(f"Eficiencia: {self.eficiencia}")
        print(f"Precio: ${self.precio:.2f}")
