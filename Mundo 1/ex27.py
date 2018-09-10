nome = input('Digite seu nome: ')
splnome = nome.split()
pnome = splnome[0]
unome = splnome[len(splnome) - 1]

print('Primeiro nome: {}, último nome: {}'.format(pnome,unome))