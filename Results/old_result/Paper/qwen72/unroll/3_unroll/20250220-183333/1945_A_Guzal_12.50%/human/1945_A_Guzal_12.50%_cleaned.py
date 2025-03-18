n = int(input())
for i in range(n):
    (a, b, c) = map(int, input().split())
    k = 0
    if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
        print(-1)
    else:
        k += a + (b + c) // 3
        if (b + c) % 3 != 0:
            k += 1
        print(k)