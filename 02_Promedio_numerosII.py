#   Este codigo determina el promedio de numeros ingresados, con ciclo while
#   This is the exercise number 61: Average

n = int(input('\nEnter the first number = '))
s = 0
c = 0

while n == 0:
    n = int(input('\n0 IS NOT AN ALLOWED VALUE,\nplease enter the first number different than 0 = '))
while n != 0:
    s = s + n
    c = c + 1
    n = int(input('\nadd 0 to finish the loop.\nadd other desired number = '))

AVG = s/c
print('\nthe average beetween all the numbers entered is {}'.format(AVG))