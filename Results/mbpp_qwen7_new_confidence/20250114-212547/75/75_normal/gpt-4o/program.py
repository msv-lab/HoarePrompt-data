def reverse_vowels(s: str) -> str:
    vowels = "AEIOUaeiou"
    s_list = list(s)
    vowel_indices = [i for i, char in enumerate(s) if char in vowels]
    vowel_chars = [s_list[i] for i in vowel_indices]

    for i in vowel_indices:
        s_list[i] = vowel_chars.pop()

    return ''.join(s_list)

# Tests
assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"
