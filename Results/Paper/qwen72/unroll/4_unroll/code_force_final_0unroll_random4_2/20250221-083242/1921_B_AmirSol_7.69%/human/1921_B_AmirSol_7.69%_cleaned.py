def func_1(n: int, s1: str, s2: str) -> int:
    counter = 0
    i = 0
    while i < n:
        if s1[i] != s2[i]:
            if i < n - 1 and s1[i + 1] != s2[i + 1] and (s1[i] != s1[i + 1]):
                counter += 1
                i += 2
            else:
                counter += 1
                i += 1
        else:
            i += 1
    return counter
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    print(func_1(n, s1, s2))