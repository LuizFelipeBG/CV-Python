a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
an = a1
for c in range(1,11):
    print(an)
    an = a1 + (c * r)
