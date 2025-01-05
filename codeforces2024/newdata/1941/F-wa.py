import bisect
import sys
input = sys.stdin.read

def min_imbalance(n, m, k, a, d, f):
    a.sort()
    d.sort()
    f.sort()
    curr_imbalance = max(a[i] - a[i - 1] for i in range(1, n))
    min_imbalance = curr_imbalance

    for new_val in [d[0] + f[0], d[0] + f[-1], d[-1] + f[0], d[-1] + f[-1]]:
        pos = bisect.bisect_left(a, new_val)
        left_gap = new_val - a[pos - 1] if pos > 0 else 0
        right_gap = a[pos] - new_val if pos < n else 0
        min_imbalance = min(min_imbalance, max(curr_imbalance, left_gap, right_gap))
        
    return min_imbalance

def solve():
    data = input().split()
    idx, t = 0, int(data[0])
    idx += 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, data[idx:idx + 3])
        idx += 3
        a = list(map(int, data[idx:idx + n]))
        idx += n
        d = list(map(int, data[idx:idx + m]))
        idx += m
        f = list(map(int, data[idx:idx + k]))
        idx += k
        results.append(min_imbalance(n, m, k, a, d, f))

    print("\n".join(map(str, results)))