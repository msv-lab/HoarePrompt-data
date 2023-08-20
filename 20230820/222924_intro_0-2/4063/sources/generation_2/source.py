N = int(input())
d = list(map(int, input().split()))

min_d = min(d)
max_d = max(d)

count = 0
for k in range(min_d, max_d+1):
    count_arc = sum([1 for i in d if i >= k])
    count_abc = N - count_arc
    if count_arc == count_abc:
        count += 1

print(count)