def func_1(s: str) -> str:
    return ''.join([char for char in s if char.isupper()])
assert func_1('PYTHon') == 'PYTH'
assert func_1('FInD') == 'FID'
assert func_1('STRinG') == 'STRG'