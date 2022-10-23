try:
    print(1 + "2")
except Exception as error:
    print("Exception: %s" % error )
else:
    print("the execution was right")
finally:
    print("this always is executed")

print("----------------")

try:
    print(1 + 3)
except Exception as error:
    print("Exception: %s" % error)
else:
    print("the execution was right")
finally:
    print("this always is executed")
