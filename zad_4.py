# c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
# wykorzystanie funkcji range ), a następnie wyświetli jedynie parzyste elementy.
def sprawdza(lista):
    literyparzyste = [lista[i] for i in range(0, 10, 2)]
    return literyparzyste


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sprawdza(a)
