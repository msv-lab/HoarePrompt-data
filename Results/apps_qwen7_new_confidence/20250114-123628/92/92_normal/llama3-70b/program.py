T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ok = True
    for x in a:
        if x < 0 or x % k:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
