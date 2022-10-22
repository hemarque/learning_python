"""
no duplicates
not ordered
mutable
"""
sample_set = set()
print(type(sample_set))

empty_set = {}  # dictionary
print(type(empty_set))

another_set = {"hi", 1, 3.5, 1}  # no duplicates
print(type(another_set))
print(another_set)
print(len(another_set))
another_set.add("hello pal!")  # not ordered
print(another_set)
print("HI" in another_set)
print("hi" in another_set)
print(another_set.union({9, 8, 7}))
print(another_set.difference({1, 2, 3.5}))
