#   Este codigo determina la devolución de una compra, devolviendo la menor cantidad de monedas posibles
#   This code has errors
pay = int(input(' How much money do you have?  :  '))
cost = int(input(' How much money does it cost?  :  '))

chan =  pay - cost

print('the exchange is  :  {}'.format(chan))

one_thousand_coin = chan / 1000
five_hundred_coin = (chan%1000) / 500
two_hundred_coin = ((five_hundred_coin)%500) / 200
one_hundred_coin = ((two_hundred_coin)%200) / 100
fifty_coin = ((one_hundred_coin)%100) / 50
lost = one_hundred_coin%50

print('coins of 1000 .............{:.0f}'.format(one_thousand_coin))
print('coins of 500 .............{:.0f}'.format(five_hundred_coin))
print('coins of 200 .............{:.0f}'.format(two_hundred_coin))
print('coins of 100 .............{:.0f}'.format(one_hundred_coin))
print('coins of 50 .............{:.0f}'.format(fifty_coin))

if lost > 0:
    print('the quantity of money that can´t be exchanged is: ...........{}'.format(lost))