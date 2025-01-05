def func_1(lst, c):
    temp = []
    for i in c:
        temp.append(lst[i])
    awk = -1
    if 0 in c and n - 1 in c:
        for i in range(len(temp)):
            awk = max(awk, temp[i] - temp[i - 1])
    if awk == -1:
        return 10000000000
    else:
        return awk
n = int(input())
lst = map(int, raw_input().split())
k = 1
awk = 10000000000
comb = list(itertools.combinations(range(n), n - k))
for c in comb:
    awk = min(awk, func_1(lst, c))
print(awk)