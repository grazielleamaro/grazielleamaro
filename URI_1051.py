sal = float(input())

if 0.00<=sal<=2000.00:
    print("Isento")
elif sal<=3000.00:
    vlrinc = sal-2000.00
    IR = vlrinc*0.08
    print("R$ {:.2f}".format(IR))
elif sal <=4500.00:
    vi1 = sal - 3000.00
    v2 = 1000*0.08
    IR2 = (vi1*0.18)+v2
    print ("R$ {:.2f}".format(IR2))
else:
    v1 = sal-4500
    v2 = 1000*0.08
    v3 = 1500*0.18
    IR3 = (v1*0.28)+v2+v3
    print ("R$ {:.2f}".format(IR3))
    
