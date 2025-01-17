import heapq

def solve():
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
        index += 2
        
        a = []
        for i in range(n):
            a.append(list(map(int, data[index:index + n - i])))
            index += n - i
        
        # Precompute all possible interval sums
        interval_sums = []
        for l in range(n):
            for r in range(l, n):
                interval_sums.append((a[l][r - l], l, r))
        
        # Sort intervals by their sum in descending order
        interval_sums.sort(reverse=True, key=lambda x: x[0])
        
        # Use a max-heap to find the k largest beauty values
        max_heap = []
        
        # We will use a bitmask to represent the painted cells
        for mask in range(1 << n):
            beauty = 0
            last = -1
            for l, r in interval_sums:
                if (mask & ((1 << (r + 1)) - (1 << l))) == ((1 << (r + 1)) - (1 << l)):
                    if last < l:
                        beauty += a[l][r - l]
                        last = r
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, beauty)
            else:
                heapq.heappushpop(max_heap, beauty)
        
        # Collect the k largest values
        results.append(sorted(max_heap, reverse=True))
    
    for result in results:
        print(' '.join(map(str, result)))