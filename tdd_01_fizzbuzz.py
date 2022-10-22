import unittest


def fizzbuzz_of(number):
    return 1


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_of_1_is_1(self):
        self.assertEqual(fizzbuzz_of(1), 1)


if __name__ == '__main__':
    unittest.main()
