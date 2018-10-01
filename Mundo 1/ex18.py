from math import sin,cos,tan,radians
ang = float(input('digite o ângulo que você deseja: '))
radins = radians(ang)
seno = sin(radins)
cose = cos(radins)
tang = tan(radins)

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cose))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang,tang))