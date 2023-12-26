import pytest
from FizzBuzz_kata import fizzbuzz


class TestFizzBuzzShould:
    @pytest.mark.parametrize("given, expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_return_as_string_when_fizzbuzz_number(self, given, expected):
        assert fizzbuzz.fizzbuzz(given) == expected
