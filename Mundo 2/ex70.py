costb = total = mais = cont = 0
barato = ''
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    conti = input('Quer continuar?[S/N] ').upper()
    if conti != 'N':
        cont+=1
        if cont == 1:
            costb = preco
            barato = nome
            total += preco
            if preco > 1000:
                mais += 1
        else:
            total += preco
            if preco > 1000:
                mais += 1
            elif preco < costb:
                costb = preco
                barato = nome
    else:
        total += preco
        if preco > 1000:
            mais += 1 
        elif preco < costb:
            costb = preco
            barato = nome
        break
print('-------------------------- FIM DO PROGRAMA -------------------------------')

print(f'O total da compra foi {total},com {mais} produtos que custam mais de 1000 reais e o mais barato foi o produto {barato}')