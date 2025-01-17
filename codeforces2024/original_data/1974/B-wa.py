def decode(encoded_string):
    unique_chars = sorted(set(encoded_string))
    char_map = {char: sym_char for char, sym_char in zip(unique_chars, reversed(unique_chars))}
    return ''.join(char_map[char] for char in encoded_string)