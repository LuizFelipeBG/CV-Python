maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {} e o menor foi {}'.format(maior,menor))