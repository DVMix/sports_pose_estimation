import unittest


def sum_(a, b):
    return a + b


def sub_(a, b):
    return a - b


class TestStringMethods(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_(2, 3), 4)

    def test_sub(self):
        self.assertEqual(sub_(2, 3), -1)


if __name__ == '__main__':
    unittest.main()
