import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from scipy.stats import norm

#Variable aleatoria
n = []
ja=10.0
n = np.random.exponential(1/ja,1000)
plt.hist(n, normed= True, bins=20)


a,b = expon.fit(n) # nos da (loc,scale)
x= np.linspace(0,1,1000)
y = expon.pdf(x, a,b)
plt.plot(x,y)


#Teorema del limite central
lista = []
m=0
while m <=1000:
	lst = np.random.exponential(0.1, 1000)
	v=np.sum(lst)
	lista.append(v)
	m+=1
#plt.hist(lista, normed = True, bins= 20)


c,d = norm.fit(lista)
w= np.linspace(0,250,1000)
q=norm.pdf(w,c,d)
#plt.plot(w,q)
plt.show()
