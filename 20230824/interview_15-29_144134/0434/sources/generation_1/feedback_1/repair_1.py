n = int(input())
a = list(map(int, input().split()))

count = 0
progressions = 0

if a[0] != -1:
    count = 1

for i in range(1, n):
    if a[i] != -1:
        if a[i] != a[i-1] + (a[i-1] - a[i-2]):
            progressions += 1
        count += 1

if count == 0:
    print(1)
else:
    print(progressions + 1)