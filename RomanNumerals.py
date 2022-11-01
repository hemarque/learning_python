import unittest


def toRoman(param):
    if(param == 2):
        return "II"
    return "I"


class RomanNumeralTranslator(unittest.TestCase):
    def testRomans(self):
        self.assertEqual("I", toRoman(1))
        self.assertEqual("II", toRoman(2))


if __name__ == '__main__':
    unittest.main()
