#   algoritmo para determinar la raíz cuadrara de un numero por algoritmo
#   This code find the square root of a  number

x = 25   # int(input('\nset a number:  '))
guess = x/2
dif=1

while dif > (10**-12):
    guess = (1/2)*(guess + (x / guess))
    dif = (guess*guess) - x

print(guess)