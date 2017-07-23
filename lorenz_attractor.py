import numpy as np
import matplotlib.pyplot as plt



#SIN DEFINIR UNA FUNCION
puntos=4000
x=np.ones(puntos)
x_prim= np.ones(puntos)
y=np.ones(puntos)
y_prim= np.ones(puntos)
z=np.ones(puntos)
z_prim= np.ones(puntos)

#constantes
sigma = 10.0
ro = 28.0
beta = 8/3.0

#Condiciones iniciales
x[0]=1
x_prim[0]=1
y[0]=1
y_prim[0]=sigma*(y[0]-x[0])
z[0]=x[0]*(ro - z[0]) - y[0]
z_prim[0]=x[0]*y[0]- beta*z[0]

h=4.0/puntos

c=1
while c<(puntos):
	x[c]= x_prim[c-1]*h+ x[c-1]
	y[c]= y_prim[c-1]*h+ y[c-1]
	z[c]= z_prim[c-1]*h+ z[c-1]

	x_prim[c]= sigma*(y[c]-x[c])
	y_prim[c]= x[c]*(ro - z[c]) - y[c]
	z_prim[c]= x[c]*y[c]- beta*z[c]

	c+=1





