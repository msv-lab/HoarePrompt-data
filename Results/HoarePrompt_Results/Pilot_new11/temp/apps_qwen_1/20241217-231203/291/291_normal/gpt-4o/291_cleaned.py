def func_1(n):
    min_segments_needed = float('inf')
    for a in range(1, int(math.sqrt(n)) + 1):
        b = (n + a - 1) // a
        segments_needed = 2 * (a + b)
        min_segments_needed = min(min_segments_needed, segments_needed)
    return min_segments_needed
n = int(input().strip())
print(func_1(n))