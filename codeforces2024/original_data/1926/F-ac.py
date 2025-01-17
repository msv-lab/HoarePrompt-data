import sys
input = lambda: sys.stdin.readline().rstrip()  # Fast input

# Memoization dictionary to store results of subproblems
memo = {}

def solve():
    # Read the grid for the current test case
    s = []
    for _ in range(7):
        s.append(input())
    
    # Recursive function to find minimum operations
    def dfs(state, parity):
        if state == 0:  # Base case: no violations left
            return 0
        if (state, parity) in memo:  # Check memoization
            return memo[(state, parity)]
        
        t = []  # List to store potential operations
        for i in range(7):
            for j in range(7):
                if (i + j) % 2 == parity:  # Check parity
                    data = [0, 0]  # [count of violations, bitmask of cells to flip]
                    # Check the cell and its diagonal neighbors
                    for x, y in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1), (i, j)]:
                        if 0 <= 7 * x + y < 49 and state & (1 << (7 * x + y)):
                            data[0] += 1
                            data[1] |= 1 << (7 * x + y)
                    if data[0] > 0:  # If there is a violation
                        t.append(data.copy())
        
        t.sort(reverse=True)  # Sort operations by effectiveness
        res = 212  # Initialize result with a large number
        for cnt, cancel in t:
            # Try fixing the grid by flipping the cells in 'cancel'
            res = min(res, 1 + dfs(state ^ cancel, parity))
        
        memo[(state, parity)] = res  # Memoize the result
        return res
    
    # Initial state for both parities
    state = [0, 0]
    for i in range(1, 6):
        for j in range(1, 6):
            # Check if the cell (i, j) is part of a violation
            if s[i][j] == 'B' and s[i-1][j-1] == 'B' and s[i+1][j-1] == 'B' and s[i+1][j+1] == 'B' and s[i-1][j+1] == 'B':
                state[(i + j) % 2] |= 1 << (7 * i + j)
    
    # Calculate the result for both parities and sum them
    res = dfs(state[0], 0) + dfs(state[1], 1)
    print(res)

# Read number of test cases
T = int(input())
for _ in range(T):
    solve()