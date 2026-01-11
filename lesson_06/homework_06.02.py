""" ДЗ 6.2. Цикл “Дочекайся літери”

Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h". """

line = input("Enter your line: ")
letter = "h"
letter_2 = "H"

for char in line:
    if (char == letter) or (char == letter_2):
        print("We have a letter h")
    else:
        continue
