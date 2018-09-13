n = 0
c = 0
t = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        t = t
    else:
        t += n
        c += 1
print('Você digitou {} números e a soma deles é {}!!'.format(c,t))