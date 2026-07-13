#SUBPLOTS Y LAYOUTS AVANZADOS

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

x = np.linspace(0,10,100)
y = np.sin(x)

data = np.random.randn(100)

#Objeto que vamos agenerar y vamos ir agregando
gs = gridspec.GridSpec(2,2, height_ratios=[2,1], width_ratios=[1,1])
fig=plt.figure(figsize=[10,8])

#Primer subplot grande, ocupa toda la primer fila
ax1=fig.add_subplot(gs[0,:])
ax1.plot(x,y,color='blue')
ax1.set_title('Seno de x')
ax1.set_xlabel('x')
ax1.set_ylabel('Sin(x)')

#Segundo subplot, ocupa la esquina inferior izquierda
ax2=fig.add_subplot(gs[1,0])
ax2.hist(data, bins=20, color= 'purple', edgecolor= 'black')
ax2.set_title('Histograma')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Frecuencia')

#Tercer subplot esquina inferior derecha
ax3=fig.add_subplot(gs[1,1])
ax3.scatter(x,y, color='red')
ax3.set_title('Dispersion de Seno')
ax3.set_xlabel('x')
ax3.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()