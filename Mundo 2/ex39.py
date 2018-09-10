ida = int(input('Digite o ano do seu nascimento: '))

if 2018 - ida < 18:
    fal = 2018 - ida
    print('Você deve se alistar daqui a {} anos'.format(18 - fal))
elif 2018 - ida > 18:
    pos =  2018 - ida
    print('Você deveria ter se alistado a {} anos'.format(pos - 18))
else:
    print('Você deve se alistar esse ano')
