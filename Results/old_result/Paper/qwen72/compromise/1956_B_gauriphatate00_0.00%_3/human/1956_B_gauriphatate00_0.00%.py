def max_points(n, a):
    from collections import Counter
 
    # Count the frequency of each card in your hand
    counter = Counter(a)
 
    # The initial number of pairs we can make
    pairs = sum(1 for count in counter.values() if count == 2)
 
    # The maximum score we can achieve is limited by the minimum of pairs and n // 2
    return min(pairs, n // 2)
 
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        results.append(max_points(n, a))
    
    for result in results:
        print(result)