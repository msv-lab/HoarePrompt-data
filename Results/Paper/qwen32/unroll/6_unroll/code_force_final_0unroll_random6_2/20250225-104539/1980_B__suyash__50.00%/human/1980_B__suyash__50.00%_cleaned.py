t = int(input())
for i in range(t):
    a = input()
    b = list(map(int, a.split()))
    o = input().split()
    n = b[0]
    f = b[1]
    k = b[2]
    if k == n:
        print('YES')
        continue
    fav = o[f - 1]
    dic = {i: o.count(i) for i in o}
    o.sort(reverse=True)
    if o.index(fav) > k - 1:
        print('NO')
        continue
    l = sorted(list(set(o)), reverse=True)
    for i in range(len(l)):
        if fav != l[i]:
            k -= dic[l[i]]
            if k <= 0:
                print('NO')
                break
        else:
            k -= dic[l[i]]
            if k < 0:
                print('MAYBE')
                break
            else:
                print('YES')
                break