# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):

    # Initialize the appropriate variable

    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 30:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)



# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    return a + b
result= sum_numbers(3, 4)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def numbers(*args):
    return sum(args) / 2
result = numbers(1, 2, 3, 4, 5)
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def line(backward_line):
    return backward_line[::-1]

line2 = line("Hello, world!")
print(line2)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def words_list (words):

    longest_word = words.replace(',', '')
    longest_word = longest_word.split ()
    longest_word = max(longest_word, key=len)
    return longest_word

final_result = words_list("Написати функцію, яка приймає список слів та повертає найдовше слово у списку.")

print (final_result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
   return str1.find(str2)

# поверне 7

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1