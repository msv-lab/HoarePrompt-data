t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    hd = 0
    for i in range(n):
        if s1[i] != s2[i]:
            hd += 1
    res = abs(s1.count('1') - s2.count('1'))
    print(res + abs(hd - res) // 2)