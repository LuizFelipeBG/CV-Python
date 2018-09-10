num1 = 0
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
       num1 += num
print('A soma dos números pares é {}'.format(num1))