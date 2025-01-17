def max_k_for_all_ones(n, s):
    zero_count = s.count('0')
    
    if zero_count == 0:
        return n
    
    max_k = 1
    for k in range(1, n + 1):
        if zero_count % k == 0:
            max_k = k
    
    return max_k

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        
        result = max_k_for_all_ones(n, s)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()