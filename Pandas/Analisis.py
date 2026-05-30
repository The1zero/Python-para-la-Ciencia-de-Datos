#Pandas sirve para la manipulación y análisis de datos. Proporciona estructuras de datos y funciones para trabajar con datos estructurados, como tablas y series temporales.
import pandas as pd

path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
retail_data = pd.read_csv(path)
#print(retail_data)
#print(type(retail_data))

#EXCEL
#data_excel= pd.read_excel(path)

#JSON
#data_json= pd.read_json(path)

columns_name= retail_data.columns
print(columns_name)

num_rows, num_columns = retail_data.shape
print(f"El número de filas es: {num_rows}")
print(f"El número de columnas es: {num_columns}")

daily_sales=retail_data['Quantity']
print(daily_sales)
print(daily_sales[2])

#Descripcion entera del dataframe
summary=retail_data.describe()
print(summary)

mean_value=daily_sales.mean()
print(f"El valor medio de las ventas diarias es: {mean_value}")

mean_value=daily_sales.median()
print(f"La mediana es: {mean_value}")

mean_value=daily_sales.sum()
print(f"La suma total es: {mean_value}")

#conteo de valores
count=daily_sales.count()
print(count)

retail_data.head() #muestra las primeras filas del dataframe
