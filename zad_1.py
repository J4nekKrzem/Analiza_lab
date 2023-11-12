#. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
#wyświetli każde z nich.

def wys_imiona(lista):
  while len(lista_imion)<5:
    imie =(input("podaj imię: "))
    lista_imion.append(imie)
  for imie in lista_imion:
    print(imie)

lista_imion = ["ukasz", "Michal","Aneta", "Iwona","Andrzej"]


wys_imiona(lista_imion)