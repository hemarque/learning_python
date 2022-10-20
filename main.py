import unittest

# hi! this is a comment in python

"""
...and this
is a multiline
comment
"""

'''
another way
to write 
multiline 
comments
'''

print("\n***** intro *****\n")
print("hi there!")
an_operation = 5 + 2
print("the result is", an_operation)

print("\n***** basic types *****\n")
print(type("hi!"))  # str
print(type(3))  # int
print(type(5.2))  # float
print(type(3 == 2))  # bool
print(type(1j))  # complex
print(type((1, 2, 3)))  # tuple
print(type([1, 2, 3]))  # list
print(type({1, 2, 3}))  # set
print(type({1: 1, 2: 5, 3: -1}))  # dict

print(type(str(5)))

print("\n***** string length *****\n")
print(len("hi!"))

print("\n***** string functions *****\n")
one, two, three = 1, 2, 3
print(one, two, three)

"""
your_name = input("what's your name? ")
print("nice to meet you", your_name)
"""
print("\n***** playing with strings *****\n")
print("hi! " * 3)

print("\n***** basic math operations *****\n")
print(10 / 3)
print(10 // 3)
print(10 % 3)

print("\n***** compare numbers *****\n")
print(3 < 4)
print(3 > 4)
print(3 >= 4)
print(3 <= 4)
print(3 >= 3)
print(3 <= 3)
print(3 == 3)
print(3 != 4)

print("\n***** string order *****\n")
print("he" < "hello")
print("he" < "hi")
print("he" < "ha")

print("\n***** boolean operations *****\n")
print(3 < 4 and "he" < "hi")
print((3 < 4) and ("he" < "hi"))
print(not (3 < 4) and not ("he" < "hi"))

print("\n***** special characters *****\n")
print("this is a tab \t and a new line \n and a slash \\, got it?")

print("\n***** string functions *****\n")
print("what are YOU doing?".upper())
print("what are YOU doing?".capitalize())
print("what are YOU doing?".lower())
print("what are YOU doing?".count("o"))
print("what are YOU doing?".startswith("what"))

print("\n***** string format *****\n")
firstname = "John"
lastname = "Galt"
print("who is %s?" % firstname)
print("who is %s %s?" % (firstname, lastname))
print("who is {} {}?".format(firstname, lastname))
print(f"who is {firstname} {lastname}?")

print("\n***** assigning chars in string to variables *****\n")
a, b, c, d, e = "ABCDE"
print(a)
print(e)

print("\n***** working with chars in strings *****\n")
name = "Mario"
print(name[0])
print(name[0:3])
print(name[-2])
print(name[::-1])
print(name[::-2])
print(name[::-3])

print("\n***** cleaning strings *****\n")
text_with_spaces = " example "
print(".%s." % text_with_spaces.rstrip())
print(".%s." % text_with_spaces.lstrip())
print(".%s." % text_with_spaces.strip())
text_with_spaces = "    example    "
print(".%s." % text_with_spaces.strip())

print("\n***** detecting the nature of a string content *****\n")
print(name.isalpha())
print("5".isnumeric())

print("\n***** lists *****\n")
first_list = list()
second_list = []
third_list = [23, 65, 12, 67, 12, 98]
forth_list = [32, "hi", 3.14, 1j]

print("1st list : %s" % first_list)
print("2nd list : %s" % second_list)
print("3rd list : %s" % third_list)
print("4th list : %s" % forth_list)

print(type(first_list))
print(type(second_list))

print(len(first_list))
print(len(second_list))
print(len(third_list))
print(len(first_list))

print("the first element is %s" % forth_list[0])
print("the last element is %s" % forth_list[-1])
# print("trying an out of bound getting the index 5 % " % forth_list[5])
# print("trying an out of bound getting the index -5 % " % forth_list[-5])
print(forth_list.count("hi"))
print(third_list.count(12))

print(third_list + forth_list)

print("the list : %s" % third_list)
print("remove the first 12 : %s" % third_list.remove(12))
print("the list : %s" % third_list)
print("extract the last element : %s" % third_list.pop())
print("the list : %s" % third_list)
print("extract the element with the index 2 : %s" % third_list.pop(2))
print("the list : %s" % third_list)

third_list.insert(2, 1024)
print("the list : %s" % third_list)
copy_list = third_list.copy()
print("the list : %s" % copy_list)
third_list.reverse()
print("the list : %s" % third_list)
third_list.sort()
print("the list : %s" % third_list)
third_list.clear()
print("the list : %s" % third_list)

print("\n***** simple method *****\n")


def say_helloTo(name):
    return "Hi %s" % name


print(say_helloTo("Helder"))


class Greeter(unittest.TestCase):
    def test_say_Hello(self):
        self.assertEqual(say_helloTo("Helder"), "Hi Helder")


if __name__ == '__main__':
    unittest.main()
