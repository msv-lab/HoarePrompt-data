N = int(input())
h = list(map(int, input().split()))
max_height = max(h) - 1
operations = 0

for i in range(1, max_height+1):
    l = r = None
    for j in range(N):
        if h[j] >= i:
            if l is None:
                l = j + 1
            r = j + 1
    if l is not None and r is not None:
        operations += 1

print(operations)