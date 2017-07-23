import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('datos.csv', delimiter=',')

time = datos[:,0]
u = datos[:,1]
uInicial = datos[:,2]


plt.plot(time,uInicial, label = 'U inicial', c='k')
plt.plot(time,u, label = 'U final', c='c')
plt.title('Conveccion lineal')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.legend(loc=0)
plt.savefig('Ecuacion_de_Conveccion_lineal.pdf')

