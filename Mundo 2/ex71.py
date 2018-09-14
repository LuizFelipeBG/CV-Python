valor = int(input('Digite o valor a ser sacado: '))
c50 = c20 = c10 = c1 = 0

while True:    
    if valor - 50 >= 50:
        c50 += 1
        valor -= 50
    else:
        break

while True:
    if valor - 20 >= 20:
        c20 += 1
        valor -= 20
    else:
        break

while True:
    if valor - 10 >= 10:
        c10 += 1
        valor -= 10
    else: 
        break

while True:
    if valor - 1 >= 1:
        c1 += 1
        valor -= 1
    else:
        break

print('--------------------------FIM DO PROGRAMA-----------------------------------------------------')
print(f'{c50} notas de 50, {c20} notas de 20, {c10} notas de 10, {c1} notas de 1')