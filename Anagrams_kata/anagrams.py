def generate_anagrams(s):
    if len(s) <= 1:
        return [s]
    else:
        anagrams = []
        for i, letter in enumerate(s):
            for perm in generate_anagrams(s[:i] + s[i + 1:]):
                anagrams.append(letter + perm)
        return anagrams
