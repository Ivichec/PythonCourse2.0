"""""the-stealth-warrior"se convierte en"theStealthWarrior"

"The_Stealth_Warrior"se convierte en"TheStealthWarrior"

"The_Stealth-Warrior"se convierte en"TheStealthWarrior"""""
def to_camel_case(text):
    text1 = list(text)
    i = 0
    while i < len(text1):
        if text1[i] == "_":
            text1[i + 1] = text1[i + 1].upper()
            text1.pop(i)
        elif text1[i] == "-":
            text1[i+1] = text1[i+1].upper()
            text1.pop(i)
        else:
            i += 1
    result = "".join(text1)
    return result

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))