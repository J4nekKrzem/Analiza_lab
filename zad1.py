class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

# Tworzenie dwóch obiektów klasy Student


student1 = Student("Jan Kowalski", [60, 75, 80, 90])
student2 = Student("Anna Nowak", [30, 40, 45, 20])


# Wywołanie metody is_passed dla obiektów
result1 = student1.is_passed()
result2 = student2.is_passed()

# Wyświetlenie wyników
print(f"{student1.name}: {'Zdany' if result1 else 'Niezdany'}")
print(f"{student2.name}: {'Zdany' if result2 else 'Niezdany'}")
