import random
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1,n2,n3,n4]

listr = random.shuffle

print('A ordem é {}'.format(lista))