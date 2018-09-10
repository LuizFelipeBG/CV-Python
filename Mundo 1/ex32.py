ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('Não é bissexto')