import pytest

from FizzBuzz_kata import fizzbuzz

FIZZ = "fizz"


class TestFizzBuzzShould:
    @pytest.mark.parametrize("given, expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_return_as_string_when_fizzbuzz_number(self, given, expected):
        assert fizzbuzz.fizzbuzz(given) == expected

    @pytest.mark.parametrize("given", [3, 6, 9])
    def test_return_fizz_when_fizzbuzz_number_3(self, given):
        assert fizzbuzz.fizzbuzz(given) == FIZZ

    def test_return_buzz_when_fizzbuzz_number_5(self):
        assert fizzbuzz.fizzbuzz(5) == "buzz"
