class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sq. m., {self.rooms} rooms, {self.price} ZŁ, {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {super().__str__()}, Plot: {self.plot} sq. m."

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {super().__str__()}, Floor: {self.floor}"

# Stworzenie obiektów dla House i Flat
house_object = House(150, 4, 350000, "Zielona 4", 300)
flat_object = Flat(80, 2, 200000, "Mickiewicza 123", 3)

# Wyświetlenie obiektów
print(str(house_object))
print(str(flat_object))