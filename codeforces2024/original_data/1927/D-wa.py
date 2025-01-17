t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        l,r = map(int,input().split())
        l -= 1
        r -= 1
        left = -1
        right = -1
        seen = set()
        for i in range(l,r+ 1):
            if not seen:
                seen.add(a[i])
                left = i
            elif a[i] not in seen:
                right = i
                break
            else:
                continue
        if right == - 1:
            print(-1,end=" ")
            print(-1)
        else:
            print(left,end=" ")
            print(right)