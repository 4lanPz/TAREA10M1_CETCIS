# Tarea: Integración de funciones y arreglos

## Ejercicio 1: Análisis de Temperaturas Mensuales

### ¿Cómo se resolvió?
Se utiliza un arreglo bidimensional para guardar las temperaturas de varias ciudades durante los 12 meses del año.  
Cada fila representa una ciudad y cada columna representa un mes.

Se crearon funciones separadas para:
- calcular el promedio anual de una ciudad
- identificar el mes más caluroso
- identificar el mes más frío
- calcular la variación de temperatura
- encontrar la ciudad con mayor variación anual

El programa recorre los datos directamente y solo guarda la información necesaria.  
El uso de memoria es bajo y el rendimiento es adecuado porque las operaciones son simples y se hacen sobre arreglos pequeños.

---

## Ejercicio 2: Sistema de Gestión de Inventario

### ¿Cómo se resolvió?
Se usó un arreglo para almacenar productos, donde cada producto guarda:

- código
- nombre
- precio
- cantidad en stock

El sistema se organizó con un menú:
- agregar productos
- ver el inventario
- aumentar stock
- registrar ventas
- mostrar productos con stock bajo
- calcular el valor total del inventario

Cada acción del sistema se convirtió en una función distinta.  
Por ejemplo, una función agrega productos, otra muestra el inventario y otra realiza ventas.
Esto permite que el código sea más ordenado y fácil de modificar.  
Si se quiere cambiar la forma de vender o de mostrar productos, no es necesario rehacer todo el programa.

---

## Ejercicio 3: Análisis de Datos de Ventas

### ¿Cómo se resolvió?
Se utiliza un arreglo bidimensional para guardar las ventas de varias sucursales durante 30 días.  
Cada fila representa una sucursal y cada columna representa un día.

Se implementaron funciones para:
- calcular el total de ventas por sucursal
- calcular el total de ventas por día
- identificar la sucursal con mejor desempeño
- encontrar el día con más ventas
- calcular promedios por sucursal
- generar un pronóstico simple para el siguiente mes

Las funciones separan el cálculo de totales, promedios y pronósticos se resuelve en funciones distintas, lo que evita mezclar toda la lógica en una sola parte del programa.
