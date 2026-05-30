import numpy as np
#Encontrar elementos unicos y contar su frecuencia
encontrar=np.array(["bueno","malo","excelente","bueno","malo","malo","excelente","bueno","malo","excelente","Kronos"])
#consultar cuales son las unicas respuestas de encontrar
unicos=np.unique(encontrar)
print("Respuestas unicas: ",unicos)
#con unique se puede contar la frecuencia de cada respuesta
unique_elements, count = np.unique(encontrar, return_counts=True)
print("Respuestas unicas: ", unique_elements)
print("Frecuencia de cada respuesta: ", count)

#Funcionamiento de las vistas
array_x=np.arange(10)
view_y=array_x[1:3]#Del array x tener la vista de datos usando corchetes desde posicion 1 a la 3
print("Array original: ",array_x)
print("Vista del array: ",view_y)
array_x[1:3] = [10,11]
print("Array original: ",array_x)
print("Vista del array: ",view_y)

#Crear una copia del array
array_y=np.arange(10)
copy_x=array_y[[1,2]]#Crear una copia del array usando corchetes con los indices de los elementos a copiar
print("Array original: ",array_y)
print("Copia del array: ",copy_x)
array_y[1:3] = [10,11]
print("Array original: ",array_y)
print("Copia del array: ",copy_x) #muestra el mismo resultado porque es una copia del array original y no se ve afectada por los cambios en el array original

#Como saber que es una copia o una vista
print("¿Es view_y una vista de array_x? ", np.shares_memory(view_y, array_x)) #True porque view_y es una vista de array_x
print("¿Es copy_x una vista de array_y? ", np.shares_memory(copy_x, array_y)) #False porque copy_x es una copia de array_y y no comparte memoria con el array original