def solve(n):
    # For n, we will output n points
    # A simple strategy is to place points in a diagonal or near-diagonal pattern
    points = []
    for i in range(n):
        # Place points in a diagonal pattern
        # (i+1, (i*2 % n) + 1) ensures we stay within bounds and spread points
        x = i + 1
        y = (i * 2 % n) + 1
        points.append((x, y))
    return points

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(t):
        n = int(data[i + 1])
        result = solve(n)
        results.append(result)
    
    for result in results:
        for x, y in result:
            print(x, y)

if __name__ == "__main__":
    main()