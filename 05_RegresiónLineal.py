#   este codigo encuentra la pendiente y el intercepto de la regresión lineal de puntos
#   This code find slope and intercept of a linear regression
import matplotlib.pyplot as plt
from random import randint, random

x = []
y = []
#x = [1, 2, 3]
#y = [1, 2.1, 2.9]
for i in range(150):
    x.append(random()*10000)
    y.append(random()*80)

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0
min_x = min(x)
max_x = max(x)
xfit = [min_x, max_x]

for i in range(len(x)):
    sum_x = sum_x + x[i]
    sum_y = sum_y + y[i]
    sum_xy = sum_xy + (x[i]*y[i])
    sum_x2 = sum_x2 + (x[i]**2)

avg_x = sum_x / (len(x))
avg_y = sum_y / (len(y))
m_pend = ( sum_xy - ((sum_x*sum_y)/ len(x)) ) / ( sum_x2 - ((sum_x **2) / len(x)) )
b_inte = avg_y - (m_pend*avg_x)

min_y = (m_pend*min_x) + b_inte
max_y = (m_pend*max_x) + b_inte
yfit= [min_y, max_y]

print('\nthe lineal function that represent the lineal regression of\nthe data is:\nY = {}X + {:.2f}'.format(m_pend,b_inte))

plt.scatter(x, y, s = 2)
plt.plot(xfit, yfit, c = 'red')
plt.show()