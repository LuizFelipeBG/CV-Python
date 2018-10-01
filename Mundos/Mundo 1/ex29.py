ve = float(input('Velocidade do Carro: '))

if ve > 80:
    multa = (ve - 80)* 7
    print('Você foi multado e vai pagar R$ {} de multa'.format(multa))
else:
    print('Tá suave!kk')
