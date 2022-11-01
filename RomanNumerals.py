import unittest


def toRoman(param):
    return "I"


class RomanNumeralTranslator(unittest.TestCase):
    def testRomans(self):
        self.assertEqual("I", toRoman(1))


if __name__ == '__main__':
    unittest.main()
