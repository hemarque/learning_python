def say_hi_to(name):
    return "Hi %s" % name


print(say_hi_to("Helder"))


def say_hi_again(first, last="Doe"):
    return f"Hello {first} {last}"


print(say_hi_again("Helder", "D.O."))
print(say_hi_again("Helder"))


def format_text_my_own_way(*words: str) -> str:
    response = ""
    for w in words:
        response += w.capitalize() + " "
    return response


print(format_text_my_own_way("this", "is", "a", "test"))
