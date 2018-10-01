dis = float(input('Digite a Distancia em Km: '))

if dis <= 200:
    preco = dis * 0.50
    print('A passagem é de R$ {}'.format(preco))

else:
    preco = dis * 0.45
    print('A passagem é de R$ {}'.format(preco))
