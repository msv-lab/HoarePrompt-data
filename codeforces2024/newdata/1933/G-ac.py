MOD = 998244353

def ok(x, y):
    # Determine the expected shape at position (x, y) based on a pattern
    # The pattern alternates shapes in a checkerboard-like fashion
    return (y % 2) ^ (x // 2 % 2)

def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, m, q = map(int, input().split())  # Grid dimensions and number of operations
        print(8)  # Initial number of valid configurations (before any operations)
        
        # Array to track valid configurations
        s = [1] * 8
        
        for _ in range(q):
            x, y, shape = input().split()
            x, y = int(x), int(y)  # Convert coordinates to integers
            
            # Determine if the shape is a circle (1) or square (0)
            if shape == "circle":
                is_circle = 1
            else:
                is_circle = 0
            
            # Check the placement against the pattern and update validity
            if is_circle == ok(x, y):
                s[0] = 0
            if is_circle == ok(x, y + 1):
                s[1] = 0
            if is_circle == ok(x + 1, y):
                s[2] = 0
            if is_circle == ok(x + 1, y + 1):
                s[3] = 0
            
            # Swap x and y to check the other diagonal
            x, y = y, x
            if is_circle == ok(x, y):
                s[4] = 0
            if is_circle == ok(x, y + 1):
                s[5] = 0
            if is_circle == ok(x + 1, y):
                s[6] = 0
            if is_circle == ok(x + 1, y + 1):
                s[7] = 0
            
            # Output the number of valid configurations after the operation
            print(sum(s) % MOD)

solve()