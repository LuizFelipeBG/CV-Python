sal = float(input('Informe seu salário: '))

if sal <= 1200:
    nsal = ((sal/100)*10) + sal
    print('Seu novo salario é de R$ {}'.format(nsal))
else:
    nsal = ((sal/100)*15) + sal
    print('Seu novo salário é de R$ {}'.format(nsal))