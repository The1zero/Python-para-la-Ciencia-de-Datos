import pandas as pd
#path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
#retail_data = pd.read_csv(path)

#manipulacion de columnas
df=pd.read_csv("C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv")
df["TotalPrice"]=df["Quantity"] * df["UnitPrice"] #creamos una nueva columna con el resultado de multiplicar las columnas Quantity y UnitPrice
print(df.head())


#creacion nueva columna en el dataframe
df['highvalue']= df['TotalPrice'] > 16 #creamos una nueva columna con el resultado de comparar la columna TotalPrice con el valor 16, si es mayor a 16 se asigna True, de lo contrario se asigna False
print(df['highvalue'].head(10))


#Informacion 
print(df.info()) #muestra informacion del dataframe, como el numero de filas, columnas, tipos de datos, etc.

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) #convertimos la columna InvoiceDate a tipo datetime
print(df.info())

#aplicar lambda
df['Discount'] = df['UnitPrice'].apply(lambda x: x * 0.9) #creamos una nueva columna con el resultado de aplicar una funcion lambda a la columna UnitPrice, en este caso se multiplica por 0.9 para obtener un descuento del 10%
print(df.head(3))

def categorize_price(price): #creamos una funcion que categoriza el precio en tres categorias: High, Medium y Low, dependiendo del valor del precio
    if price > 50:
        return 'High'
    elif price >= 20: 
        return 'Medium'
    else:
        return 'Low' 

df['PriceCategory'] = df['UnitPrice'].apply(categorize_price) #creamos una nueva columna con el resultado de aplicar la funcion categorize_price a la columna UnitPrice
print(df.head(10))