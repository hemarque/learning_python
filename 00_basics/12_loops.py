number = 5
while number > 0:
    print(number)
    number -= 1
else:
    print("number is less or equals to zero")

number = 10
while number > 0:
    print(number)
    number -= 1
    if number == 5:
        break

number = 10
while number > 0:
    number -= 1
    if number % 2 == 0:
        continue
    print(number)



