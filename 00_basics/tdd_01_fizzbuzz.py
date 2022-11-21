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

    def test_first_100_fizzbuzz(self):
        expected = \
            [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
             11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
             'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz',
             31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz',
             41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz',
             'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz',
             61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz',
             71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz',
             'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz',
             91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz']

        response = []
        for number in range(1, 100):
            response.append(fizzbuzz_of(number))

        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
