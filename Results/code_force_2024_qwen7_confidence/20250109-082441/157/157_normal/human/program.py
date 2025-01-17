def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        k = int(data[index])
        index += 1
        n = 2 ** k
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Sort the array to easily find the largest elements
        a.sort(reverse=True)
        
        # Calculate the scores for each t from 1 to k
        scores = []
        for t in range(1, k + 1):
            # Bob can erase 2^(k-t) elements, so Alice can keep 2^t elements
            # We want the maximum of the largest 2^t elements
            max_score = max(a[:2**t])
            scores.append(max_score)
        
        results.append(" ".join(map(str, scores)))
    
    print("\n".join(results))