from sys import stdout


def query(a, b, c, d):
    print('?', a, b, c, d)
    stdout.flush()
    x = input()
    stdout.flush()
    return x


for _ in range(int(input())):
    n = int(input())
    mx, ans1, ans2 = 0, 0, 0
    v = []
    for i in range(1, n):
        c = query(ans1, ans1, i, i)
        if c == '<':
            ans1 = i
    v.append(0)
    for i in range(1, n):
        c = query(mx, ans1, i, ans1)
        if c == '<':
            mx, v = i, [i]
        elif c == '=':
            v.append(i)
    ans2 = v[0]
    for i in range(1, len(v)):
        c = query(ans2, ans2, v[i], v[i])
        if c == '>':
            ans2 = v[i]
    print("!", ans1, ans2)
    stdout.flush()