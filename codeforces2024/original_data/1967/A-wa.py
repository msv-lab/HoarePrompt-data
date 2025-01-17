def max_score(n, k, a):
    # Binary search for the maximum number of complete sets
    left, right = 0, max(a) + k + 1
    
    while left < right:
        mid = (left + right) // 2
        # Calculate the total number of additional cards needed to make `mid` sets
        needed = 0
        for ai in a:
            if ai < mid:
                needed += mid - ai
            if needed > k:
                break
        
        if needed <= k:
            left = mid + 1
        else:
            right = mid
    
    return left - 1

def main():
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
        a = list(map(int, data[index:index + n]))
        index += n
        
        result = max_score(n, k, a)
        results.append(result)
    
    for res in results:
        print(res)