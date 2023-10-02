from Tecnologia import Tecnologia
from Transporte import Transporte
from Tv import Tv
from Consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta

# Listas para almacenar objetos registrados
tvs = []
consolas = []
scooters = []
bicicletas = []

def menu():
    opcion = ""
    while opcion != '6':
        print("\nMenú:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_tv()
        elif opcion == '2':
            registrar_consola()
        elif opcion == '3':
            registrar_scooter()
        elif opcion == '4':
            registrar_bicicleta()
        elif opcion == '5':
            cotizar_producto()
        elif opcion == '6':
            print("Saliendo del programa...")
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

def cotizar_producto():
    print("\nCotización de Producto:")
    tipo_producto = input("Ingrese el tipo de producto a cotizar (TV, Consola, Scooter, Bicicleta): ").strip().lower()

    if tipo_producto == 'tv':
        cotizar_tv()
    elif tipo_producto == 'consola':
        cotizar_consola()
    elif tipo_producto == 'scooter':
        cotizar_scooter()
    elif tipo_producto == 'bicicleta':
        cotizar_bicicleta()
    else:
        print("Tipo de producto no válido. Por favor, ingrese un tipo válido.")

def cotizar_tv():
    print("\nCotización de TV:")
    if not tvs:
        print("No hay TVs registradas.")
        return

    print("Seleccione una TV para cotizar:")
    for i, tv in enumerate(tvs):
        print(f"{i + 1}. Marca: {tv.marca}, Precio: ${tv.precio:.2f}")

    seleccion = input("Ingrese el número de la TV que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(tvs):
            tv = tvs[seleccion - 1]
            tv.imprimir_caracteristicas()
            descuento = tv.calcular_descuento()
            precio_final = tv.precio - (tv.precio * (descuento / 100))
            print(f"Descuento aplicado: {descuento}%")
            print(f"Precio final con descuento: ${precio_final:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")

def cotizar_consola():
    print("\nCotización de Consola:")
    if not consolas:
        print("No hay Consolas registradas.")
        return

    print("Seleccione una Consola para cotizar:")
    for i, consola in enumerate(consolas):
        print(f"{i + 1}. Marca: {consola.marca}, Precio: ${consola.precio:.2f}")

    seleccion = input("Ingrese el número de la Consola que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(consolas):
            consola = consolas[seleccion - 1]
            consola.imprimir_caracteristicas()
            descuento = consola.calcular_descuento()
            precio_final = consola.precio - (consola.precio * (descuento / 100))
            print(f"Descuento aplicado: {descuento}%")
            print(f"Precio final con descuento: ${precio_final:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")

def cotizar_scooter():
    print("\nCotización de Scooter:")
    if not scooters:
        print("No hay Scooters registrados.")
        return

    print("Seleccione un Scooter para cotizar:")
    for i, scooter in enumerate(scooters):
        print(f"{i + 1}. Marca: {scooter.marca}, Peso: {scooter.peso} kg, Precio: ${scooter.precio:.2f}")

    seleccion = input("Ingrese el número del Scooter que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(scooters):
            scooter = scooters[seleccion - 1]
            scooter.imprimir_caracteristicas()
            costo_despacho = scooter.calcular_despacho()
            descuento = Tecnologia.calcular_descuento(scooter)
            precio_final = scooter.precio - (scooter.precio * (descuento / 100)) + costo_despacho
            #print(f"Costo de despacho: ${costo_despacho:.2f}")
            #print(f"Descuento aplicado: {descuento}%")
            #print(f"Precio final con descuento y despacho: ${precio_final:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")

def cotizar_bicicleta():
    print("\nCotización de Bicicleta:")
    if not bicicletas:
        print("No hay Bicicletas registradas.")
        return

    print("Seleccione una Bicicleta para cotizar:")
    for i, bicicleta in enumerate(bicicletas):
        print(f"{i + 1}. Marca: {bicicleta.marca}, Peso: {bicicleta.peso} kg, Precio: {bicicleta.precio} $")

    seleccion = input("Ingrese el número de la Bicicleta que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(bicicletas):
            bicicleta = bicicletas[seleccion - 1]
            bicicleta.imprimir_caracteristicas()
            costo_despacho = bicicleta.calcular_despacho()
            precio_final = bicicleta.precio + costo_despacho  # Calcula el precio final
            print(f"Precio final (con despacho): ${precio_final:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")


def registrar_tv():
    print("\nRegistro de TV:")
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    eficiencia = input("Eficiencia (A, B, C, D, E, F): ").upper()
    precio = float(input("Precio: $"))
    tamano = input("Tamaño: ")

    tv = Tv(marca, voltaje, eficiencia, precio, tamano)
    tvs.append(tv)

    print("\nTV registrada con éxito.")

def registrar_consola():
    print("\nRegistro de Consola:")
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    eficiencia = input("Eficiencia (A, B, C, D, E, F): ").upper()
    precio = float(input("Precio: $"))
    nombre = input("Nombre de la Consola: ")
    version = input("Versión (Lite o normal): ")

    consola = Consola(marca, voltaje, eficiencia, precio, nombre, version)
    consolas.append(consola)

    print("\nConsola registrada con éxito.")

def registrar_scooter():
    print("\nRegistro de Scooter:")
    marca = input("Marca: ")
    peso = float(input("Peso (en kg): "))
    aro = int(input("Aro: "))
    velocidad = int(input("Velocidad (en km/h): "))
    eficiencia = input("Eficiencia (A, B, C, D, E, F): ").upper()
    precio = float(input("Precio: $"))  # Solicita el precio al usuario

    scooter = Scooter(marca, peso, aro, velocidad, eficiencia, precio)  # Pasa el precio al constructor
    scooters.append(scooter)
    print("\nScooter registrado con éxito.")
    #scooter.imprimir_caracteristicas()
    #costo_despacho = scooter.calcular_despacho()
    #print(f"Costo de despacho: ${costo_despacho:.2f}")

def registrar_bicicleta():
    print("\nRegistro de Bicicleta:")
    marca = input("Marca: ")
    peso = float(input("Peso (en kg): "))
    aro = int(input("Aro: "))
    precio = float(input("Precio: $"))  # Agrega la entrada de precio

    bicicleta = Bicicleta(marca, peso, aro, precio)  # Pasa el precio al constructor de Bicicleta
    bicicletas.append(bicicleta)

    print("\nBicicleta registrada con éxito.")

if __name__ == "__main__":
    print("Bienvenido al sistema")
    menu()
