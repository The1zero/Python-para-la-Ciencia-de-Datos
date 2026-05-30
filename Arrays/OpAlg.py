import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

#Suma
sum= A+B
print("Matriz A:\n",A)
print("Matriz B:\n",B)
print("Suma:\n",sum)

#resta
resta = A - B 
print("Resta:\n",resta)

#multiplicacion
multiplicacion = np.dot(A,B)
print("Multiplicacion:\n",multiplicacion)

#determinante
det_A = np.linalg.det(A) #calcula el determinante de la matriz A
inv_A = np.linalg.inv(A) #calcula la inversa de la matriz A
print("Determinante de A:", det_A)
print("Inversa de A:\n", inv_A)


#resolver sistema de ecuaciones lineales Ax=B
b=np.array([9, 11]) 
x = np.linalg.solve(A, b) #resuelve el sistema de ecuaciones lineales Ax=b
print("Solución del sistema de ecuaciones Ax=b:", x)
