def func_1(d: dict, n: int) -> dict:
    return {k: v for (k, v) in d.items() if v >= n}
assert func_1({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert func_1({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 180) == {'Alden Cantrell': 180, 'Pierre Cox': 190}
assert func_1({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 190) == {'Pierre Cox': 190}