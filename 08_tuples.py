"""
ordered
with duplicates
immutable
"""

print("\n***** tuples *****\n")

my_tuple = tuple()
another_tuple = ()
mixed_tuple = (1, 3.1, "hi")
print(type(my_tuple))
print(type(another_tuple))
print(type(mixed_tuple))
print(mixed_tuple[1])
print(mixed_tuple[-1])
print(mixed_tuple.count("hi"))
print(mixed_tuple.index("hi"))
print(mixed_tuple)
sum_tuple = mixed_tuple + (4, "aloha", 5.7)
print(sum_tuple)
print(sum_tuple[3:5])
changed_tuple = (1, 2, 3)
# Original tuple
print(changed_tuple)
changed_tuple = list(changed_tuple)
# Changed to list
print(changed_tuple)
changed_tuple.insert(3, "Boom!")
# Inserting element to list
print(changed_tuple)
changed_tuple = tuple(changed_tuple)
# Changed list to tuple
print(changed_tuple)
# Remember, tuples are immutable