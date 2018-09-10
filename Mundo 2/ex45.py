import random
pla = input('pedra, papel ou tesoura: ')
lis = ['pedra','papel','tesoura']
maq = random.choice(lis)

if (maq == 'pedra' and pla == 'papel') or (maq == 'tesoura' and pla == 'pedra') or (maq == 'papel' and pla == 'tesoura'):
    print('Você venceu')
else:
    print('Você perdeu')