"""
Leia 100 valores inteiros. Apresente então o maior valor lido e
a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
"""
lista = {}
cont=0
maior=0
while cont<100:
    n=int(input())
    if n >maior:
        maior=n
        lista[maior] = cont #determina o valor do indice da lista atribuindo a varivel conte na lista[n]
    cont+= 1
print (maior)
print (lista[maior]+1)#incrementa 1 ao indice da lista pois a lista sempre inicia em 0
