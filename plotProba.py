import numpy as np
import matplotlib.pyplot as plt

final = np.genfromtxt('final.csv', delimiter=',')

tiempo= final[:,0]
uProm = final[:,1]
uUnaVez = final[:,2]
uFormal = final[:,3]

plt.plot(tiempo, uFormal,'c', label ='La que es')
plt.plot(tiempo, uUnaVez, 'r',label = 'Una vez')
plt.plot(tiempo,uProm, 'k', label ='Promedio')
plt.legend(loc=0)
plt.show()
