n = int(input())
arr = list(map(int, input().split()))
min_val = min(arr)
min_indices = [i for i, x in enumerate(arr) if x == min_val]
min_indices.sort()
min_distance = float('inf')
for i in range(1, len(min_indices)):
    min_distance = min(min_distance, min_indices[i] - min_indices[i-1])
print(min_distance)
