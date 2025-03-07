def func_1(n: int, s1: str, s2: str) -> int:
    cats_to_add = sum((1 for i in range(n) if s1[i] == '0' and s2[i] == '1'))
    cats_to_remove = sum((1 for i in range(n) if s1[i] == '1' and s2[i] == '0'))
    return max(cats_to_add, cats_to_remove)
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    print(func_1(n, s1, s2))