from math import factorial
num = int(input('Digite um número: '))
fa = num
while  fa > 0:
    print('{}'.format(fa), end=' ')
    print(' x ' if fa > 1 else ' = ' ,end=' ')
    fa-=1
print(factorial(num), end=' ')
    