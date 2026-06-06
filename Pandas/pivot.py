import pandas as pd
file_path= "C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv"
sales_data=pd.read_csv(file_path)

#pivot tablas son como las tablas dinamicas de excel. Resume y reorgnaniza los datos en un formato tabular.
# Permite transformar los datos de un formato largo a un formato ancho, donde las filas representan una categoría y las columnas representan otra categoría. 
# Es útil para analizar y comparar datos de manera más eficiente.

pivot_table=pd.pivot_table(sales_data,values='Quantity',index='Country',
                           columns='StockCode',aggfunc='sum') #Crear una tabla pivote que resuma la cantidad total de productos vendidos por país y código de producto.
#print(pivot_table)

df=pd.DataFrame({
    'A':['foo','bar','baz'],
    'B':[1,2,3],
    'C':[4,5,6]
})
print(df)

#transformacion de indices con stack
df_stack=df.stack() #Transformar el DataFrame utilizando stack para convertir las columnas en un formato de índice jerárquico.
print(df_stack)

df_unstack=df_stack.unstack() #Transformar el DataFrame utilizando unstack para convertir el índice jerárquico de nuevo a un formato de columnas.
print(df_unstack)

#como crees que se pueda utilizar las pivot tables o como tambien como podemos apilar y desapilar la informacion para poder demostrar los resultados pero basandonos en el proyecto de retail

#Apila los datos para estructurar limpiamente cada transacción y usa tablas dinámicas o desapilado para resumirlos en comparativas claras que demuestren el rendimiento del negocio a los directivos.
