#zad 5 Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int .
#Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.
def czyzawiera(a: list, b: int):
  for el in a:
    if el == b:
      d = bool(el == b)
    else:
      d = bool((el == b))
  return d


lista1 = [1,2,-1,12,76,2,-26,3]
poszukiwana = 1
czyzawiera(lista1,poszukiwana)
