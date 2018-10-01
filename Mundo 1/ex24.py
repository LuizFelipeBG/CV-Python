city = input('Digite o nome da sua cidade: ').lower()

spl = city.split()
find = 'santo' in spl[0]
print('Sua Cidade começa com Santo? {}'.format(find))
