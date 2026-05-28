import numpy as np
#crear un array de precios y descuentos
precios = np.array([100, 200, 300, 400, 500])
descuentos = np.array([0.9])
#quiero precios con descuento
precios_con_descuento = precios * descuentos
print(precios_con_descuento)

#lista de precios aleatorios
precios_aleatorios = np.random.randint(100, 500, size=(3, 3))
descuentos2=np.array([10,20,30])
resultado=precios_aleatorios + descuentos2
print("array aleatorio:", precios_aleatorios)
print("resultado:", resultado)

#tambien podemos hacer operaciones logicas
array=np.array([1, 2, 3, 4, 5])
print(np.all (array > 9)) #verificar si todos los elementos son mayores a 
print(np.any (array > 0)) #verificar si alguno de los elementos es mayor a 

#Concatenacion de arrays
array1=np.array([1, 2, 3])
array2=np.array([4, 5, 6])
array_concatenado=np.concatenate((array1, array2))
print("array concatenado:", array_concatenado)

#Stack de arrays con vstack y hstack con array1 y array2
array_stack=np.hstack((array1, array2))
print("array stack:", array_stack)

#crear un nuevo array con np.arange y split
array_nuevo=np.arange(1,10)
split_array=np.split(array_nuevo, 3)
print("array nuevo:", array_nuevo)
print("split array:", split_array)

#EJERCICIO usar un array con np.arange y split con mas dimension
array_nuevo2=np.arange(1, 25)
split_array2=np.split(array_nuevo2, 4)
print("array nuevo 2:", array_nuevo2)
print("split array 2:", split_array2)


