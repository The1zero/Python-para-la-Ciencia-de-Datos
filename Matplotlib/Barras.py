import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))#tamaño
categorias=['PRODUCTO A','PRODUCTO B','PRODUCTO C']
sales=[120,150,90]

#Creacion del grafico de barras verticales
plt.bar(categorias,sales,color='skyblue',label='Ventas mensuales')

# Ampliar el límite del eje Y para hacerle espacio al texto (de 0 a 200)
plt.ylim(0, 200)

#Anotacion con flecha para destar un punto en especifico
plt.annotate("Maximo de ventas", xy=("PRODUCTO B",150), xytext=("PRODUCTO C", 160),
              arrowprops = dict(facecolor = 'black', shrink = 0.05))

plt.title("Ventas de productos en un mes")
plt.xlabel("Productos")
plt.ylabel("Ventas")

plt.legend()

plt.show()
