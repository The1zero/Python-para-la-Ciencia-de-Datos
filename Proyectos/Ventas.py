#Graficar ventas mensuales
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter


#creando info de las fechas
dates=pd.date_range(start='2023-01-01', periods=12, freq='M')
sales=np.random.randint(1000,5000, size=12)

sales_data=pd.DataFrame=({'Date':dates, 'Sales':sales})
#crear figura
plt.plot(sales_data['Date'], sales_data['Sales'], marker='o',
         linestyle='-',label='Ventas Mensuales')

plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))

plt.xticks(rotation=45)
plt.title('Ventas mensuales')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.legend()
plt.tight_layout()
plt.show()
