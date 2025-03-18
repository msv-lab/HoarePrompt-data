def count_polygons(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
    return sum(v // 4 for v in freq.values())
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_polygons(arr))