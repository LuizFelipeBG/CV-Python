cont = sum = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    sum += n
    cont += 1
print(f'Você digitou {cont} números e a soma foi {sum}.')
