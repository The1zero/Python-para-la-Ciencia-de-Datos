import pandas as pd
file_path= "C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv"
sales_data=pd.read_csv(file_path)

#Convertir la columna 'InvoiceDate' a tipo datetime
sales_data['InvoiceDate']=pd.to_datetime(sales_data['InvoiceDate'])

#Eliminar Filas con valores faltantes en las columnas 'CustomerID' e 'InvoiceDate'
sales_data.dropna(subset=['CustomerID','InvoiceDate'], inplace=True)

#crear una nueva columna 'TotalPrice'
sales_data['TotalPrice']=sales_data['Quantity']*sales_data['UnitPrice']
#print(sales_data.head())

#Filtrar ventas en Reino Unido
uk_sales=sales_data[sales_data['Country']=='United Kingdom']
print(uk_sales)

high_quantity_sales=sales_data[sales_data['Quantity']>10]#Filtrar ventas con cantidad mayor a 10
print(high_quantity_sales)


uk_high_quantity_sales=sales_data[(sales_data['Country']=='United Kingdom') & 
                                  (sales_data['Quantity']>40)]#Filtrar ventas en Reino Unido con cantidad mayor a 10. Mas de una itereacion en una liena de codigo
print(uk_high_quantity_sales)

#filtracion de ventas año 2011
sales_2011=sales_data[sales_data['InvoiceDate'].dt.year==2011] #Filtrar ventas del año 2011 utilizando la propiedad dt.year para extraer el año de la columna 'InvoiceDate'
print(sales_2011)

#filtracion por año y mes(representado por numero)
sales_dec_2010=sales_data[(sales_data['InvoiceDate'].dt.year==2010) & 
                          (sales_data['InvoiceDate'].dt.month==12)] #Filtrar ventas del año 2010 y mes de diciembre utilizando las propiedades dt.year y dt.month para extraer el año y el mes de la columna 'InvoiceDate'

print(sales_dec_2010)
