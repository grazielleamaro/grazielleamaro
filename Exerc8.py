"""
Escreva um programa que leia três números reais e informe se eles constituem os
lados de um triângulo.
Em caso afirmativo, informe se o triângulo é equilátero, isósceles ou escaleno.
Para que três números formem um triângulo deve ocorrer que a soma dos dois
lados menores deve ser maior que o lado maior.
Para resolver essa questão será preciso usar os operadores and e or.
Colocar este programa no site do professor.
"""
a = float(input("Insira o primeiro valor: "))#1
b = float(input("Insira o segundo valor: "))#2
c = float(input("Insira o terceiro valor: "))#3

if a+b<=c or b+c<=a or a+c<=b:
     print ("Não é possível constituir um trângulo") 

elif a==b and b==c:
    print("Os valores inseridos constituem um triângulo Equilátero.")
elif a!=b and b!=c and a!=c:
    print("Os valores inseridos constituem um Escaleno")
else:
    print("Os valores inseridos constituem um triângulo Isóceles.")
