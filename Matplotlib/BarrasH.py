import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
categorias=['PRODUCTO A','PRODUCTO B','PRODUCTO C']
sales=[120,150,90]

#Creacion de barras horizontales
plt.barh(categorias,sales,color="skyblue",label="ventas mensuales")

plt.title("Ventas de producto de un mes")
plt.ylabel("Productos")
plt.xlabel("Ventas")

plt.show()