def dict_filter(d: dict, n: int) -> dict:
    return {k: v for k, v in d.items() if v >= n}

# Test cases
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 180) == {'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 190) == {'Pierre Cox': 190}
