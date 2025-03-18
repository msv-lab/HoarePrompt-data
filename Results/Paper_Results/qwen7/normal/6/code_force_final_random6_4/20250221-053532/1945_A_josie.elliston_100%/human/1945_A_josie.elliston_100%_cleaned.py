def func_1(extroverts: int, universals: int) -> Optional[int]:
    if extroverts % 3 != 0:
        if extroverts % 3 + universals < 3:
            return None
    return ceil((extroverts + universals) / 3)

def func_2(introverts: int, extroverts: int, universals: int) -> int:
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
test_case_n = int(input())
for _ in range(test_case_n):
    (introverts, extroverts, universals) = map(int, input().split(' '))
    print(func_2(introverts, extroverts, universals))