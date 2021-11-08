"""
3. Escreva um programa que leia dois números quaisquer
e mostre na tela qual é o menor e qual é o maior.
"""

a = int(input("Digite um número: "))
b = int(input("Digite outro número:"))
if a < b:
    print ("O número", a, "é maior que", b)
else:
    print ("O número", b, "é maior que", a)
