cont = 0
pos = 0
neg = 0
par = 0
impar = 0
while cont<5:
    a=float(input())
    cont = cont+1
    if a<0:
        neg = neg+1
        if a%2==0:
            par = par+1
        else:
            impar = impar+1
    elif a>0:
        pos = pos+1
        if a%2==0:
            par = par+1
        else:
            impar = impar+1
    else:
        par = par+1
print ("{} valor(es) par(es)".format(par))
print ("{} valor(es) impar(es)".format(impar))
print ("{} valor(es) positivo(s)".format(pos))
print ("{} valor(es) negativo(s)".format(neg))
