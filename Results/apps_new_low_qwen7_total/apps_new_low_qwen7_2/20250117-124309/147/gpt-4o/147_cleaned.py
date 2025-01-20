(n, k) = map(int, input().split())
tab_types = list(map(int, input().split()))

def func_1(b):
    remaining_tabs = tab_types[:]
    for i in range(b, n, k):
        remaining_tabs[i] = 0
    for i in range(b, -1, -k):
        remaining_tabs[i] = 0
    return remaining_tabs
max_diff = 0
for b in range(n):
    remaining_tabs = func_1(b)
    e = remaining_tabs.count(1)
    s = remaining_tabs.count(-1)
    max_diff = max(max_diff, abs(e - s))
print(max_diff)