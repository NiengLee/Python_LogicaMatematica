#   Es un tablero de ajedrez, el codigo sirve para descifrar el color de la casilla dadas las coordenadas
#   This code predict the color in tile given a letter-number coordinates

n = 7       # --- insert number of the row
l = 'd'     # --- insert letter of the column

if (n == 1) | (n == 3) | (n == 5) | (n == 7):
    if (l == 'a') | (l == 'c') | (l == 'e') | (l == 'g'):
        print('\nthe square with coordinates {},{} has BLACK color'.format(n,l))
    else:
        print('\nthe square with coordinates {},{} has WHITE color'.format(n,l))

else:
    if (l == 'a') | (l == 'c') | (l == 'e') | (l == 'g'):
        print('\nthe square with coordinates {},{} has WHITE color'.format(n,l))
    else:
        print('\nthe square with coordinates {},{} has BLACK color'.format(n,l))