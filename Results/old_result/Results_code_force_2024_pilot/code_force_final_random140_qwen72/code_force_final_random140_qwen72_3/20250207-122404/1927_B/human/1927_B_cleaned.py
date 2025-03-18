def func_1(n, a):
    sam = 'abcdefghijklmnopqrstuvqwxyz'
    a_map = {x: 0 for x in range(n)}
    res = ''
    for i in range(n):
        beg = a_map[a[i]]
        res += sam[a_map[a[i]] % 27]
        a_map[a[i]] += 1
    return res
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = func_1(n, a)
    print(ans)