import unittest


def fizzbuzz_of(number):
    response = number
    if number % 15 == 0:
        response = "FizzBuzz"
    elif number % 3 == 0:
        response = "Fizz"
    elif number % 5 == 0:
        response = "Buzz"
    return response


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_of_1_is_1(self):
        self.assertEqual(fizzbuzz_of(1), 1)

    def test_fizzbuzz_of_2_is_2(self):
        self.assertEqual(fizzbuzz_of(2), 2)

    def test_fizzbuzz_of_3_is_fizz(self):
        self.assertEqual(fizzbuzz_of(3), "Fizz")

    def test_fizzbuzz_of_5_is_buzz(self):
        self.assertEqual(fizzbuzz_of(5), "Buzz")

    def test_fizzbuzz_of_6_is_fizz(self):
        self.assertEqual(fizzbuzz_of(6), "Fizz")

    def test_fizzbuzz_of_10_is_Buzz(self):
        self.assertEqual(fizzbuzz_of(10), "Buzz")

    def test_fizzbuzz_of_15_is_FizzBuzz(self):
        self.assertEqual(fizzbuzz_of(15), "FizzBuzz")

    def test_fizzbuzz_of_30_is_FizzBuzz(self):
        self.assertEqual(fizzbuzz_of(30), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
