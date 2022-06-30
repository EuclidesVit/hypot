# Maneira de calcular a hipotenusa de modo tradicional, sem a importaçao

print('Olá, bem vindo(a) ao calculo da hipotenusa!!')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
