#groupby
import pandas as pd
df=pd.read_csv("C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv")
country_count=df['Country'].value_counts() #contamos el numero de ocurrencias de cada pais en la columna Country
#print(country_count)

country_group=df.groupby('Country')['Quantity'].sum() #agrupamos el dataframe por la columna Country y sumamos los valores de la columna Quantity para cada pais
#print(country_group)

#calculo de estadisticas
country_stats=df.groupby('Country')['UnitPrice'].agg(['mean', 'sum'])#agrupamos el dataframe por la columna Country y calculamos la media y la suma de los valores de la columna UnitPrice para cada pais
#print(country_stats)

country_stock_group=df.groupby(['Country', 'StockCode'])['Quantity'].sum() #agrupamos el dataframe por las columnas Country y StockCode y sumamos los valores de la columna Quantity para cada combinacion de pais y codigo de producto
#print(country_stock_group)

def total_revenue(group): #creamos una funcion que calcula el ingreso total para cada grupo, multiplicando la cantidad por el precio unitario
    return (group['Quantity'] * group['UnitPrice']).sum() #calculamos el ingreso total para cada grupo aplicando la funcion total_revenue a cada grupo
revenue_by_country=df.groupby('Country').apply(total_revenue) #agrupamos el dataframe por la columna Country y aplicamos la funcion total_revenue a cada grupo para obtener el ingreso total por pais
print(revenue_by_country)