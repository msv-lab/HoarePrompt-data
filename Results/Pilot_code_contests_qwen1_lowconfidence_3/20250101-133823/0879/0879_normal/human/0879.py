from bisect import bisect_left
n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

min_r = 0

for el in a:
    i = bisect_left(b, el)
    if i == 0:
        min_r = max(min_r, abs(el - b[0]))
    elif i == m:
        min_r = max(min_r, abs(el - b[m-1]))
    elif i == m - 1:
        min_r = max(min_r, min(abs(el - b[m - 1]), abs(el - b[m - 2])))
    else:
        min_r = max(min_r, min(abs(el - b[i + 1]), abs(el - b[i - 1]), abs(el-b[i])))

print(min_r)

