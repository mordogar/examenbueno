productos_almacen = {
    "Estantería A":[
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

def buscar_producto(productos_almacen, nombre_producto):
    resultado = []
    
    for estanteria, productos in productos_almacen.items():

        for producto in productos:

            if producto["nombre"].lower() == nombre_producto.lower():

                resultado.append({"estanteria": estanteria, "cantidad": producto["cantidad"]})

    if resultado:
        for r in resultado:
            print(f"Producto '{nombre_producto}' encontrado en {r['estanteria']} con cantidad {r['cantidad']}.")
    else:
        print(f"Producto '{nombre_producto}' no encontrado en el almacén.")
    
    return resultado

nombre_producto=input("Introduzca el nombre del producto que deseas buacar")
print(productos_almacen,nombre_producto)
