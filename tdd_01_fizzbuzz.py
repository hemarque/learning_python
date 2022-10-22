import unittest


def fizzbuzz_of(number):
    return number


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_of_1_is_1(self):
        self.assertEqual(fizzbuzz_of(1), 1)

    def test_fizzbuzz_of_2_is_2(self):
        self.assertEqual(fizzbuzz_of(2), 2)


if __name__ == '__main__':
    unittest.main()
