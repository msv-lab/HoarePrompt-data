def func_1(extroverts: int, universals: int) -> Optional[int]:
    if extroverts % 3 != 0:
        if extroverts % 3 + universals < 3:
            return None
    return ceil((extroverts + universals) / 3)

def func_2(introverts: int, extroverts: int, universals: int) -> int:
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
for line in '1 2 3\n1 4 1\n1 4 2\n1 1 1\n1 3 2\n19 7 18\n0 0 0\n7 0 0\n0 24 0\n1000000000 1000000000 1000000000'.splitlines():
    (introverts, extroverts, universals) = map(int, line.split(' '))
    print('line:', line)
    print('ret:', func_2(introverts, extroverts, universals))