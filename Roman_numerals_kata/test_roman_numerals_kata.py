from Roman_numerals_kata import roman_numerals


class TestRomanNumeralsShould:
    def test_convert_to_roman_an_arabic_number(self):
        assert roman_numerals.convert_to_roman(1) == "I"
