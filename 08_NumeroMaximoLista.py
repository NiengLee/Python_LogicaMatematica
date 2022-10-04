#   Este codigo determina el valor mas alto de una lista con numeros aleatorios
#   Find the highest value from a random numbers in a list

import random

k = 16
max = 0
cont = 0
list = []

for i in range(k):
    val = int(random.random() * 999999)
    list.append(val)

for i in range(k):
    if list[i] > max:
        max = list[i]
    cont =cont+1


print(cont)
print(max)