cont = 0
pos = 0
while cont<6:
    a=float(input())
    if a>0:
        pos=pos+1
        cont = cont+1
    else:
        cont = cont + 1
print ("{} valores positivos".format(pos))
