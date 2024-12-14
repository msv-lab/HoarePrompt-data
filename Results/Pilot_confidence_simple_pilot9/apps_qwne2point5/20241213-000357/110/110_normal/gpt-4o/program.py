import heapq

def max_expected_fishes(n, m, r, k):
    # Calculate the number of positions each cell can be covered by the scoop-net
    def coverage(x, y):
        return (min(x + 1, n - r + 1) - max(x - r + 1 + 1, 0)) * (min(y + 1, m - r + 1) - max(y - r + 1 + 1, 0))

    # Use a max-heap to place fishes in the most frequently covered cells first
    heap = []
    for x in range(n):
        for y in range(m):
            heapq.heappush(heap, (-coverage(x, y), x, y))
    
    total_coverage = 0
    for _ in range(k):
        cov, x, y = heapq.heappop(heap)
        total_coverage -= cov  # cov is negative, so we subtract to add the positive value

    # Calculate the maximum expected number of caught fishes
    total_positions = (n - r + 1) * (m - r + 1)
    return total_coverage / total_positions

# Read input
import sys
input = sys.stdin.read
n, m, r, k = map(int, input().split())

# Print the result
print(f"{max_expected_fishes(n, m, r, k):.10f}")
