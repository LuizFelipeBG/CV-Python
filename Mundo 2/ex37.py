
num = int(input('Digite um número: '))
con = int(input('Conversão -> 1-Binario / 2-octal / 3-hexadecimal: '))

if con == 1:
    print('O número em binario é: {}'.format(bin(num)))
elif con == 2:
    print('O número em octal é: {}'.format(oct(num)))
elif con == 3:
    print('O número em octal é: {}'.format(hex(num)))
else:
    print('Opção invalida')


