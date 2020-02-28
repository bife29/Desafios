def valid(validCampos):
    list = []
    inicio = tuple('({[')
    fim = tuple(')}]')
    arr = dict(zip(inicio, fim))


    for i in validCampos:
        if i in inicio:
            list.append(map[i])
        elif i in fim:
            if not list or i != list.pop():
                return "nao Permitido"
    return "Permitido"