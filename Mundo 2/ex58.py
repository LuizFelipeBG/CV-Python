n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

c = 1
n3 = 0
while 0 == n3:
    d = int(input('[1]Somar, [2]Multiplicar, [3]Maior, [4]Novos Números, [5]Sair : '))
    if d == 1:
        print(n1 + n2)
    if d == 2:
        print(n1 * n2)
    if d == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print('O maior é', maior)
    if d == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    if d == 5:
        n3 = 1

