import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

sel= [n1, n2, n3, n4]
ran = random.choice(sel)

print('O aluno escolido foi {}'.format(ran))
