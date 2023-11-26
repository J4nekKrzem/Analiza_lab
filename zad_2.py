#b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci.
#i. Wykorzystując pętle for .


listaliczb=[1,2,3,4,5]

def dziaania(lista):
  for el in lista:
    el*=2
    lista2=[]
    lista2.append(el)
    print(lista2)

dziaania(listaliczb)