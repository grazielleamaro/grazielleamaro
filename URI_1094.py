"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e
precisa de sua ajuda para organizar os experimentos de um laboratório
o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias
foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias:
sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente
o número de experimentos que foram realizados, o tipo de cobaia utilizada e a
quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários
casos de teste que vem a seguir. Cada caso de teste contém um inteiro
Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas
e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia
(R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia
utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas,
sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
"""
n = int(input())
lista = []
cont=0
s=0
r=0
c=0
total=0
ps = 0
pr = 0
pc = 0

while cont<n:
    quantia, tipo = input().split(' ')
    quantia = int(quantia)
    tipo = str(tipo)
    if 1<=quantia<=15:
        total = total + quantia
        cont += 1
        if tipo == 'S' or tipo == 's':
            s = s + quantia
        elif tipo == 'R' or tipo == 'r':
            r = r + quantia
            
        elif tipo == 'C' or tipo == 'c':
            c = c + quantia
            
ps =(s*100)/total
pr =(r*100)/total
pc =(c*100)/total
print ("Total: {} cobaias".format(total))
print ("Total de coelhos:", c)
print ("Total de ratos:", r)
print ("Total de sapos:", s)
print ("Percentual de coelhos: {:.2f} %".format(pc))
print ("Percentual de ratos: {:.2f} %".format(pr))
print ("Percentual de sapos: {:.2f} %".format(ps))
print ("Fim")
