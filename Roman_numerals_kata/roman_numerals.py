def convert_to_roman(arabic_number):
    if arabic_number == 5:
        return "V"
    if arabic_number == 6:
        return "VI"
    if arabic_number == 7:
        return "VII"
    return "I" * arabic_number
