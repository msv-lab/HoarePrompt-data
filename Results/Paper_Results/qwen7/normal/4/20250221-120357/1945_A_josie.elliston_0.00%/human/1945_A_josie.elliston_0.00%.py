from math import ceil
from typing import Optional
 
 
 
 
# Each introvert wants to live in a tent alone. Thus, a tent with an introvert must contain exactly one person — only the introvert himself.
# Each extrovert wants to live in a tent with two others. Thus, the tent with an extrovert must contain exactly three people.
# Each universal is fine with any option(living alone, with one other person, or with two others).
 
 
def f(extroverts: int, universals: int) -> Optional[int]:
    if extroverts % 3 != 0:
        if extroverts % 3 + universals < 3:
            return None
    return ceil((extroverts + universals)/3)
 
def g(introverts: int, extroverts: int, universals: int) -> int:
    ret = f(extroverts, universals)
    return -1 if ret is None else introverts+ret
    
# test_case_n = int(input())
# for _ in range(test_case_n):
#     (introverts, extroverts, universals) = map(int, input().split(' '))
#     # return min area
#     print(g(introverts, extroverts, universals))
    
for line in '''1 2 3
1 4 1
1 4 2
1 1 1
1 3 2
19 7 18
0 0 0
7 0 0
0 24 0
1000000000 1000000000 1000000000'''.splitlines():
    (introverts, extroverts, universals) = map(int, line.split(' '))
    print('line:', line)
    print('ret:', g(introverts, extroverts, universals))