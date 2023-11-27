# zad 1 Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}!

def przywitanie(name: str, surname: str):
    print("Cześć", name, "", surname)


name = input("podaj imię: ")
surname = input("podaj nazwisko: ")
przywitanie(name, surname)
