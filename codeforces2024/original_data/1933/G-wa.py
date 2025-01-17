MOD = 998244353

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
        m = int(data[index + 1])
        q = int(data[index + 2])
        index += 3
        
        operations = []
        for __ in range(q):
            r = int(data[index])
            c = int(data[index + 1])
            shape = data[index + 2]
            operations.append((r, c, shape))
            index += 3
        
        # Initial number of ways
        total_cells = n * m
        initial_ways = pow(2, total_cells, MOD)
        results.append(initial_ways)
        
        # Grid to store the current state
        grid = {}
        valid = True
        
        def check_violation(r, c):
            # Check horizontal
            if (r, c) in grid and (r, c+1) in grid and (r, c+2) in grid:
                if grid[(r, c)] == grid[(r, c+1)] == grid[(r, c+2)]:
                    return True
            # Check vertical
            if (r, c) in grid and (r+1, c) in grid and (r+2, c) in grid:
                if grid[(r, c)] == grid[(r+1, c)] == grid[(r+2, c)]:
                    return True
            # Check diagonal \
            if (r, c) in grid and (r+1, c+1) in grid and (r+2, c+2) in grid:
                if grid[(r, c)] == grid[(r+1, c+1)] == grid[(r+2, c+2)]:
                    return True
            # Check diagonal /
            if (r, c) in grid and (r+1, c-1) in grid and (r+2, c-2) in grid:
                if grid[(r, c)] == grid[(r+1, c-1)] == grid[(r+2, c-2)]:
                    return True
            return False
        
        for r, c, shape in operations:
            if not valid:
                results.append(0)
                continue
            
            grid[(r, c)] = shape
            
            # Check for violations around the newly placed cookie
            if check_violation(r, c) or check_violation(r, c-1) or check_violation(r, c-2) or \
               check_violation(r-1, c) or check_violation(r-2, c):
                valid = False
                results.append(0)
            else:
                # Calculate the number of ways for the remaining empty cells
                remaining_cells = total_cells - len(grid)
                ways = pow(2, remaining_cells, MOD)
                results.append(ways)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")