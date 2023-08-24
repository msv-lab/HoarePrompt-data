
from collections import defaultdict

def can_achieve_configuration(n, edges):
    degrees = defaultdict(int)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    for degree in degrees.values():
        if degree == 2:
            return "NO"
    
    return "YES"

n = int(input())
edges = []
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

result = can_achieve_configuration(n, edges)
print(result)
