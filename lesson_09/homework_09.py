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
    def __init__(self, side_a, angle_a):
        self.side_a = side_a      # піде через __setattr__
        self.angle_a = angle_a   # автоматично створить angle_b

    def __setattr__(self, name, value):
        if name == "side_a":
            if value > 0:
                object.__setattr__(self, name, value)
            else:
                raise ValueError("Сторона має бути більшою за 0")

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має бути між 0 і 180")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("angle_b розраховується автоматично")

        else:
            object.__setattr__(self, name, value)

a = Rhombus(5, 60)

print(a.angle_a)  # 60
print(a.angle_b)  # 120
print(a.side_a)  # 5









