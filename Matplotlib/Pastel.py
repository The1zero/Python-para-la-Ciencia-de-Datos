import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

categorias=['PRODUCTO A','PRODUCTO B','PRODUCTO C']
market_share=[50,35,15]

#Creacion pastel
plt.pie(market_share, labels=categorias, autopct='%1.1f%%',startangle=140,
        colors=['green','purple','pink'])

plt.title("Ventas de producto de un mes")

#Asegurar que sea circulo
plt.axis('equal')

plt.show()