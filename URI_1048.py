sal = float(input())
if 0<=sal<=400:
    reajuste = sal*0.15
    novo=sal+reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")
elif sal<=800:
    reajuste = sal*0.12
    novo=sal+reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")
elif sal<=1200:
    reajuste = sal*0.10
    novo=sal+reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")
elif sal<=2000:
    reajuste = sal*0.07
    novo=sal+reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")
else:
    reajuste = sal*0.04
    novo=sal+reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")
