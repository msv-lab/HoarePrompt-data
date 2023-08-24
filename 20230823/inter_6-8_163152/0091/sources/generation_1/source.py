t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    v = [0] * n
    possible = True

    for i in range(62):
        val = k**i
        if all((v[j] >> i) & 1 == (a[j] >> i) & 1 for j in range(n)):
            continue
        cnt = sum((a[j] >> i) & 1 for j in range(n))
        if cnt == 0 or cnt == n:
                continue
        possible = False
        break

    if possible:
        print("YES")
    else:
        print("NO")