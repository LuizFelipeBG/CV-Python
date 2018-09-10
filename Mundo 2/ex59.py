num = int(input('Digite um número: '))
fa = 0
while num != 0:
    fa = (num - 1) * num
    num -= 1
    print('{}'.format(fa))