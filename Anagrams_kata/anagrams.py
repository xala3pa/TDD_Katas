def generate_anagrams(word):
    if len(word) <= 1:
        return [word]
    else:
        anagrams = []
        for i, letter in enumerate(word):
            for perm in generate_anagrams(word[:i] + word[i + 1:]):
                anagrams.append(letter + perm)
        return anagrams
