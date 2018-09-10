nas = int(input('Data de nascimento: '))

ida = 2018 - nas

if ida <= 9:
    print('MIRIM')
elif 9 < ida <= 14:
    print('INFANTIL')
elif 14 < ida <= 19:
    print('JUNIOR')
elif 19 < ida <= 20:
    print('SÊNIOR')
else:
    print('MASTER')