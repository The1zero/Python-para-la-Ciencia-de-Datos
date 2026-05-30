import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
transpuesta=matrix.T
print("Matriz original:",matrix)
print("Matriz transpuesta:",transpuesta) 

array=np.arange(1,13)
reshaped_array=array.reshape(3,4) #Cambia la forma del array a 3 filas y 4 columnas
print("Array original:",array)
print("Array reshaped:",reshaped_array)

#reverse
reversed_array=array[::-1] #Invierte el orden de los elementos del array
print("Array original:",array)
print("Array invertido:",reversed_array)

flattened_array=matrix.flatten() #Aplana el array a una dimensión
print("Matriz original:",matrix)
print("Matriz aplanada:",flattened_array)
