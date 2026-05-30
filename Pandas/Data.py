#dataframe es una estructura de datos bidimensional, es decir, tiene filas y columnas. Es similar a una tabla en una base de datos o a una hoja de cálculo en Excel. Cada columna puede contener un tipo de dato diferente (por ejemplo, números, texto, fechas), y cada fila representa un registro o una entrada de datos.
import pandas as pd
import numpy as np
file_path = "C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv"
sales_data= pd.read_csv(file_path)
print(sales_data.head())#lo que hace head es mostrar las primeras filas del dataframe, por defecto muestra las primeras 5 filas, pero se puede especificar el número de filas que se quieren mostrar pasando un argumento a la función head(), por ejemplo head(10) mostrará las primeras 10 filas del dataframe.

#Dataframe usando array numpy
data=np.array ([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array=pd.DataFrame(data, columns=['A','B','C'])
print(dt_from_array)

#Dataframe usando lista
data2 = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]
dt_from_list=pd.DataFrame( data2, columns=['ID', 'Name', 'Age'])
print(dt_from_list)

#dataframe usando diccionario
data3 = [{"ID":1, "Name":"Bob", "Age":30}, {"ID":2, "Name":"Alice", "Age":25}, {"ID":3, "Name":"Charlie", "Age":35}]
dt_from_dict_list=pd.DataFrame(data3)#aqui no es necesario especificar las columnas porque el dataframe las toma del diccionario
print(dt_from_dict_list)

#dataframe diccionario donde las claves son los nombres de las columnas y los valores son listas con los datos de cada columna
data4={"ID":[1,2,3], "Name":['Bob', 'Alice', 'Charlie'], "Age":[30, 25, 35]}
dt_from_dict=pd.DataFrame(data4) #llamando a pandas
print(dt_from_dict)

#series es una estructura de datos unidimensional, es decir, tiene una sola columna. Es similar a una lista o un array en Python, pero con etiquetas para cada elemento. Cada elemento de una serie puede contener un tipo de dato diferente (por ejemplo, números, texto, fechas), y cada elemento tiene una etiqueta única que se utiliza para acceder a él.
data5={"ID":pd.Series([1, 2, 3]),"Name":pd.Series(['Bob', 'Alice', 'Charlie']), "Age":pd.Series([30, 25, 35])}
dt_from_dict_series=pd.DataFrame(data5)
print(dt_from_dict_series)