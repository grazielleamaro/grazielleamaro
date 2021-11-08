"""
Escreva um programa que leia um número inteiro e apresente na tela se ele
é par ou ímpar (para determinar se um número é par ou ímpar verifique se o
resto da divisão dele por 2 é zero ou não. Para isso use o operador % para
calcular esse resto).
"""

a = int(input("Digite um número inteiro: "))

if a%2 == 0:
    print ("O número", a, "é um número par")
else:
    print ("O número", a, "é um número impar")
