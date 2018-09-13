from random import randint
cont = 0
rand = 0
while True:
    rand = randint(1,10)
    n = int(input('Digite seu número: '))
    pi = input('Par ou Ìmpar?[P/I] ').upper()
    if pi =='P':
        if (n + rand) % 2 == 0:
            cont += 1
            print(f'Você ganhou,Seu número foi {n} e o computador foi {rand} e é par!! ')
        else:
            break
    if pi == 'I':
        if (n + rand) % 2 != 0:
            cont += 1
            print(f'Você ganhou,Seu número foi {n} e o computador foi {rand} e é ímpar!!')
        else:
            break
    
print(f'Você ganhou {cont} vezes!!')
