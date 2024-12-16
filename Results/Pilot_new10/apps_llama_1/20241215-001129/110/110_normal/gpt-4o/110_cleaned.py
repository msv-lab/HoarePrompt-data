def func_1(n, m, r, k):

    def coverage(x, y):
        return (min(x + 1, n - r + 1) - max(x - r + 1 + 1, 0)) * (min(y + 1, m - r + 1) - max(y - r + 1 + 1, 0))
    heap = []
    for x in range(n):
        for y in range(m):
            heapq.heappush(heap, (-coverage(x, y), x, y))
    total_coverage = 0
    for _ in range(k):
        (cov, x, y) = heapq.heappop(heap)
        total_coverage -= cov
    total_positions = (n - r + 1) * (m - r + 1)
    return total_coverage / total_positions
input = sys.stdin.read
(n, m, r, k) = map(int, input().split())
print(f'{func_1(n, m, r, k):.10f}')