for _ in range(int(input())):
    n = int(input())
    (*inp,) = map(int, input().split())
    x = y = n + 1
    ans = 0
    for a in inp:
        if a <= x:
            x = a
        elif a <= y:
            y = a
        else:
            x == y
            y = a
            ans += 1
    print(ans)