# Problema 2: Sistema de Gestión de Inventario

inventario = []
opcion = 0
total = 0

# Agrega un producto nuevo al inventario
def agregar_producto(inventario):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock: "))
    producto = [codigo, nombre, precio, stock]
    inventario.append(producto)
    print("Producto agregado correctamente")

# Muestra todos los productos con número de lista
def mostrar_inventario(inventario):
    print("\n=== INVENTARIO ===")
    if len(inventario) == 0:
        print("El inventario está vacío")
        return
    for i in range(len(inventario)):
        producto = inventario[i]
        print(i + 1, ": Código:", producto[0], "| Nombre:", producto[1], "| Precio:", producto[2], "| Stock:", producto[3])

# Permite seleccionar un producto por su número en la lista
def seleccionar_producto(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío")
        return -1
    mostrar_inventario(inventario)
    opcion = int(input("Ingrese el número del producto: "))
    # Se valida que el número esté dentro del rango correcto
    if opcion < 1 or opcion > len(inventario):
        return -1
    return opcion - 1

# Aumenta el stock de un producto ya existente
def aumentar_stock(inventario):
    indice = seleccionar_producto(inventario)
    if indice == -1:
        print("Selección inválida")
        return
    cantidad = int(input("Ingrese la cantidad a aumentar: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        return
    inventario[indice][3] += cantidad
    print("Stock actualizado correctamente")

# Realiza una venta y disminuye el stock
def realizar_venta(inventario):
    indice = seleccionar_producto(inventario)
    if indice == -1:
        print("Selección inválida")
        return
    cantidad = int(input("Ingrese la cantidad a vender: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        return
    if inventario[indice][3] < cantidad:
        print("Stock insuficiente")
        return
    # Se descuenta la cantidad vendida del stock actual
    inventario[indice][3] -= cantidad
    print("Venta realizada correctamente")

# Muestra productos con stock menor a 5
def mostrar_stock_bajo(inventario):
    print("\n=== PRODUCTOS CON STOCK BAJO ===")
    encontrado = False
    for i in range(len(inventario)):
        if inventario[i][3] < 5:
            producto = inventario[i]
            print(i + 1, "-> Código:", producto[0], "| Nombre:", producto[1], "| Precio:", producto[2], "| Stock:", producto[3])
            encontrado = True
    if not encontrado:
        print("No hay productos con stock bajo")

# Calcula el valor total del inventario
def calcular_valor_total(inventario):
    for producto in inventario:
        total += producto[2] * producto[3]
    return total

while opcion != 6:
    print("\n=== MENÚ DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Aumentar stock")
    print("4. Realizar venta")
    print("5. Mostrar valor total del inventario")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        agregar_producto(inventario)
    elif opcion == 2:
        mostrar_inventario(inventario)
        mostrar_stock_bajo(inventario)
    elif opcion == 3:
        aumentar_stock(inventario)
    elif opcion == 4:
        realizar_venta(inventario)
    elif opcion == 5:
        total = calcular_valor_total(inventario)
        print("Valor total del inventario:", total)
    elif opcion == 6:
        print("Fin del programa")
    else:
        print("Opción inválida")