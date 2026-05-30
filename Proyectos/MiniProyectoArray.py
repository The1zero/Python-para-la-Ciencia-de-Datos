import numpy as np 
#Paso 1: Crear Arrays con Datos de Ventas
#Usa la librería numpy para crear los siguientes arrays: meses: un array con los nombres de los meses del año. ventas_A, ventas_B, ventas_C: arrays que representan las ventas mensuales de tres productos diferentes.
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700])
ventas_B = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650])
ventas_C = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])

#Paso 2: Estadísticas Básicas

#Calcula la media y la suma de ventas para los productos A, B y C usando las funciones de NumPy.
#Imprime estos valores en el formato siguiente:
#Media de ventas Producto A: <valor>
#Suma de ventas Producto A: <valor>
#Repite para los productos B y C.

media_A = np.mean(ventas_A)
suma_A = np.sum(ventas_A)

media_B = np.mean(ventas_B)
suma_B = np.sum(ventas_B)

media_C = np.mean(ventas_C)
suma_C = np.sum(ventas_C)

print(f"Media de ventas Producto A: {media_A}")
print(f"Suma de ventas Producto A: {suma_A}")
print(f"Media de ventas Producto B: {media_B}")
print(f"Suma de ventas Producto B: {suma_B}")
print(f"Media de ventas Producto C: {media_C}")
print(f"Suma de ventas Producto C: {suma_C}")

#Paso 3: Manipulación y Análisis de Datos
#Total de ventas por mes: Suma las ventas de los tres productos para cada mes.
#Promedio de ventas por producto: Calcula el promedio de ventas por producto.
#Mes con mayor y menor ventas: Identifica qué mes tuvo el total de ventas más alto y cuál el más bajo usando las funciones np.argmax y np.argmin.

total_ventas_mes = ventas_A + ventas_B + ventas_C
promedio_ventas_producto=np.array([media_A, media_B, media_C])#Promedio de ventas por producto
mes_mayor_ventas = meses[np.argmax(total_ventas_mes)]
mes_menor_ventas = meses[np.argmin(total_ventas_mes)]

print(f"Total de ventas por mes: {total_ventas_mes}")
print(f"Promedio de ventas por producto: {promedio_ventas_producto}")
print(f"Mes con mayor ventas: {mes_mayor_ventas}")
print(f"Mes con menor ventas: {mes_menor_ventas}")

#Paso 4: Operaciones Avanzadas con NumPy

#Reshape y Transposición:

#Crea una matriz 2D con las ventas de los tres productos y transforma su forma (reshape) a un array tridimensional con dimensiones (3, 4, 3).
#Transpone la matriz de ventas para que las filas se conviertan en columnas.
#Invertir arrays: Invierte las ventas de cada producto en orden de meses.
#Aplanar la matriz: Convierte la matriz de ventas a un array unidimensional.
matriz_ventas = np.array([ventas_A, ventas_B, ventas_C])
matriz_ventas_reshaped = matriz_ventas.reshape(3, 4, 3)
matriz_ventas_transpuesta = matriz_ventas.T
ventas_invertidas = matriz_ventas[:, ::-1]
matriz_ventas_aplanada = matriz_ventas.flatten()
print(f"Matriz de ventas original: {matriz_ventas}")
print(f"Matriz de ventas reshaped: {matriz_ventas_reshaped}")
print(f"Matriz de ventas transpuesta: {matriz_ventas_transpuesta}")
print(f"Ventas invertidas: {ventas_invertidas}")
print(f"Matriz de ventas aplanada: {matriz_ventas_aplanada}")

#Paso 5: Análisis de Elementos Únicos
#Utiliza np.unique para encontrar los elementos únicos en los datos de ventas y cuenta cuántas veces aparece cada uno.
elementos_unicos, conteo = np.unique(matriz_ventas_aplanada, return_counts=True)#Elementos únicos y su conteo se usa la de aplanada porque es un array unidimensional que contiene todas las ventas de los tres productos. Al usar la matriz original, se obtendrían elementos únicos por producto, lo que no es el objetivo en este caso.
print(f"Elementos únicos en las ventas: {elementos_unicos}")
print(f"Conteo de cada elemento único: {conteo}")

#Paso 6: Indexación y Slicing

#Ventas del primer trimestre: Extrae las ventas de los tres primeros meses del año.
#Indexación booleana: Selecciona los meses donde el total de ventas de los tres productos supere los 800.
#Selección avanzada: Usa una lista de índices para seleccionar las ventas de los meses pares (o selecciona los meses a tu elección) y muestra esas ventas en una nueva matriz.

ventas_primer_trimestre = matriz_ventas[:, :3]
meses_superan_800 = meses[total_ventas_mes > 800]
ventas_altas=total_ventas_mes[total_ventas_mes > 800]
indices=[1, 3, 5, 7, 9, 11]
ventas_meses = matriz_ventas[:, indices]
print(f"Ventas del primer trimestre: {ventas_primer_trimestre}")
print(f"Meses donde el total de ventas supera los 800: {meses_superan_800}")
print(f"Ventas totales que superan los 800: {ventas_altas}")
print(f"Ventas de los meses seleccionados: {ventas_meses}")


