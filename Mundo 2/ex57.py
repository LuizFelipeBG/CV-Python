from random import randint

c = 0
t = 1
while t != randint(1,10):
    ten = int(input('tente acertar o número: '))
    c += 1 
print('Você tentou {} vezes até acertar!!'.format(c))
