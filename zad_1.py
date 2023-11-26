# Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.

def wys_imiona(lista):
    while len(lista) < 5:
        imie = (input("podaj imię: "))
        lista.append(imie)
    for imie in lista:
        print(imie)


lista_imion = []


wys_imiona(lista_imion)
