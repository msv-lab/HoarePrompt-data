def min_cost_to_sort(s):
    count_0 = s.count('0')
    count_1 = len(s) - count_0
    return min(count_0, count_1) * 2

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_cost_to_sort(s))