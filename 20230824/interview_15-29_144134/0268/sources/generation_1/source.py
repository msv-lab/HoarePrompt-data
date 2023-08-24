n, k, d = map(int, input().split())
pencils = list(map(int, input().split()))

pencils.sort()

boxes = 1
i = 0

while i < n - 1:
    j = i + 1
    while j < n and pencils[j] - pencils[i] <= d:
        j += 1
    if j - i >= k:
        boxes += 1
        i = j - 1
    else:
        i += 1

if boxes >= k:
    print("YES")
else:
    print("NO")