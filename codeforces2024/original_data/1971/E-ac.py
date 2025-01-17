import bisect

def find_time(a, b, d):
    # Find the index of the rightmost value less than or equal to d
    idx = bisect.bisect_right(a, d) - 1

    if idx == -1:
        return 0

    # Linear interpolation formula to find the time
    segment_start_distance = a[idx]
    segment_end_distance = a[idx + 1] if idx + 1 < len(a) else a[idx]
    segment_start_time = b[idx]
    segment_end_time = b[idx + 1] if idx + 1 < len(b) else b[idx]

    if segment_start_distance == segment_end_distance:
        return segment_start_time

    # Interpolate the time
    time_at_d = segment_start_time + ((d - segment_start_distance) * (segment_end_time - segment_start_time)) // (segment_end_distance - segment_start_distance)

    return int(time_at_d)

# Reading input
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    q = int(data[index + 2])
    index += 3

    a = [0] + [int(data[index + i]) for i in range(k)]
    b = [0] + [int(data[index + k + i]) for i in range(k)]
    index += 2 * k

    queries = [int(data[index + i]) for i in range(q)]
    index += q

    for query in queries:
        results.append(find_time(a, b, query))

# Printing results
print("\n".join(map(str, results)))