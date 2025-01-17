def replace_spaces(s: str) -> str:
    return ''.join('_' if char == ' ' else ' ' if char == '_' else char for char in s)

# Test cases
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('The_Avengers') == 'The Avengers'
assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'
