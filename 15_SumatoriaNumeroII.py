#   This code sum all numbers from 1 to n

def sum_n( n ):
    s = (1+n)*(n/2)
    return s

n = int(input('\nnumber:   '))
result = sum_n(n)

print(result)