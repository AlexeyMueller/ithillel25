"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об('єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",'
'який дозволяє змінювати середній бал студента.'
'Виведіть інформацію про студента та змініть його середній бал.)"""



class Student:
    def __init__(self, name, surname, age, mark):
        self.name = name
        self.surname =surname
        self.age = age
        self.mark = mark

    def average_mark(self):
        average = sum(self.mark)/len(self.mark)
        return average


first_student = Student ("Taras", "Schevchenko", 20, [5, 3, 4, 4, 3])

print(f"Середній бал студента Тараса Шевченко : {first_student.average_mark()}")


