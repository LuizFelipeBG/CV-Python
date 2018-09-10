casa = float(input('Valor da Casa? '))
sal = float(input('Seu salário? '))
anos = int(input('Em quantos anos? '))

psal = (sal/100)*30
pmes = anos*12

qt = casa / pmes

if qt > psal:
    print('Credito negado')
else:
    print('Credito aceito e você pagará R$ {} por mês'.format(qt))