import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

#Crear data set de ejemplo con pandas con un rango de fechas pero que inicie como yo le diga(año,mes,dia) y 100 fechas
dates=pd.date_range(start='2023-01-01', periods=100)

#crear valores representando la suma acumulada
values= np.random.rand(100).cumsum()

#data con las fehcas y valores generados
data=pd.DataFrame({'Date': dates, 'Values': values})

#Graficación con lineas
fig, ax = plt.subplots(figsize=(12,6)) 
#quiero una grafica en base al tiempo 
ax.plot(data['Date'], data['Values'],color='green')

plt.xticks(rotation=45)

plt.title('Serie de tiempo con formato en las fechas')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()