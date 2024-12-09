def func_1(s: str) -> int:
    return s.count('std')
assert func_1('letstdlenstdporstd') == 3
assert func_1('truststdsolensporsd') == 1
assert func_1('makestdsostdworthit') == 2
assert func_1('stds') == 1
assert func_1('') == 0