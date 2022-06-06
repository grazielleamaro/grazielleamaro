"""
5. Escreva um programa que leia um número inteiro
e informe se o mesmo é positivo, zero ou negativo.

"""

x = int(input("Insira um número: "))

if x == 0:
    print ("O número inserido é zero.")
elif x<0:
    print ("O número inserido é negativo.")
else:
    print ("O número inserido é positivo.")
