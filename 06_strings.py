
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
