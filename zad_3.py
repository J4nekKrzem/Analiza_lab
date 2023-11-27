'''cw 3 Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jestparzysta i zwróci tą informację jako typ logiczny bool ( True / False ).
Należy uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" / "Liczba nieparzysta"
'''


def sprawdzamczyparzy(liczba):
    a = bool(liczba % 2 == 0)
    return a


liczba = int(input("podaj liczbę:"))


wynik = sprawdzamczyparzy(liczba)

if wynik is True:
    print("jest parzysta")
else:
    print("nie jest parzysta")
