(n, k) = map(int, input().split())
tabs = list(map(int, input().split()))
max_diff = 0
for b in range(1, n + 1):
    (e, s) = (0, 0)
    for i in range(1, n + 1):
        if (i - b) % k != 0:
            e += tabs[i - 1] == 1
            s += tabs[i - 1] == -1
    max_diff = max(max_diff, abs(e - s))
print(max_diff)