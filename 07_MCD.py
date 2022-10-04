#   Este codigo determina el Maximo común divisor entre dos numeros

n = 36
m = 48

if m<n:
    d = m
else:
    d = n

while (m%d!=0) or (n%d!=0):
    d = d-1

print(d)