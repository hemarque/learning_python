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

print("hi there!")

an_operation = 5 + 2
print("the result is", an_operation)

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

print(len("hi!"))

one, two, three = 1, 2, 3
print(one, two, three)

"""
your_name = input("what's your name? ")
print("nice to meet you", your_name)
"""

print("hi! " * 3)

print(10 / 3)
print(10 // 3)
print(10 % 3)

print(3 < 4)
print(3 > 4)
print(3 >= 4)
print(3 <= 4)
print(3 >= 3)
print(3 <= 3)
print(3 == 3)
print(3 != 4)

print("he" < "hello")
print("he" < "hi")
print("he" < "ha")

print(3 < 4 and "he" < "hi")
print((3 < 4) and ("he" < "hi"))
print(not (3 < 4) and not ("he" < "hi"))

print("this is a tab \t and a new line \n and a slash \\, got it?")

print("what are YOU doing?".upper())
print("what are YOU doing?".capitalize())
print("what are YOU doing?".lower())
print("what are YOU doing?".count("o"))

firstname = "John"
lastname = "Galt"
print("who is %s?" % firstname)
print("who is %s %s?" % (firstname, lastname))
print("who is {} {}?".format(firstname, lastname))
print(f"who is {firstname} {lastname}?")

a, b, c, d, e = "ABCDE"
print(a)
print(e)

name = "Mario"
print(name[0])
print(name[0:3])
print(name[-2])
print(name[::-1])
print(name[::-2])
print(name[::-3])

print(name.isalpha())
print("5".isnumeric())