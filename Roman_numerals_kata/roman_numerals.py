def convert_to_roman(arabic_number):
    roman_numerals = {10: "X", 5: "V", 1: "I"}

    roman_number = ""
    for value, numeral in roman_numerals.items():
        while arabic_number >= value:
            roman_number += numeral
            arabic_number -= value
    return roman_number
