#TASK 1 - 3
#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where" —— said Alice.
 "Then it doesn't matter which way you go," said the Cat.
 "—— so long as I get somewhere," Alice added as an explanation.
 "Oh, you're sure to do that," said the Cat, "if you only walk long enough."""

print(alice_in_wonderland)
print (alice_in_wonderland.count("'"))


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_Sea_square = 436.402
Azov_Sea_square = 37.800
Total_square = Black_Sea_square + Azov_Sea_square
print(f"{Total_square}" + " km2 ")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


Supermarket_Total = 375291
Supermarkets_One_and_Two = 250449
Supermarkets_Two_and_Three = 222950

Supermarkets_One = Supermarket_Total - Supermarkets_Two_and_Three
Supermarkets_Three = Supermarket_Total - Supermarkets_One_and_Two
Supermarkets_Two = Supermarket_Total -(Supermarkets_One + Supermarkets_Three)

print(f"{Supermarkets_One}" + " items ")
print(f"{Supermarkets_Three}" + " items ")
print(f"{Supermarkets_Two}" + " items ")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
Monthly_payment = 1179
Months_to_pay = 18
Total_payment = Monthly_payment * Months_to_pay

print(f"{Total_payment}" + " hrn ")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
Піца_велика = 274 * 4
Піца_середня = 218 * 2
Сік = 35 * 4
Торт = 350
Вода = 21 * 3

Замовлення = (Піца_велика + Піца_середня + Сік + Торт + Вода)

print(f"Вартість замовлення дорівнює {Замовлення}" + " грн ")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

Photos = 232
Pages = 232  / 8

print (round(Pages))

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""


Distance = 1600
Gasoline_tank = 48
Gasoline = (1600 / 100) * 9
Stops = Gasoline / Gasoline_tank

print(f"{Gasoline} літрів бензину знадобиться для подорожі")
print (f"{round(Stops)} рази доведеться зупинитись, щоб заправити машину")
