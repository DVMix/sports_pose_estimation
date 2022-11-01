import unittest


# твоя функция 1
def sum_(a, b):
    return a + b


# твоя функция 2
def sub_(a, b):
    return a - b


class TestStringMethods(unittest.TestCase):
    def test_sum(self):
        # подаешь в функцию 2 аргумента sum_(2, 3) и ждешь на выходе 5, но тут я поставил 4.
        # и тест не будет пройдет. вывалится ошибка
        self.assertEqual(sum_(2, 3), 4)

    def test_sub(self):
        # здесь тесты будут пройдены успешно ,т.к. на входе 2 и 3. 2-3 = -1
        self.assertEqual(sub_(2, 3), -1)


if __name__ == '__main__':
    unittest.main()
