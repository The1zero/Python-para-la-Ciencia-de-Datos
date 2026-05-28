#¿Por qué usamos lo arrays en Numpy?

#Los arrays en NumPy se utilizan porque ofrecen una estructura eficiente y flexible para manejar grandes volúmenes de datos numéricos. Estos son algunos de los motivos:

#Eficiencia: Los arrays de NumPy son más rápidos y utilizan menos memoria que las listas de Python. Esto se debe a que NumPy está implementado en C y realiza operaciones matemáticas de manera muy eficiente.
#Operaciones Vectorizadas: NumPy permite realizar operaciones matemáticas y lógicas sobre arrays enteros sin necesidad de bucles explícitos. Esto se conoce como vectorización y resulta en un código más limpio y rápido.
#Funcionalidad Extendida: NumPy proporciona una amplia gama de funciones matemáticas y estadísticas que se pueden aplicar directamente a los arrays. Además, facilita la manipulación de datos, como la reshaping, slicing, y indexing de arrays.
#Compatibilidad: NumPy es el fundamento de muchos otros paquetes científicos y de análisis de datos en Python, como SciPy, Pandas, y scikit-learn. Utilizar NumPy facilita la integración y el uso de estas bibliotecas.

import numpy as np
array= np.array([[1,2,3],[4,5,6]])
print(array.ndim)
print(array.shape)
print(array.dtype)#describe el tipo de elementos que tenemos en el array

z = np.array(3, dtype=np.uint8)
print (z)

double_array= np.array([1,2,3], dtype='d')
print(double_array)

z=z.astype(np.float64)
print(z)

sum=np.sum(array)
print(sum)

mean=np.mean(array)
print(mean)

std=np.std(array)
print(std)