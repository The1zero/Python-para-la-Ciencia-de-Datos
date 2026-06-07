import pandas as pd
file_path= "C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv"
df=pd.read_csv(file_path)

#Mostrar las primeras filas para entender la estructura del dataset
#print(df.head())
#print(df.info())
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])#Convertir la columna 'InvoiceDate' a formato datetime para facilitar el filtrado por fechas.
#print(df.info())

#borrar nulos
df.dropna(subset=['InvoiceDate'],inplace=True)#Eliminar filas que tengan valores nulos en la columna 'InvoiceDate' para asegurar que todas las filas tengan una fecha válida para el filtrado.
df.set_index('InvoiceDate',inplace=True)

df['Year']=df.index.year #Crear una nueva columna 'Year' extrayendo el año de la columna 'InvoiceDate' para facilitar el filtrado por año.
df['Month']=df.index.month #Crear una nueva columna 'Month' extrayendo el mes de la columna 'InvoiceDate' para facilitar el filtrado por mes.
df['Day']=df.index.day #Crear una nueva columna 'Day' extrayendo el día de la columna 'InvoiceDate' para facilitar el filtrado por día.
df['Weekday']=df.index.weekday #Crear una nueva columna 'Weekday' extrayendo el día de la semana de la columna 'InvoiceDate' para facilitar el filtrado por día de la semana.
df['Hour']=df.index.hour #Crear una nueva columna 'Hour' extrayendo la hora de la columna 'InvoiceDate' para facilitar el filtrado por hora.
#print(df['Year'])
#print(df['Month'])
#print(df['Day'])
#print(df['Weekday'])
#print(df['Hour'])
#print(df)

#extraer dataframe con la info del año 2011
df_2011=df.loc['2011']#Utilizar el método loc para filtrar el DataFrame df y extraer solo las filas correspondientes al año 2011, creando un nuevo DataFrame llamado df_2011.
#print(df_2011.head())

#ahora con mes tambie
df_2011_dec=df.loc['2011-12']#Utilizar el método loc para filtrar el DataFrame df y extraer solo las filas correspondientes al año 2011 y al mes de diciembre, creando un nuevo DataFrame llamado df_2011_dec.
#print(df_2011_dec.head())

#rango de 1 de diciembre 2010 al 15 de diciembre 2010
df_range_dec=df.loc['2010-12-01':'2010-12-15']#Utilizar el método loc para filtrar el DataFrame df y extraer solo las filas correspondientes al rango de fechas desde el 1 de diciembre de 2010 hasta el 15 de diciembre de 2010, creando un nuevo DataFrame llamado df_range_dec.
#print(df_range_dec.head())

#ayudar a crear rangos de fechas donde nosotros vamos a utilizar en info nueva
date_range_new=pd.date_range(start='2024-01-01',end='2024-12-31',freq='D')#Crear un rango de fechas utilizando el método date_range de pandas, especificando la fecha de inicio como '2024-01-01', la fecha de fin como '2024-12-31' y la frecuencia como 'D' (diaria). El resultado es un objeto DatetimeIndex que contiene todas las fechas dentro del rango especificado.
#print(date_range_new)

date_dates=pd.DataFrame(date_range_new,columns=['Date'])#Crear un nuevo DataFrame llamado date_dates a partir del rango de fechas date_range_new, asignando la columna 'Date' para almacenar las fechas.
print(date_dates)