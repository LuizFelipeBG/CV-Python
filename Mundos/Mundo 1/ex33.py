n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
maior = 0 
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2> n3:
    maior = n2
if n3 > n1 and n3> n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('Menor número = {} e maior número = {}'.format(menor,maior))
