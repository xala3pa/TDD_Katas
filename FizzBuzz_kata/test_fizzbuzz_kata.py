import pytest

from FizzBuzz_kata import fizzbuzz

FIZZBUZZ = "fizzbuzz"
BUZZ = "buzz"
FIZZ = "fizz"


class TestFizzBuzzShould:
    @pytest.mark.parametrize("given, expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_return_as_string_when_fizzbuzz_number(self, given, expected):
        assert fizzbuzz.fizzbuzz(given) == expected

    @pytest.mark.parametrize("given", [3, 6, 9])
    def test_return_fizz_when_fizzbuzz_number_3(self, given):
        assert fizzbuzz.fizzbuzz(given) == FIZZ

    @pytest.mark.parametrize("given", [5, 10, 20])
    def test_return_fizz_when_fizzbuzz_number_5(self, given):
        assert fizzbuzz.fizzbuzz(given) == BUZZ

    @pytest.mark.parametrize("given", [0, 15, 30, 45])
    def test_return_fizzbuzz_when_fizzbuzz_number_15(self, given):
        assert fizzbuzz.fizzbuzz(given) == FIZZBUZZ

