#grafico de dispersion: Muestra la relación entre dos variables, cada punto representa una observación.
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))

hours_study=[2,3,4,5,6,7,8]
score_student1=[55,60,65,70,75,80,85]
score_student2=[50,58,63,69,74,78,83]

#para graficar este de dispersion de dos estudiantes
#plt.scatter(hours_study,score_student1,marker='o',color='green',label='Estudiante 1')
#plt.scatter(hours_study,score_student2,marker='s',color='blue',label='Estudiante 2')

#Con el de lineas
#para graficar este de dispersion de dos estudiantes
plt.plot(hours_study,score_student1,marker='o',color='green',linestyle='-',linewidth = 2,label='Estudiante 1')
plt.plot(hours_study,score_student2,marker='s',color='blue',linestyle='--',linewidth = 2,label='Estudiante 2')

plt.title('Relacion entre horas estduiadas y puntaje de dos estudiantes')

plt.xlabel('Horas de estudio')
plt.ylabel('Puntaje')
plt.legend(loc='upper left', fontsize=10, frameon=True)#para que funcione label

plt.show()