#   este codigo determina los multiplos de cierto numero, en un rango dado de numeros
#   this program gets all multiples of a certain number from a number to number
i = int(input('\nset starting number:  '))
e = int(input('set the final number:  '))
m = int(input('set the number that we will find its multiples:  '))

list = []

for a in range(i,(e+1)):
    if a % m == 0:
        list.append(a)
        print(a)