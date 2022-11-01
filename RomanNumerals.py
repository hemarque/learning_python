import unittest


def toRoman(param):
    romans = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
              5: "V", 4: "IV", 1: "I"}
    response = ""
    for arabic in romans:
        while param >= arabic:
            response += romans[arabic]
            param -= arabic
    return response


class RomanNumeralTranslator(unittest.TestCase):
    def testRomans(self):
        self.assertEqual("I", toRoman(1))
        self.assertEqual("II", toRoman(2))
        self.assertEqual("III", toRoman(3))
        self.assertEqual("IV", toRoman(4))
        self.assertEqual("V", toRoman(5))
        self.assertEqual("VI", toRoman(6))
        self.assertEqual("VII", toRoman(7))
        self.assertEqual("VIII", toRoman(8))
        self.assertEqual("IX", toRoman(9))
        self.assertEqual("MMMCMXCIX", toRoman(3999))
        self.assertEqual("MCMXCIX", toRoman(1999))
        self.assertEqual("MMM", toRoman(3000))


if __name__ == '__main__':
    unittest.main()
