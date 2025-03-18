for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
 
    if len(set(a)) == 1 and len(set(c)) == 1 and a[0] == c[0]:
        print(0)
        continue
    a.sort()
    c.sort(reverse=True)
    if len(a) == 1:
        print(max(abs(a[0]-max(c)), abs(a[0]-min(c))))
        continue
    i,j, ans = 0, 1, 0
    for k in range(len(a)):
        t1 =abs(a[i]-c[i])
        t2 = abs(a[len(a)-j]-c[len(c)-j])
        if t2 > t1:
            j += 1
        else:
            i += 1
        ans += max(t1, t2)
    print(ans)