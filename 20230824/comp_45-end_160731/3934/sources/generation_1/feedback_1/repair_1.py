def can_achieve_configuration(n, edges):
    degrees = {}
    
    # Compute the degree of each node
    for u, v in edges:
        degrees[u] = degrees.get(u, 0) + 1
        degrees[v] = degrees.get(v, 0) + 1
        
    # Check if a valid configuration is possible
    if len(degrees) < 4:
        return "YES"
    
    return "NO"

# Read inputs
n = int(input())
edges = []
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Call the function and print the result
result = can_achieve_configuration(n, edges)
print(result)