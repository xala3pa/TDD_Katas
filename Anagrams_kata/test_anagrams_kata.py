from Anagrams_kata import anagrams


class TestAnagrams:

    def test_return_a_empty_string_when_generate_anagrams_of_empty_string(self):
        assert anagrams.generate_anagrams('') == ['']
