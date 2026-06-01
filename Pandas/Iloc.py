import pandas as pd
#Iloc extrae informacion del dataframe especificando el indice y loc con la etiqueta filas y columnas

path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
retail_data = pd.read_csv(path)

first_row=retail_data.iloc[0]
print(f"Primera fila del dataframe:\n{first_row}")

first_five_row=retail_data.iloc[6:8]
print(f"Primeras cinco filas del dataframe:\n{first_five_row}")


subset=retail_data.iloc[:3, :2]
print(f"Subset del dataframe (primeras 3 filas y primeras 2 columnas):\n{subset}")

retail_value=retail_data.iloc[1,3]
print(f"Valor del dataframe (fila 1, columna 2):\n{retail_value}")

#Loc seleccion de filas
row_index_3=retail_data.loc[3]
print(f"Fila con indice 3:\n{row_index_3}")

row_index_0_to_4=retail_data.loc[0:4]
print(f"Filas con indices 0 a 4:\n{row_index_0_to_4}")

quantity_column=retail_data.loc[:, 'Quantity'] #Especificamos la etiqueta de la columna que queremos
print(f"Columna 'Quantity':\n{quantity_column}")


quantity_unitprices_column= retail_data.loc[:, ['Quantity', 'UnitPrice']] #Especificamos las etiquetas de las columnas que queremos en forma de lista
print(f"Columnas 'Quantity' y 'UnitPrice':\n{quantity_unitprices_column}")