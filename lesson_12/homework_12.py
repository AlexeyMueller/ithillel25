"""Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів -
1 правильно задизайнений позитивний тест на функцію."""

"""  Task 1
Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def numbers(*args):
    return sum(args) / len(args)

result = numbers(1, 2, 3, 4, 5)

print(result)

""" Task 2
 == Зробіть так, щоб кількість бананів була
 завжди в чотири рази більша, ніж яблук"""

def fruits(apples):
    b = apples * 4
    return b
total_bananas = fruits(2)
print(f"We have {total_bananas} bananas")

""" Task 3
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?"""

def day(start,*changes):
    return start + sum(changes)

evening_temperature = day(0,5, -10, 4)
print(f"Evening temperature: {evening_temperature}°C")


""" ДЗ 6.4. Сумуємо числа
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""

def even(numbers):
    total = 0
    for i in numbers:
        if i % 2 != 0:
            continue
        else:
            total += i

    return total

even_numbers_sum = even([1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10])
print(even_numbers_sum)
