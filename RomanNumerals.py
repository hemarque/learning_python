import unittest


def toRoman(param):
    response = ""
    while param >= 5:
        response += "V"
        param -= 5
    while param >= 4:
        response += "IV"
        param -= 4
    while param >= 1:
        response += "I"
        param -= 1
    return response


class RomanNumeralTranslator(unittest.TestCase):
    def testRomans(self):
        self.assertEqual("I", toRoman(1))
        self.assertEqual("II", toRoman(2))
        self.assertEqual("III", toRoman(3))
        self.assertEqual("IV", toRoman(4))
        self.assertEqual("V", toRoman(5))
        self.assertEqual("VI", toRoman(6))


if __name__ == '__main__':
    unittest.main()
