t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    i = 0
    for j in range(n):
        if b[j] < a[i]:
            cnt += 1
        else:
            i += 1
    print(cnt)