# Problema 3: Análisis de Datos de Ventas
totales = []
totales_dia = []
promedios = []
pronostico = []
ventas = []

# Calcula el total vendido por cada sucursal
def calcular_total_por_sucursal(ventas):
    for sucursal in ventas:
        suma = 0
        for venta in sucursal:
            suma += venta
        totales.append(suma)
    return totales

# Calcula el total vendido por cada día sumando todas las sucursales
def calcular_total_por_dia(ventas):
    for dia in range(len(ventas[0])):
        suma = 0
        for sucursal in range(len(ventas)):
            suma += ventas[sucursal][dia]
        totales_dia.append(suma)
    return totales_dia

# Devuelve la sucursal con mejor desempeño
def mejor_sucursal(totales_sucursal):
    indice_mejor = 0
    for i in range(1, len(totales_sucursal)):
        if totales_sucursal[i] > totales_sucursal[indice_mejor]:
            indice_mejor = i
    return indice_mejor, totales_sucursal[indice_mejor]

# Busca qué día tuvo mayores ventas totales
def mejor_dia(totales_dia):
    indice_mejor = 0
    for i in range(1, len(totales_dia)):
        if totales_dia[i] > totales_dia[indice_mejor]:
            indice_mejor = i
    return indice_mejor, totales_dia[indice_mejor]

# Calcula el promedio de ventas de cada sucursal
def calcular_promedio_por_sucursal(ventas):
    for sucursal in ventas:
        suma = 0
        for venta in sucursal:
            suma += venta
        promedios.append(suma / len(sucursal))
    return promedios

# Genera un pronóstico simple para el siguiente mes
# usando el promedio actual de cada sucursal por 30 días
def pronosticar_siguiente_mes(promedios_sucursal):
    for promedio in promedios_sucursal:
        pronostico.append(promedio * 30)
    return pronostico

# Muestra la matriz de ventas
def mostrar_ventas(ventas):
    print("\n=== VENTAS POR SUCURSAL ===")
    for i in range(len(ventas)):
        print("Sucursal", i + 1, ":", ventas[i])
print("=== ANÁLISIS DE DATOS DE VENTAS ===")
cantidad_sucursales = int(input("Ingrese cuántas sucursales hay: "))

# Se pide cuántas sucursales existen y luego se cargan sus ventas
for i in range(cantidad_sucursales):
    ventas_sucursal = []  # esta lista debe reiniciarse para cada sucursal
    print(f"\nIngrese las ventas de la sucursal {i + 1} durante 30 días:")
    for j in range(30):
        venta = float(input(f"Día {j + 1}: "))
        ventas_sucursal.append(venta)
    ventas.append(ventas_sucursal)
mostrar_ventas(ventas)
totales_sucursal = calcular_total_por_sucursal(ventas)
totales_dia = calcular_total_por_dia(ventas)

print("\n=== TOTAL DE VENTAS POR SUCURSAL ===")
for i in range(len(totales_sucursal)):
    print("Sucursal", i + 1, ":", totales_sucursal[i])

print("\n=== TOTAL DE VENTAS POR DÍA ===")
for i in range(len(totales_dia)):
    print("Día", i + 1, ":", totales_dia[i])

indice_mejor_sucursal, total_mejor_sucursal = mejor_sucursal(totales_sucursal)
print("\nLa sucursal con mejor desempeño fue la Sucursal", indice_mejor_sucursal + 1, "con", total_mejor_sucursal)

indice_mejor_dia, total_mejor_dia = mejor_dia(totales_dia)
print("El día con mejores ventas fue el Día", indice_mejor_dia + 1, "con", total_mejor_dia)

promedios_sucursal = calcular_promedio_por_sucursal(ventas)
pronostico = pronosticar_siguiente_mes(promedios_sucursal)

print("\n=== PROMEDIO DE VENTAS POR SUCURSAL ===")
for i in range(len(promedios_sucursal)):
    print("Sucursal", i + 1, ":", round(promedios_sucursal[i], 2))

print("\n=== PRONÓSTICO SIMPLE PARA EL SIGUIENTE MES ===")
for i in range(len(pronostico)):
    print("Sucursal", i + 1, ":", round(pronostico[i], 2))
    
# Se compara la primera mitad del mes con la segunda mitad
print("\n=== TENDENCIA GENERAL POR SUCURSAL ===")
for i in range(len(ventas)):
    suma_primera_mitad = 0
    suma_segunda_mitad = 0

    for j in range(15):
        suma_primera_mitad += ventas[i][j]

    for j in range(15, 30):
        suma_segunda_mitad += ventas[i][j]

    if suma_segunda_mitad > suma_primera_mitad:
        print("Sucursal", i + 1, ": tendencia de crecimiento")
    elif suma_segunda_mitad < suma_primera_mitad:
        print("Sucursal", i + 1, ": tendencia de disminución")
    else:
        print("Sucursal", i + 1, ": tendencia estable")