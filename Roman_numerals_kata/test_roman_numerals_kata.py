import pytest

from Roman_numerals_kata import roman_numerals


class TestRomanNumeralsShould:
    @pytest.mark.parametrize("given, expected", [(1, "I"), (2, "II")])
    def test_convert_to_roman_an_arabic_number(self, given, expected):
        assert roman_numerals.convert_to_roman(given) == expected
