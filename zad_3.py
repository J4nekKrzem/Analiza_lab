##b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci.
#ii. Wykorzystując listę składaną.

def mnozy(lista):
  lista2 = []
  for el in lista:
    el*=2
    lista2.append(el)
  return lista2

a = [1,2,3,4,5]
mnozy(a)
