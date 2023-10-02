from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamano):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.tamano = tamano

    def imprimir_caracteristicas(self):
        super().imprimir_caracteristicas()
        print(f"Tamaño: {self.tamano}")
