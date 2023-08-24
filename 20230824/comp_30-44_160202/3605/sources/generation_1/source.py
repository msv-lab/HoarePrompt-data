n, k = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

min_diff = float('inf')
for i in range(n-k+1):
    diff = trees[i+k-1] - trees[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)