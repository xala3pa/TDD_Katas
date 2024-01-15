from itertools import permutations


def generate_anagrams(word):
    if len(word) <= 1:
        return [word]

    anagrams_set = set()

    for perm in permutations(word):
        anagram = ''.join(perm)
        anagrams_set.add(anagram)

    return sorted(list(anagrams_set))
