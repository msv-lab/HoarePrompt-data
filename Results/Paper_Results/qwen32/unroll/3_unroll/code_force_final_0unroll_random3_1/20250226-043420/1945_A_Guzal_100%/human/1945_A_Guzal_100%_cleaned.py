n = int(input())
for i in range(n):
    (a, b, c) = map(int, input().split())
    k = 0
    if b % 3 != 0 and b % 3 + c < 3:
        print(-1)
    else:
        k += a + (b + c) // 3
        if (b + c) % 3 != 0:
            k += 1
        print(k)