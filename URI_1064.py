cont = 0
pos = 0
soma = 0
while cont<6:
    a=float(input())
    if pos ==0 and a<0:
        a = float(input())
    elif a>0:
        soma=soma+a
        pos=pos+1
        media=(soma)/pos
        cont = cont+1
    else:
        cont = cont + 1
print ("{} valores positivos".format(pos))
print ("{:.1f}".format(media))

