#p1,n1,v1 = input().split(' ')
cod, qtd, vlrUnit = input().split(' ')
cod = int(cod)
qtd = int(qtd)
vlrUnit = float(vlrUnit)

cod1, qtd1, vlrUnit1 = input().split(' ')
cod1 = int(cod1)
qtd1 = int(qtd1)
vlrUnit1 = float(vlrUnit1)

vlrTot = (qtd*vlrUnit)+(qtd1*vlrUnit1)

print ("VALOR A PAGAR: R$ {:.2f}".format(vlrTot))
