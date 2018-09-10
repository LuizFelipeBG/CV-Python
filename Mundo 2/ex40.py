nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

med = (nota1 + nota2) / 2

if med < 5:
    print('Reprovado')
elif 5 < med < 6.9:
    print('Recuperação')
else:
    print('Aprovado')
