# Matplitlib es:
# Herramienta para visualización de datos.
# Estándar para la creación de gráficos.
# Integración con Numpy y Pandas.
# Ésta es una librería escrita en python, está enfocada en la visualización de datos por medio de gráficos 2D tales como:
# Barras
# Líneas
# Pie
# Dispersión
# Entre otras.
# Gráfico de líneas: Muestra tendencias y cambios en los datos a lo largo del tiempo.

#Crear nuestro primer grafico de lineas
import numpy as np
import matplotlib.pyplot as plt #usar modulo especifico para hacer los graficos: pyplot

#UTIL PARA IDENTIFICAR PATRONES EN LOS DATOS
month=np.array(['E','F','M','J','A'])
sales=np.array([20,25,30,28,35])

#configurar tamaño de grafico
plt.figure(figsize=(8,6))

#crear el grafico de lineas
plt.plot(month,sales,marker='o',color='blue')

#agregar titulo
plt.title('Ventas Mensuales de un Producto')
#agregar etiquetas a los ejes
plt.xlabel('Meses')
plt.ylabel('Ventas')

#mostrarlo
plt.show()

