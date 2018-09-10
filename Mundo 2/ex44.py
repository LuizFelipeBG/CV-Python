preco = float(input('Preço do produto: '))
met = int(input('1 - A vista dinheiro/cheque , 2 - À vista no cartão , 3 - 2x no cartão , 4 - 3x ou mais no cartão: '))

if met == 1:
    npreco = preco - (preco/100)*10
    print('Você pagará R$ {} pelo produto'.format(npreco))
elif met == 2:
    npreco = preco - (preco/100)*5
    print('Você pagará R$ {} pelo produto'.format(npreco))
elif met == 3:
    print('Você pagará o preço normal do produto')
elif met == 4:
    npreco = preco + (preco/100)*20
    print('Você pagará R$ {} pelo produto'.format(npreco))
