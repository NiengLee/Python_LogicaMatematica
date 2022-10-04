#   Grafico de la campana de gauss
#   Gauss bell plot
import os
import matplotlib.pyplot as plt
import numpy as np

def campanagauss(x, sigma, nu):
    pt1 =  1/(sigma*((2*3.1416)**0.5))
    pt2 = 2.718281**((-0.5) * (((x-nu)/sigma)**2))
    y   = pt1*pt2
    return y

x = []
y = []
for i in np.arange(20, 30, 0.1):
    x.append(i)
    f_x = campanagauss(i, 3.2, 25)
    y.append(f_x)

#print('\n',x)
#print('\n',y)

plt.plot(x, y, color='#303496', marker='o', linestyle= 'solid')
plt.show()