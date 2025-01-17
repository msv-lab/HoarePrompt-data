n, k, d = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

i = 0
while i < n:
    j = i + 1
    while j < n and a[j] - a[i] <= d:
        j += 1
    if j - i < k:
        print("NO")
        exit()
    i = j

print("YES")
