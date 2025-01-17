def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx]) 
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        min_val = float('inf')
        max_val = float('-inf')
        for num in a:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        max_expression_value = 4 * (max_val - min_val)
        results.append(max_expression_value)
    print("\n".join(map(str, results)))