frase = input('Digite um frase: ').lower()
con = frase.count('a')
fin = frase.find('a')
finr = frase.rfind('a')

print('A letra "a" apareceu {} vezes, sendo que apareceu primeiro na posição {} e apareceu por ultimo na posição {}'.format(con,fin,finr))