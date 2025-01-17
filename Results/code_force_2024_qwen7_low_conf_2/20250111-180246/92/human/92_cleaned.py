def func_1(n, v, p):
    v_sorted = sorted(v, reverse=True)
    max_strength = 0
    min_mushrooms = n
    for i in range(1, n + 1):
        strength = i * v_sorted[i - 1]
        if strength > max_strength:
            max_strength = strength
            min_mushrooms = i
        elif strength == max_strength:
            min_mushrooms = min(min_mushrooms, i)
    return (max_strength, min_mushrooms)
t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    p = list(map(int, input().split()))
    result = func_1(n, v, p)
    print(*result)