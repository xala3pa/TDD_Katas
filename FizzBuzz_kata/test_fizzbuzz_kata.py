from FizzBuzz_kata import fizzbuzz


class TestFizzBuzzShould:
    def test_return_1_as_string_when_fizzbuzz_number_1(self):
        assert fizzbuzz.fizzbuzz(1) == "1"

    def test_return_2_as_string_when_fizzbuzz_number_2(self):
        assert fizzbuzz.fizzbuzz(2) == "2"

