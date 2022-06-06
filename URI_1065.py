cont = 0
par = 0
while cont<5:
    a=float(input())
    if a%2==0:
        par=par+1
        cont = cont+1
    else:
        cont = cont + 1
print ("{} valores positivos".format(par))
