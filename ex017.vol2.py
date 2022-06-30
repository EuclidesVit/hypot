# Maneira de calcular a hipotenusa atraves da importaçao "hypot"

print('Olá, bem vindo(a) ao calculo da hipotenusa!!')
from math import hypot

co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
