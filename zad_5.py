#d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
#wykorzystanie funkcji range ), a następnie wyświetli co drugi element.

def zwroc2(lista):
  i = 0
  while i < len(lista):
    print(lista[i])
    i+=2

a=[0,1,2,3,4,5,6,7,8,9,10]
zwroc2(a)