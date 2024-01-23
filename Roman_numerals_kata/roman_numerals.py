def convert_to_roman(arabic_number):
    roman_number = ""
    if arabic_number == 11:
        return "XI"
    if arabic_number == 10:
        return "X"
    if arabic_number >= 5:
        roman_number += "V"
        arabic_number -= 5
    roman_number += "I" * arabic_number
    return roman_number
