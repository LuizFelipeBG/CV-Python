r1 = int(input('primeira reta: '))
r2 = int(input('segunda reta: '))
r3 = int(input('terceira reta: '))

if (r1 - r3) < r1 < r2+r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print('Pode ser Triangulo')
else:
    print('Não pode ser Triangulo')
