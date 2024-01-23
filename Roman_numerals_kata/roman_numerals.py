def convert_to_roman(arabic_number: int) -> str:
    """
    Convert an Arabic number to its Roman numeral representation.

    Args:
    - arabic_number (int): Arabic number to convert (should be in the range of 1 to 3999).

    Returns:
    - str: Roman numeral representation.
    """
    if not (0 < arabic_number < 4000):
        raise ValueError("The number must be in the range of 1 to 3999")

    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    roman_number = ""
    for value, numeral in roman_numerals.items():
        while arabic_number >= value:
            roman_number += numeral
            arabic_number -= value
    return roman_number
