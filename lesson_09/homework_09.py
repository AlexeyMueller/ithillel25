"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""

class Rhombus:
        def __init__(self):
                pass

        def __setattr__(self, name, value):
            if name == "side_a":
                if value > 0:
                    object.__setattr__(self, name, value)
                else:
                    print("Сторона має бути більшою за 0")

            elif name == "angle_a":
                object.__setattr__(self, name, value)
                object.__setattr__(self, "angle_b", 180 - value)

            elif name == "angle_b":
                print("angle_b розраховується автоматично. Не можна змінювати напряму.")

            else:
                object.__setattr__(self, name, value)

a = Rhombus()
a.angle_a = 60 # OK, angle_b має стати 120

print(a.angle_b)   # → 120
a.angle_b = 90






