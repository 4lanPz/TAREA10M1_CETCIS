# Problema 1: Análisis de Temperaturas Mensuales

ciudades = []
temperaturas = []
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Devuelve el promedio anual de una ciudad
def calcular_promedio_anual(temperaturas_ciudad):
    suma = 0
    for temp in temperaturas_ciudad:
        suma += temp
    return suma / len(temperaturas_ciudad)

# Devuelve el índice del mes más caluroso
def obtener_mes_mas_caluroso(temperaturas_ciudad):
    indice_mayor = 0
    for i in range(1, len(temperaturas_ciudad)):
        if temperaturas_ciudad[i] > temperaturas_ciudad[indice_mayor]:
            indice_mayor = i
    return indice_mayor

# Devuelve el índice del mes más frío
def obtener_mes_mas_frio(temperaturas_ciudad):
    indice_menor = 0
    for i in range(1, len(temperaturas_ciudad)):
        if temperaturas_ciudad[i] < temperaturas_ciudad[indice_menor]:
            indice_menor = i
    return indice_menor

# Calcula la variación de temperatura de una ciudad
# (temperatura mayor - temperatura menor)
def calcular_variacion(temperaturas_ciudad):
    mayor = temperaturas_ciudad[0]
    menor = temperaturas_ciudad[0]
    for temp in temperaturas_ciudad:
        if temp > mayor:
            mayor = temp
        if temp < menor:
            menor = temp
    return mayor - menor

# Devuelve el nombre de la ciudad con mayor variación anual
def ciudad_con_mayor_variacion(ciudades, temperaturas):
    indice_mayor = 0
    mayor_variacion = calcular_variacion(temperaturas[0])
    for i in range(1, len(temperaturas)):
        variacion_actual = calcular_variacion(temperaturas[i])
        if variacion_actual > mayor_variacion:
            mayor_variacion = variacion_actual
            indice_mayor = i
    return ciudades[indice_mayor], mayor_variacion

print("=== ANÁLISIS DE TEMPERATURAS MENSUALES ===")

num_ciudades = int(input(f"Ingrese el numero de ciudades: "))
for i in range(num_ciudades):
    nombre_ciudad = input(f"Ingrese el nombre de la ciudad {i + 1}: ")
    ciudades.append(nombre_ciudad)

    temperaturas_ciudad = []
    print(f"Ingrese las temperaturas de {nombre_ciudad} para los 12 meses:")

    for j in range(12):
        temp = float(input(f"{meses[j]}: "))
        temperaturas_ciudad.append(temp)

    temperaturas.append(temperaturas_ciudad)

print("\n=== RESULTADOS ===")

for i in range(num_ciudades):
    promedio = calcular_promedio_anual(temperaturas[i])
    mes_caluroso = obtener_mes_mas_caluroso(temperaturas[i])
    mes_frio = obtener_mes_mas_frio(temperaturas[i])

    print(f"\nCiudad: {ciudades[i]}")
    print(f"Promedio anual: {promedio:.2f}")
    print(f"Mes más caluroso: {meses[mes_caluroso]}")
    print(f"Mes más frío: {meses[mes_frio]}")

ciudad, variacion = ciudad_con_mayor_variacion(ciudades, temperaturas)
print(f"\nLa ciudad con mayor variación de temperatura fue {ciudad} con {variacion:.2f} grados.")