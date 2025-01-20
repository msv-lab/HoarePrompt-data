n = int(input())
if n == 1:
    print(-1)
else:
    for m in range(n, int(1e+18) + 1):
        k = (m ** 2 - n ** 2) ** 0.5
        if k == int(k):
            print(m, int(k) + n)
            break
    else:
        print(-1)