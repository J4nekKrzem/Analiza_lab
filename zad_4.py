#zad 4 Stworzyć funkcję, która przyjmie 3 argumenty typu int i
#sprawdzi czy suma dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację jako typ logiczny bool

def sprawdzaczywieksze(a: int,b: int,c: int):
    d=bool(a+b==c)
    if d is True:
      print("są równe")
    else:
      print("nie są równe")

liczba1 = int(input("podaj liczbę1: "))
liczba2 = int(input("podaj liczbę2: "))
liczba3 = int(input("podaj liczbę3: "))

sprawdzaczywieksze(liczba1,liczba2,liczba3)