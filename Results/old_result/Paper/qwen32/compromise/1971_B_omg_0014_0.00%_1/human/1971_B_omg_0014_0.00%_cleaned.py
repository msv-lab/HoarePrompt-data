n = int(input())
for i in range(n):
    s = input()
    a = set(s)
    if len(a) == 2:
        print('NO')
    else:
        print('YES')
        b = ''.join(sorted(s))
        c = ''.join(sorted(s, reverse=True))
        if b == s:
            print(c)
        else:
            print(b)