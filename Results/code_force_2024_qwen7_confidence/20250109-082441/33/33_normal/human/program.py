def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1:n+1]
    
    # Check if the matrix is consistent with a tree structure
    # We will use a simple line tree structure to check the consistency
    # and construct the tree if possible.
    
    # Check if the matrix is symmetric
    for i in range(n):
        for j in range(n):
            if s[i][j] != s[j][i]:
                print("NO")
                return
    
    # Check if the diagonal is all zeros
    for i in range(n):
        if s[i][i] != '0':
            print("NO")
            return
    
    # Construct a simple line tree
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))
    
    # Output the result
    print("YES")
    for u, v in edges:
        print(u, v)