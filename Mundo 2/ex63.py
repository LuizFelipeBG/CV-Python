n = int(input('Digite um número: '))
f = 0
t = 0
g = 2 
while f < n/2:
    f += 1
    g = g + t
    t = g + (t + 1)
    print(g,t, end=' ')