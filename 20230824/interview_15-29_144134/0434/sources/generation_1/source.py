n = int(input())
a = list(map(int, input().split()))

count = 1
progressions = 0

for i in range(1, n):
    if a[i] == -1:
        count += 1
    elif a[i-1] == -1:
        progressions += 1
        count = 1
    elif a[i] - a[i-1] != a[i-1] - a[i-2]:
        progressions += 1
        count = 1

print(progressions + 1)