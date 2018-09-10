c1 = 0
c2 = 0
for c in range(1,8):
    nas = int(input('Digite a data de nascimento: '))
    if 2018 - nas > 18:
        c1 += 1
    else:
        c2 += 1
print('existem {} pessoas que já são maiores de idade e {} que ainda não atingiram a maioridade!!'.format(c1,c2))
