"""
Escreva um programa que leia três números reais A, B e C
que são os coeficientes de uma equação do 2º grau (A.x2 + B.x + C = 0).
Calcule e apresente na tela as raízes dessa equação, considerando os três
casos possíveis:
Delta maior que zero (duas raízes reais),
Delta igual a zero (uma raiz) e
Delta menor que zero (não há raízes reais).
"""
a = float(input("Insira um número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))

delta = b**2 - 4*a*c

if  delta > 0:
    x = (- b + delta**0.5)/(2*a)
    y = (- b - delta**0.5)/(2*a)

    print ("A equação possui duas raizes possíveis que são:", x, "e",y)

elif delta == 0:
    
    x=(-b+delta**0.5)/(2*a)

    print ("A equação possui uma raiz possível que é:", x)

else:

    print ("A equação não possui raízes possiveis.")
