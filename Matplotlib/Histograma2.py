import numpy as np
import matplotlib.pyplot as plt

#Graficar una distribucion normal
#data=np.random.normal(170,10,200) #muestra de datos array distribucion normal(media de la distribucion en los parametros, luego la desviacion estandar y le pidemos a numpy que cree 200 datos)

#Graficar informacion (histograma)
#plt.hist(data, color='Salmon', bins=20, edgecolor='black', alpha=0.6)

#Crear semilla donde queremos iniciar la informacion inicia desde el mismo lugar aun siendo aleatoria
np.random.seed(0)
#crear lista de arrays de informacion de edades
ages = [np.random.normal(30,5,100),
        np.random.normal(40,5,100),
        np.random.normal(35,5,100)]

#Graficar esta info
plt.boxplot(ages, patch_artist=True, notch=True, vert=True,
            labels=['Grupo 1','Grupo 2', 'Grupo 3'])

plt.title('Distribucion de edades por grupo')
plt.xlabel('Grupo')
plt.ylabel('Edad (años)')   
plt.show()