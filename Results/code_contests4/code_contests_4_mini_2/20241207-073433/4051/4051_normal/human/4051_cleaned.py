def func_1():
    arr = list(map(int, raw_input().strip().split(' ')))
    return arr
(n, k) = map(int, raw_input().strip().split(' '))
if n >= k:
    x = k - 1
    print(max(0, x // 2))
else:
    l = k - n
    l = n - l + 1
    print(max(0, l // 2))