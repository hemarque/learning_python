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
