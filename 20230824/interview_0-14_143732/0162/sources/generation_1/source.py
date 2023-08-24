n, k = map(int, input().split())
buckets = list(map(int, input().split()))

hours = k
for bucket in buckets:
    if k % bucket == 0:
        hours = min(hours, k // bucket)

print(hours)