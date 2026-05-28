#Forma de acceder a elementos de un array por medio de su indice
import numpy as np
array=np.array([10,20,30,40,50])
print (array[1])
print (array[-1])

print(array[1:4]) 

#indexacion booleana
#crear una variable donde pregunte que elementos son mayores a 25
bool_index = array > 25
print(type(bool_index)) #Devuelve booleanos que cumplen False/True

#imprimir los elementos del array que esten en index
index=[2,3,4]#formato lista
print(array[index])
#Permite obtener multiples elementos de un array con una lista de indices.

#array con mas dimensiones y con numeros aleatorios
array2 = np.random.randint(1,10, size=[3,3]) #tipo entero de numero del 1 al 10 con una matriz de 3x3
print(array2)
print(array2 [0,1])
print(array2 [:2,:2]) #hacer cortes de mayor longitud 

#Ejercicios para practicar Indexación y Slicing:

#1 Acceder a elementos específicos:
#Crea un arreglo de 10 números y accede al cuarto y penúltimo elemento usando índices positivos y negativos.
arrayejer=np.array([74,34,102,33,55,1,0,4444,777,10000000])
print("Ejercicio 1 4to elemento", arrayejer[3]) 
print("Ejercicio 1 penultimo elemento", arrayejer[-2]) 

#2 Slicing de arreglos:
#Dado un arreglo de números del 1 al 20, extrae los elementos entre las posiciones 3 y 7, y luego los elementos de las últimas 5 posiciones.
arrayejer2 = np.arange(1,21)
print("Ejercicio2",arrayejer2[3:8]) #posiciones 3 y 7
print("Ejercicio2", arrayejer2[-5:]) #5 ultimos

#Indexing con booleanos:
#3 Crea un arreglo de números aleatorios entre 0 y 100. Usa una expresión booleana para acceder solo a los números mayores a 50.
arrayejer3 = np.random.randint(0,100,10)#que sean 10 en el arreglo
bool_index2 = arrayejer3 > 50
print("Ejercicio 3 arreglo: ", arrayejer3)
print("Booleanos: ", bool_index2) #Al ser booleano nos dira True en la respuesta
print("Mayores a 50: ", arrayejer3[bool_index2])

#Indexación con múltiples índices:
# 4 Dado un arreglo de 8 elementos, crea una lista de índices para acceder a los elementos en las posiciones 1, 4, y 6.
arrayejer4=np.random.randint(0,100,8)
index2=[1,4,6] #formato lista
print("Ejercicio 4 arreglo: ",arrayejer4)
print("Ejecicio 4 elementos posicion 1, 4 y 6:", arrayejer4[index2])

#Matrices bidimensionales:
# 5 Genera una matriz 4x4 de números aleatorios entre 10 y 50, y accede a la submatriz de 2x2 ubicada en la esquina inferior derecha.
arrayejer5 = np.random.randint(10,50, size=[4,4]) 
print("Ejercicio 5 arreglo: ", arrayejer5)
print(arrayejer5 [0,1])
print(arrayejer5 [2:4,2:4])