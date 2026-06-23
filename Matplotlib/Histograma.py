import numpy as np
import matplotlib.pyplot as plt

#Graficar una distribucion normal
data=np.random.normal(170,10,200) #muestra de datos array distribucion normal(media de la distribucion en los parametros, luego la desviacion estandar y le pidemos a numpy que cree 200 datos)

#Graficar informacion (histograma)
plt.hist(data, color='Salmon', bins=20, edgecolor='black', alpha=0.6)
plt.title('Distribucion de altura')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')   
plt.show()