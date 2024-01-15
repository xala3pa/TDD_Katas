from Anagrams_kata import anagrams


class TestAnagrams:

    def test_return_a_empty_string_when_generate_anagrams_of_empty_string(self):
        assert anagrams.generate_anagrams('') == ['']

    def test_return_a_when_generate_anagram_of_a(self):
        assert anagrams.generate_anagrams('a') == ['a']

    def test_return_b_when_generate_anagram_of_b(self):
        assert anagrams.generate_anagrams('b') == ['b']

    def test_return_all_anagrams_when_generate_anagram_of_ab(self):
        assert anagrams.generate_anagrams('ab') == ['ab', 'ba']
