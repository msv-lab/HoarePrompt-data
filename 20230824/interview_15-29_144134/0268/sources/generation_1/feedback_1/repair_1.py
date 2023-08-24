n, k, d = map(int, input().split())
pencils = list(map(int, input().split()))

boxes = 0  # Initialize boxes with 0
i = 0

while i < n:
    j = i + 1
    while j < n and pencils[j] - pencils[i] <= d:
        j += 1
    if j - i >= k:
        boxes += 1
        i = j  # Increment i to the next pencil after j
    else:
        i += 1

if boxes >= k:
    print("YES")
else:
    print("NO")