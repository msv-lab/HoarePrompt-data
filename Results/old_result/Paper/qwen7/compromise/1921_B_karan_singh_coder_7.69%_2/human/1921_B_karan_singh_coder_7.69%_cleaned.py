for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    s1 = s.count('1')
    t1 = t.count('1')
    cnt = 0
    for i in range(n):
        cnt += s[i] != t[i]
    if s1 == t1:
        print(s1 if cnt else 0)
    else:
        d = abs(s1 - t1)
        print((cnt - d) // 2 + d)