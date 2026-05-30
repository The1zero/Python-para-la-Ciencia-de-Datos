#Pandas sirve para la manipulación y análisis de datos. Proporciona estructuras de datos y funciones para trabajar con datos estructurados, como tablas y series temporales.
import pandas as pd

path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
retail_data = pd.read_csv(path)
print(retail_data)
print(type(retail_data))

#EXCEL
#data_excel= pd.read_excel(path)

#JSON
#data_json= pd.read_json(path)