cm = ch = mi = 0
while True:
    sexo = input('Digite seu sexo:[M/F] ').upper()
    i = int(input('Digite sua idade: '))
    if i >= 18:
        mi += 1
    if sexo == 'M':
        ch += 1
    if sexo == 'F' and i <= 20:
        cm += 1
    op = input('Quer continuar?[S/N] ').upper()
    if op == 'N':
        break
    
print(f'Você digitou {mi} maiores de idade, {ch} Homens e {cm} mulheres com menos de 20 anos')

