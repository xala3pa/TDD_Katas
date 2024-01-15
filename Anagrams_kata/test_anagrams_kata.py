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

    def test_return_all_anagrams_when_generate_anagram_of_abc(self):
        assert anagrams.generate_anagrams("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]

    def test_return_all_anagrams_when_generate_anagram_of_biro(self):
        expected_anagrams = ["biro", "bior", "brio", "broi", "boir", "bori",
                             "ibro", "ibor", "irbo", "irob", "iobr", "iorb",
                             "rbio", "rboi", "ribo", "riob", "roib", "robi",
                             "obir", "obri", "oibr", "oirb", "orbi", "orib"]

        result = anagrams.generate_anagrams("biro")
        assert set(result) == set(expected_anagrams)
