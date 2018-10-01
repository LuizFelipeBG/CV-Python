d = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km percorridos? '))

pd = 60 * d
pkm = km * 0.15

total = pd + pkm

print('Você irá pagar R$ {} por todos os dias mais R$ {} pelos Km rodados, total = R$ {}'.format(pd,pkm,total))