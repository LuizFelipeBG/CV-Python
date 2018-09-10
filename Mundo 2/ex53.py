fra = input('Digite a frase: ')
con = ''
for c in range(len(fra)-1,-1, -1):
    con += fra[c]

f = fra.split()
fa = ''.join(f)
spl = con.split()
sp = ''.join(spl)


if fa == sp:
    print('Essa Frase é um palíndromo!!')
else:
    print('Essa frase não é um palíndromo!!')