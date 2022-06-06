"""
6. Escreva um programa que leia o nome de um
lutador e seu peso. Em seguida informe a
categoria a que pertence o lutador, conforme a
tabela ao lado (note que a tabela foi criada para
efeito deste exercício e não condiz com
qualquer categoria de luta). A saída do
programa deve exibir na tela um texto no
seguinte padrão:
Nome fornecido: Pepe Jordão
Peso fornecido: 73.4
Saída exibida na tela: O lutador Pepe Jordão pesa 73.4 kg e
se enquadra na categoria Ligeiro
"""

nome = str(input("Digite o nome do lutador: "))
peso = float(input("Digite o peso do lutador: "))

if peso < 65.0:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Pena.")
elif peso >= 65 and peso < 72:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Leve.")
elif peso >= 72 and peso < 79:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Ligeiro.")
elif peso >= 79 and peso < 86:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Meio Médio.")
elif peso >= 86 and peso < 93:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Médio.")
elif peso >= 93 and peso < 100:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Médio Pesado.")
else:
    print ("O lutador,", nome, "pesa,", peso, "e se enquadra na categoria Pesado.")
