from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = sqrt((ca**2) + (co**2))

print('A hipotenusa vai medir {:.2f}'.format(hi))