import numpy as np
escalar = np.array(42)
print(type(escalar))
print (escalar)

#Vector
vector=np.array([30,29,35,31,33,36,42])
print(vector)

#CREACION DE MATRIZ
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

#TENSOR
tensor= np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

#RANGE
array_range=np.arange(10)
print(array_range)

#matriz identidad
eye_matrix=np.eye(3)
print(eye_matrix)

#Matriz diagonal
diag=np.diag([1,2,3,4,5,6])
print (diag)

#random
random=np.random.random((2,3))
print(random)