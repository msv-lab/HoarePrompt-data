import math

def solve():
    # Read input
    n, r = input().split()
    n = int(n)
    r = float(r)
    
    # The step between trees is 2 * r
    step = 2 * r
    
    # List to hold the positions of trees
    trees = []
    
    # Try to place trees on the grid
    for x in range(int(r), n + 1, int(step)):
        for y in range(int(r), n + 1, int(step)):
            # Check if the tree can be placed within bounds
            if x <= n and y <= n:
                trees.append((x, y))
    
    # Output the results
    print(len(trees))
    for tree in trees:
        print(tree[0], tree[1])

# Run the function to process the input and output the result
solve()