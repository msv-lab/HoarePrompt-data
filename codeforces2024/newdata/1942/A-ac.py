t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
for n, k in test_cases:
    a = []
    if n-k == 0:
        a.extend([1] * n)
    elif k == 1:
        a.extend(list(range(1,n+1)))
    else:
        a.extend([-1])
    print(*a, sep=' ')