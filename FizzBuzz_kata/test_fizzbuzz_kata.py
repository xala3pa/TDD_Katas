import pytest

from FizzBuzz_kata import fizzbuzz


class TestFizzBuzzShould:
    @pytest.mark.parametrize("given, expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_return_as_string_when_fizzbuzz_number(self, given, expected):
        assert fizzbuzz.fizzbuzz(given) == expected

    def test_return_fizz_when_fizzbuzz_number_3(self):
        assert fizzbuzz.fizzbuzz(3) == "fizz"

    def test_return_fizz_when_fizzbuzz_number_6(self):
        assert fizzbuzz.fizzbuzz(6) == "fizz"

    def test_return_fizz_when_fizzbuzz_number_9(self):
        assert fizzbuzz.fizzbuzz(9) == "fizz"
