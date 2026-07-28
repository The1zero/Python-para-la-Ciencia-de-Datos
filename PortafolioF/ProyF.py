import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el dataset
path="C:\\Users\\andos\\OneDrive\\Escritorio\\Platzi\\Python_Ciencia_de_datos\\Pandas\\online_retail.csv" 
data = pd.read_csv(path)

#Valores faltantes
#print (data.isnull().sum())

#Valores Duplicados
#print (data.duplicated().sum())


#Valores Únicos buscar principalmente pais y creamos diccionario
unique_values={col: data[col].unique() for col in data.columns if col == 'Country'} #si quitamos el if nos mostrará todos los valores únicos de todas las columnas
#for col,values in unique_values.items():
    #print(f"Columna: {col}")
    #print(f'Número de valores únicos: {len(values)}')
    #print(f'Valores únicos: {values[:10]}')
    #print('- ' * 50)

#Limpieza de datos, eliminar duplicadas con nuevo data frame

data_cleaned=data.drop_duplicates()
data_cleaned = data_cleaned.dropna(subset=['CustomerID'])

#Verificamos cambios
#print (data_cleaned.isnull().sum())
#print (data_cleaned.duplicated().sum()) #Ya todo debe aparecer en 0

#Creamos una columna nueva para tener el resultado dela multiplicacion de cantidad y precio unitario
data_cleaned['TotalAmount'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']


data_cleaned['InvoiceDate']=pd.to_datetime(data_cleaned['InvoiceDate'])


data_cleaned['Year'] = data_cleaned['InvoiceDate'].dt.year
data_cleaned['Month'] = data_cleaned['InvoiceDate'].dt.month
#print(data_cleaned.head())
#print(data_cleaned.info())

#Insights de los datos. Analizar ventas por año, trimestre, etc
sales_by_year = data_cleaned.groupby('Year')['TotalAmount'].sum()
#print(sales_by_year)

data_cleaned['Semester'] = data_cleaned['Month'].apply(lambda x:1 if x<=6 else 2)

sales_by_semester = data_cleaned.groupby(['Year','Semester'])['TotalAmount'].sum()
#print(sales_by_semester)

total_returns = data_cleaned[data_cleaned['Quantity'] < 0]. shape[0]
#print(total_returns)

total_non_returns = data_cleaned[data_cleaned['Quantity'] >= 0]. shape[0]
#print(total_non_returns)

#Graficación en forma de pastel
#labels = ['Devoluciones', 'No Devoluciones']
#sizes = [total_returns, total_non_returns]
#colors = ['lightcoral', 'lightgreen']

#plt.figure(figsize=(8,8))
#plt.pie(sizes, labels = labels, colors=colors,startangle=140)

#plt.title('Porcentaje de transacciones con y sin devolucion')
#plt.show()

#Creamos nueva columna "categoria"
def categorize_total_amount(amount):
    if amount < 20:
        return 'Low'
    elif 20 <= amount < 100:
        return 'Medium'
    else:
        return 'High'
data_cleaned['AmountCategory'] = data_cleaned['TotalAmount'].apply(categorize_total_amount)

#Mostrar las primeras filas de la nueva columna
#print(data_cleaned.head())

#Graficando por categoria
# Contar la cantidad de transacciones por categoría
category_counts = data_cleaned['AmountCategory'].value_counts()

# Graficación en forma de pastel para las categorías
#plt.figure(figsize=(8, 8))

# Extraemos los valores (conteo) y los índices (nombres de las categorías)
#plt.pie(category_counts.values, 
        #labels=category_counts.index, 
        #autopct='%1.1f%%', # Esto agrega el porcentaje en el gráfico
        #colors=['lightskyblue', 'gold', 'lightcoral'], 
        #startangle=140)

#plt.title('Distribución por Categoría de Monto (AmountCategory)')
#plt.show()


#Graficar la distribucion de ventas por mes y año
#plt.figure(figsize=(12,6))
#data_cleaned.groupby(['YEAR', 'MONTH'])['Totalamount'].sum().plot(kind='bar')
#plt.title('Distribucion de Ventas por mes y año')
#plt.xlabel('Año, Mes')
#plt.ylabel('ventas totales')
#plt.show()

#Para la informacion del grafico 4
top_products = data_cleaned.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
top_products = top_products.reset_index()
top_products = pd.merge(top_products, data_cleaned[['StockCode', 'Description']].drop_duplicates(),
                        on='StockCode', how='left')

#PARA UNIR  GRAFICAS EN UNA SOLA

#CREACIÓN DEL DASHBOARD 

plt.figure(figsize=(16, 12)) # Ajustamos un poco el tamaño para acomodar los 4

# Gráfico 1: Pastel de devoluciones (Arriba Izquierda)
plt.subplot(2, 2, 1) 
labels1 = ['Devoluciones', 'No Devoluciones']
sizes1 = [total_returns, total_non_returns]
plt.pie(sizes1, labels=labels1, colors=['lightcoral', 'lightgreen'], startangle=140, autopct='%1.1f%%')
plt.title('Transacciones con y sin devolución')

# Gráfico 2: Pastel de categorías (Arriba Derecha)
plt.subplot(2, 2, 2) 
plt.pie(category_counts.values, labels=category_counts.index, 
        colors=['lightskyblue', 'gold', 'lightcoral'], startangle=140, autopct='%1.1f%%')
plt.title('Distribución por Categoría de Monto')

# Gráfico 3: Barras de ventas por fecha (Abajo Izquierda)
plt.subplot(2, 2, 3) 
# Cambiamos a posición 3 (esquina inferior izquierda)
data_cleaned.groupby(['Year', 'Month'])['TotalAmount'].sum().plot(kind='bar', color='steelblue')
plt.title('Distribución de Ventas por mes y año')
plt.xlabel('Año, Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)

# Gráfico 4: Top 10 Productos (Abajo Derecha)
plt.subplot(2, 2, 4)
# Usamos .astype(str).str[:30] para recortar los nombres largos a 30 caracteres y que no se encimen
descripciones_cortas = top_products['Description'].astype(str).str[:30]
plt.barh(descripciones_cortas, top_products['Quantity'], color='mediumseagreen')
plt.title('Top 10 Productos más Vendidos')
plt.xlabel('Cantidad Vendida')
plt.ylabel('Producto')

# Ajustar diseño para que todo encaje perfecto y mostrar
plt.tight_layout()
plt.show()