mm = ''
mi = 0
mv = 0
cont = 0
for c in range(1,5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Seu sexo: ').upper()
    if sexo[0] == 'M':
        if c == 1:
            mi = idade
            mm = nome
        elif idade > mi:
            mm = nome
    elif sexo[0] == 'F':
        if idade < 20:
            mv += 1
    cont += idade 
print('O homem mais velho é {}, existem {} mulheres com menos de vinte anos e a media do grupo é {}'.format(mm,mv,cont/4))
