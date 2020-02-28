import datetime as dt

func = ['compra','venda']
listC = []
listV = []
dateAtual = dt.datetime.now()

def compras(totalCompra=0,totalVenda=0,valor=0):

    if func[0]:
        print("Informe o valor",valor)
        listC.append(dateAtual,valor)
        if listC[0] != dateAtual:
            totalCompra += listC[1]

    elif func[1]:
        print("Informe o valor", valor)
        listV.append(dateAtual,valor)
        if listV[0] != dateAtual:
            totalVenda += listC[1]

    lucro = totalCompra - totalVenda

    return lucro