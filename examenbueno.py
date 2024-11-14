
productos_almacen = {
    "Estantería A": [
        {"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5},
        {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}
    ],
    "Estantería B": [
        {"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
        {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}
    ],
    "Estantería C": [
        {"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
        {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}
    ],
    "Estantería D": [
        {"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
        {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}
    ]
}
#gestion de entrada de productos 
def agregar_producto(almacen, estanteria, nombre_producto, cantidad, precio):
    if estanteria not in almacen:
        almacen[estanteria] = []
    almacen[estanteria].append({"nombre": nombre_producto, "cantidad": cantidad, "precio": precio})
    print(f"Producto '{nombre_producto}' agregado a la {estanteria} con éxito.")
nombre_producto=input("ingreseel nombre del producto que quieres")
estanteria=input=("eligue una estanteria ")
cantidad=input=("cuantos quieres")
precio=("cuanto vale")
print(f"nombre:{nombre_producto} estanteria: {estanteria} cantidad: {cantidad} precio{ precio}")
#gestion de salida de productos 
def retirar_producto(almacen, estanteria, nombre_producto, cantidad):
    for producto in almacen.get(estanteria, []):
        if producto["nombre"] == nombre_producto:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                print(f"{cantidad} unidades de '{nombre_producto}' retiradas de {estanteria}.")
                return
            else:
                print("Error: No hay suficiente cantidad disponible.")
                return
    print(f"Producto '{nombre_producto}' no encontrado en {estanteria}.")
nombre_producto=input("que producto quieres ")
cantidad=input("cuantos quieres")
print(f"nombre: {nombre_producto} cantidad: {cantidad}")

#verificar disponibilidad de productos 
def verificar_disponibilidad(almacen, nombre_producto):
    encontrado = False
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                print(f"Producto '{nombre_producto}' disponible en {estanteria} con {producto['cantidad']} unidades.")
                encontrado = True
    if not encontrado:
        print(f"Producto '{nombre_producto}' no disponible.")
nombre_producto = input("Introduce el nombre del producto que deseas buscar: ")
verificar_disponibilidad(productos_almacen, nombre_producto)

#verificar el estado del almacen 
def estado_almacen(almacen):
    for estanteria, productos in almacen.items():
        total_estanteria = sum(p["cantidad"] for p in productos)
        valor_estanteria = sum(p["cantidad"] * p["precio"] for p in productos)
        print(f"{estanteria} contiene {total_estanteria} productos con un valor total de {valor_estanteria}.")

#Trasferencia de productos entre estanterías
def transferir_producto(almacen, estanteria_origen, estanteria_destino, nombre_producto, cantidad):
    for producto in almacen.get(estanteria_origen, []):
        if producto["nombre"] == nombre_producto:
            if producto["cantidad"] >= cantidad:
                # Reducir en la estantería origen
                producto["cantidad"] -= cantidad
                # Añadir en la estantería destino
                if estanteria_destino not in almacen:
                    almacen[estanteria_destino] = []
                # Buscar el producto en la estantería destino
                for prod_destino in almacen[estanteria_destino]:
                    if prod_destino["nombre"] == nombre_producto:
                        prod_destino["cantidad"] += cantidad
                        print(f"{cantidad} unidades de '{nombre_producto}' transferidas de {estanteria_origen} a {estanteria_destino}.")
                        return
                # Si el producto no existe en la estantería destino, añadirlo
                almacen[estanteria_destino].append({"nombre": nombre_producto, "cantidad": cantidad, "precio": producto["precio"]})
                print(f"{cantidad} unidades de '{nombre_producto}' transferidas de {estanteria_origen} a {estanteria_destino}.")
                return
            else:
                print("Error: No hay suficiente cantidad disponible para transferir.")
                return
    print(f"Producto '{nombre_producto}' no encontrado en {estanteria_origen}.")
datos=input("ingrese el nombre del prodcuto la cantidad que desea la estanteria en donde se encuentra y la estanteria a donde quiere llegar")
print(f"nombre: {nombre_producto} cantidad: {cantidad} estantería donde se encuentra: {estanteria_origen} y lo he cambiado a la estanteria {estanteria_destino}")