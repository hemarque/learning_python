"""
No duplicate for keys
Ordered
Mutable
key:value pairs
"""

a_dictionary = dict()
print(type(a_dictionary))

another_dictionary = {}
print(type(another_dictionary))

another_dictionary = {1: "hi", "Name": "Helder", "Age": 44, 1: "Hello", "Favorite number": 44,
                      "My favorite keyboard": ["ISO", "ES", "TKL", "MX BLUE"]}
print(another_dictionary)

print(another_dictionary.pop("Name"))
print(another_dictionary)
print(another_dictionary.get("My favorite keyboard")[0])
print(another_dictionary["Favorite number"])
print("Hello" in another_dictionary)  # doesnt find values...
print("Favorite number" in another_dictionary)  # ...only finds keys...
print("Hello" in another_dictionary.values())  # ...but we can query the values
