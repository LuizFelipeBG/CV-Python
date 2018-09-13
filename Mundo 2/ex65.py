n = False
maior = menor = c = 0
media = sum = 0
while n != True:
    n1 = int(input('Digite um número: '))
    c +=1
    if c == 1:
        maior = menor = n1
        sum =+ n1
        media = sum/c
    else:
        sum += n1
        media = sum / c
        if n1 < menor:
            menor = n1
        if n1 > maior:
            maior = n1
    op = input('Deseja continuar?[S/N] ').upper()
    if op == 'N':
        n = True

print('O maior número foi {}, o menor foi {} e a media dos números foi {:.2f}'.format(maior,menor,media))
    
    
