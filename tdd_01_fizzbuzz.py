import unittest


def fizzbuzz_of(number):
    if number % 3 == 0:
        return "Fizz"
    if number == 5:
        return "Buzz"
    return number


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_of_1_is_1(self):
        self.assertEqual(fizzbuzz_of(1), 1)

    def test_fizzbuzz_of_2_is_2(self):
        self.assertEqual(fizzbuzz_of(2), 2)

    def test_fizzbuzz_of_3_is_fizz(self):
        self.assertEqual(fizzbuzz_of(3), "Fizz")

    def test_fizzbuzz_of_5_is_buzz(self):
        self.assertEqual(fizzbuzz_of(5), "Buzz")

    def test_fizzbuzz_of_6_is_Fizz(self):
        self.assertEqual(fizzbuzz_of(6), "Fizz")

if __name__ == '__main__':
    unittest.main()
