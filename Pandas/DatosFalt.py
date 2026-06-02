import pandas as pd
path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
retail_data = pd.read_csv(path)

#ver si hay datos disponibles, nulos, faltantes
missing_data=retail_data.isna()
print(f"Datos faltantes en el dataframe:\n{missing_data.head()}")

#contar cuantos datos son faltan
missing_count=retail_data.isna().sum()
print(f"Cantidad de datos faltantes por columna:\n{missing_count}")

#eliminar estas partes de información faltante
no_missing_rows=retail_data.dropna()
print(f"Datos sin filas con valores faltantes:\n{no_missing_rows}")

#elimnar columnas con datos faltantes
no_missing_columns=retail_data.dropna(axis=1) #eje que queremos eliminar, 0 filas, 1 columnas
print(f"Datos sin columnas con valores faltantes:\n{no_missing_columns}")

#rellenar los datos faltantes con un valor específico
filled_data=retail_data.fillna(0) #rellena con 0
missing_count=filled_data.isna().sum()
print(f"Cantidad de datos faltantes por columna:\n{missing_count}") #debe salir 0 en todas las columnas
print(f"Datos con valores faltantes rellenados con 0:\n{filled_data}")

#precios unitarios media
mean_unit_price=retail_data["UnitPrice"].mean()
retail_data_filled_mean=retail_data["UnitPrice"].fillna(mean_unit_price) #rellena los datos faltantes de la columna "UnitPrice" con la media de esa columna
print(f"Datos con valores faltantes de 'UnitPrice' rellenados con la media:\n{retail_data_filled_mean}")
