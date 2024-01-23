import pytest

from Roman_numerals_kata import roman_numerals


class TestRomanNumeralsShould:
    @pytest.mark.parametrize("given, expected",
                             [(1, "I"), (2, "II"), (3, "III"),
                              (5, "V"), (6, "VI"), (7, "VII"),
                              (10, "X"), (11, "XI"), (12, "XII"),
                              (16, "XVI"), (17, "XVII"), (18, "XVIII"),
                              (20, "XX"), (21, "XXI"), (26, "XXVI"),
                              (30, "XXX"), (32, "XXXII"), (37, "XXXVII"),
                              (4, "IV"), (9, "IX"), (19, "XIX"),
                              (40, "XL"), (90, "XC"), (800, "DCCC"),
                              (846, "DCCCXLVI"), (1999, "MCMXCIX"), (2008, "MMVIII")])
    def test_convert_to_roman_an_arabic_number(self, given, expected):
        assert roman_numerals.convert_to_roman(given) == expected

    def test_raise_exception_with_non_integer_input(self):
        with pytest.raises(ValueError, match="The number must be in the range of 1 to 3999"):
            roman_numerals.convert_to_roman(5000)
