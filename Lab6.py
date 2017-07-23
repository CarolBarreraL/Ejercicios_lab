import numpy as np
import matplotlib.pyplot as plt


espacio=1000
x = np.linspace(0,1,espacio)
dt=0.0005
dx= 1/float(espacio-1)
c=1.0
gamma = c*dt/dx
tiempo = 400

u0= np.exp(-((x-0.3)*(x-0.3))/0.01)
u0[0]=0
u0[-1]=0

uInicial = np.copy(u0)
#Para t=0
u1 = np.ones(espacio)
u1[0]=0
u1[-1]=0
for i in range(1,espacio-1):
	u1[i]= u0[i]+ gamma*gamma/2*(u0[i+1]-2*u0[i]+u0[i-1])

#Para t=1
u2 = np.ones(espacio)
u2[0]=0
u2[-1]=0

t=0
ut =[]
while t<tiempo:
	for i in range(1,espacio-1):
		u2[i]=2*(1-gamma*gamma)*u1[i]-u0[i]+gamma*gamma*(u1[i+1]+u1[i-1])
	u0 = np.copy(u1)
	u1 = np.copy(u2)
	ut.append(u2)
	t+=1
	


plt.plot(x,uInicial, 'c')
#plt.plot(x,u1)
#plt.plot(x,u2, 'g')
plt.plot(x,ut[50])
plt.plot(x,ut[250], 'k')
plt.show()



