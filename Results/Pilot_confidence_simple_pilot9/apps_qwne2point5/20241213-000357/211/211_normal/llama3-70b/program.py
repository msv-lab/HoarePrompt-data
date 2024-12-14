n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

if prefix_sum[n] == 0:
    print("NO")
else:
    print("YES")
    k = 1
    l = 1
    for r in range(1, n + 1):
        if prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]:
            print(k, l, r)
            k += 1
            l = r
    print(k, l, n)
