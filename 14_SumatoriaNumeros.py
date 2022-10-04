#   This code sum numbers from 1 to n

def sumahasta(n):
    k = 0
    i = 0
    li = []
    lk = []
    while i <= n :
        i = i + 1
        k = k + i
        li.append(i)
        lk.append(k)

    if k == n:
        return('\nla suma desde el 1 hasta {}, dio exactamente {}, y el ultimo numero fue {}'.format(n,lk[-2],li[-2]))
    else:
        return('\nla suma desde el 1 hasta {}, dio {}, y el ultimo numero fue {}'.format(n,lk[-2],li[-2]))

n = int(input('\ningrese el valor de n:  '))
print(sumahasta(n))
