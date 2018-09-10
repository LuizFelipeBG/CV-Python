from random import randint
num = int(input('Digite um número inteiro de 0 a 5: '))
ran = randint(0 ,5)
print('O numero do computador foi {} e o seu Foi {}'.format(ran,num))
if ran == num:
    print('Você Gamhou!!')
else:
    print('Você Perdeu!!')


