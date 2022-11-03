"""
with duplicates
ordered
mutable
"""
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

matrix = [["0", "X", "0"], ["0", "X", "0"], ["0", "X", "0"]]
print("%s\n%s\n%s" % (matrix[0], matrix[1], matrix[2]))