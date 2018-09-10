num = int(input('Informe so número: '))

uni = num // 1 % 10
dez = num // 10 % 10
cem = num // 100 % 10
mil = num // 1000 % 10

print('Unidade  = {}, Dezena = {}, Centena = {} e Milhar = {}'.format(uni,dez,cem,mil))