def solve():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the number of forbidden cells
        forbidden_cells = set()
        for _ in range(n):
            c, d = map(int, input().split())  # Read each forbidden cell
            forbidden_cells.add((c, d))
        
        # Check for the specific 2x2 block from (0,0)
        if (0, 0) in forbidden_cells and (1, 0) in forbidden_cells and (0, 1) in forbidden_cells and (1, 1) in forbidden_cells:
            print("NO")
        else:
            print("YES")

# Run the solve function
solve()