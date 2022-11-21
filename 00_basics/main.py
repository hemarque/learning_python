import unittest

print("\n***** simple method *****\n")


def say_helloTo(name):
    return "Hi %s" % name


print(say_helloTo("Helder"))

print("\n***** simple test *****\n")


class Greeter(unittest.TestCase):
    def test_say_Hello(self):
        self.assertEqual(say_helloTo("Helder"), "Hi Helder")


if __name__ == '__main__':
    unittest.main()
