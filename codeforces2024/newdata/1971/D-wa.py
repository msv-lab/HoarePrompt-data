t = int(input())
for _ in range(t):
    s = input()
    p = 1
    q = 1
    for i in range(len(s)):
        if p:
            if s[i] == '1':
                p = 0
        else:
            if s[i] == '0':
                q += 1
                p = 1
    print(q)