import numpy as np
import matplotlib.pyplot as plt

#SIN DEFINIR UNA FUNCION
puntos=3000
x=np.ones(puntos)
x_prim= np.ones(puntos)
x_2prim=np.ones(puntos)

#Condiciones y constantes
x_0 = 0.2
xprim_0 = 0.0
k=42.0
g=9.8
m=0.25
mu=0.15

x[0]= x_0
x_prim[0] = xprim_0
x_2prim[0] = -(k/m)*x_0 + mu*g

h=3.0/puntos

c=1
while c<(puntos):
	x[c]= x_prim[c-1]*h+ x[c-1]
	x_prim[c]= x_2prim[c-1]*h + x_prim[c-1]
	if x_prim[c]>0:
		x_2prim[c] = -(k/m)*x[c] - g*mu
	else:
		x_2prim[c] = -(k/m)*x[c] + g*mu
	c+=1

plt.subplot(3,1,1)
plt.plot(x, 'c', label='Posicion')
plt.subplot(3,1,2)
plt.plot(x_prim, 'r', label='Velocidad')
plt.subplot(3,1,3)
plt.plot(x_2prim, 'k', label='Aceleracion')
plt.show()

