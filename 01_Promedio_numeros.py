# Este codigo halla el promedio entre los numeros ingresados en el codigo
# This code find the average among the numbers entered in the code
n = int(input('set a number:    '))
end = ""
list = []
sum = 0
con = 0

while n != end:
    con = con + 1
    sum = sum +n
    list.append(n)
    n = (input('set a number again or press enter to finish:     '))
    if n == end:
        n = end
    else:
        n = int(n)

avg = sum/con
print(avg)