t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    (len_a, len_b) = (len(a), len(b))
    (count_a, count_b) = (0, 0)
    d = k // 2
    for i in range(max(len_a, len_b)):
        if len_a > i + 1:
            if a[i] <= k:
                count_a += 1
        if len_b > i + 1:
            if b[i] <= k:
                count_b += 1
    print('YES' if count_a >= d and count_b >= d else 'NO')