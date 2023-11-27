# testuję
def mixujlisty(lista1: list, lista2: list):
    lista3 = []
    for el in lista1:
        if el not in lista2:
            lista2.append(el)
    for el in lista2:
        x = el**3
        lista3.append(x)
    print(sorted(lista3))
    return sorted(lista3)


lista_1 = [1, 2, 3, 4]
lista_2 = [1, 5, 6, 7]

mixujlisty(lista_1, lista_2)
