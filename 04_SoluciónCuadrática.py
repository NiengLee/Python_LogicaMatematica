#   Este codigo grafica una ecuación de grado 2, y determina las raices
#   This code plot a grade 2 equation given numeric coefficients, and find the roots of this equation
import matplotlib.pyplot as plt

a = 1
b = -8
c = 15

discr = (b**2) - (4*a*c)

def cuadratic_fun(x, a, b, c):
    y = (a*(x**2)) + (b*x) + c
    return y

if discr > 0:
    x_1 = (-b + (discr**0.5)) / (2*a)
    x_2 = (-b - (discr**0.5)) / (2*a)
    print('\nthe 2nd grade equation with a = {}, b = {} and c = {} has two roots,\nand they are {} and {}'.format(a, b, c, round(x_1,2),round(x_2,2)))
elif discr == 0:
    x = -b / (2*a)
    print('\nthe 2nd grade equation with a = {}, b = {} and c = {} has one root,\n and it is {}'.format(a,b,c,x))
else:
    print('\nthe 2nd grade equation with a = {}, b = {} and c = {} has no roots'.format(a,b,c))

x = range(-10, 11)
y = []

for i in x:
    y.append(cuadratic_fun(i, a, b, c))

plt.plot(x, y)
plt.show()