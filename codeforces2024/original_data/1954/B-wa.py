for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = l[0]
    for x in range(n//2 + 1):
        if l[x] != ans or l[n-1-x] != ans:
            print(x)
            break
    else:
        print(-1)
    