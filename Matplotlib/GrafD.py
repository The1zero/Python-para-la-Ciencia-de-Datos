#grafico de dispersion: Muestra la relación entre dos variables, cada punto representa una observación.
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))

hours_study=[2,3,4,5,6,7,8]
score=[55,60,65,70,75,80,85]

#para graficar este de dispersion
plt.scatter(hours_study,score,color='green')#scatter es para graficar de dispersion, despues va la variable x y la variable y, y al final el color

#agregar titulo
plt.title('Relacion entre horas estduiadas y puntaje')
#agregar etiquetas a los ejes
plt.xlabel('Horas de estudio')
plt.ylabel('Puntaje')

plt.show()