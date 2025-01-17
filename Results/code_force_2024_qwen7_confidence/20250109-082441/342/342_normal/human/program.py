t = int(input())

for tc in range(t):
    n = int(input())
    s = input()
    mn = 0
    mx = 0
    cur = 0

    for c in s:

        if (cur % 2 == 0) == (c == '1'):
            cur = cur + 1
        else:
            cur = cur - 1

        mn = min(mn, cur)
        mx = max(mx, cur)

    print(mx - mn)