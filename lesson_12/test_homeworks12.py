import unittest
from homework_12 import numbers, fruits, day, even

"""Task1"""
class Calculation (unittest.TestCase):
    def test_arithmetic_mean(self):
        self.assertEqual(numbers(1, 2, 3, 4, 5), 3)

    def test_empty_args(self):
        with self.assertRaises(ZeroDivisionError):
            numbers()


if __name__ == '__main__':
    unittest.main()

"""Task2"""
class Market (unittest.TestCase):
    def test_fruits_calculation(self):
        self.assertEqual(fruits(2), 8)

"""Task3"""
class Temperature (unittest.TestCase):
    def test_weather_forecast(self):
        self.assertEqual(day(0, 5, -10, 4), -1)

    def test_string_change(self):
        with self.assertRaises(TypeError):
            day(0, "5")

    def test_none_change(self):
        with self.assertRaises(TypeError):
            day(0, None)

    def test_list_inside(self):
        with self.assertRaises(TypeError):
            day(0, [5, -10, 4])


if __name__ == '__main__':
    unittest.main()

"""Task4"""

class Different_numbers(unittest.TestCase):
    def test_sum (self):
        self.assertEqual(even([1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10]), 30)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            even("123")

    def test_invalid_element(self):
        with self.assertRaises(TypeError):
            even([1, 2, "3", 4])


if __name__ == '__main__':
    unittest.main()