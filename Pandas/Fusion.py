import pandas as pd
#file_path= "C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv"
#sales_data=pd.read_csv(file_path)

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

#print(df1)
#print(df2)

inner_join=pd.merge(df1,df2, on='key',how='inner') #Realiza una unión interna (inner join) entre df1 y df2 utilizando la columna 'key' como clave de unión. Solo se incluirán las filas que tengan valores coincidentes en ambas tablas.
#print(inner_join)

outer_merged=pd.merge(df1,df2, on='key',how='outer') #Realiza una unión externa (outer join) entre df1 y df2 utilizando la columna 'key' como clave de unión. Se incluirán todas las filas de ambas tablas, y se rellenarán con NaN los valores faltantes.
#print(outer_merged)

left_merged=pd.merge(df1,df2, on='key',how='left') #Realiza una unión izquierda (left join) entre df1 y df2 utilizando la columna 'key' como clave de unión. Se incluirán todas las filas de df1 y solo las filas coincidentes de df2. Los valores faltantes en df2 se rellenarán con NaN.
#print(left_merged)

right_merged=pd.merge(df1,df2, on='key',how='right') #Realiza una unión derecha (right join) entre df1 y df2 utilizando la columna 'key' como clave de unión. Se incluirán todas las filas de df2 y solo las filas coincidentes de df1. Los valores faltantes en df1 se rellenarán con NaN.
#print(right_merged)

df3 = pd.DataFrame({
        'A': ['A0', 'A1', 'A2'],
        'B': ['B0', 'B1', 'B2']
    })
    
df4 = pd.DataFrame({
        'A': ['A3', 'A4', 'A5'],
        'B': ['B3', 'B4', 'B5']
    })
#print(df3)
#print(df4)

vertical_concat=pd.concat([df3,df4])#Concatena verticalmente los DataFrames df3 y df4, apilando las filas de df4 debajo de las filas de df3. El resultado es un nuevo DataFrame que contiene todas las filas de ambos DataFrames.
#print(vertical_concat)

horizontal_concat=pd.concat([df3,df4],axis=1) #Concatena horizontalmente los DataFrames df3 y df4, uniendo las columnas de ambos DataFrames. El resultado es un nuevo DataFrame que contiene todas las columnas de ambos DataFrames. importante poner axis=1 para concatenar horizontalmente, si no se pone se concatena verticalmente por defecto.
#print(horizontal_concat)

#join combina dataframes con base a un indice o columna clave
df5 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df6 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])

print(df5)
print(df6)

joined=df5.join(df6, how='inner') #Realiza una unión interna (inner join) entre df5 y df6 utilizando los índices como clave de unión. Solo se incluirán las filas que tengan índices coincidentes en ambos DataFrames.
print(joined)

#diferencia de merge y join es que en join se usa indices y merge se usa columnas para unir los dataframes. 
# Merge es mas flexible que join porque permite especificar la columna de unión y el tipo de unión, mientras que join solo permite unir por índices. 
# Merge también puede manejar uniones más complejas, como uniones múltiples o uniones basadas en condiciones, mientras que join se limita a uniones simples basadas en índices.