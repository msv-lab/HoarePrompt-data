from collections import defaultdict

def dfs(node, parent, adj_list, color_options):
    total_ways = 1
    num_colors = len(color_options[node])
    
    # Remove the parent's color option from the current node
    if parent != 0:
        num_colors -= 1
    
    for child in adj_list[node]:
        if child == parent:
            continue
            
        total_ways *= (num_colors % MOD)
        total_ways %= MOD
        
        num_colors -= 1
        
        total_ways *= dfs(child, node, adj_list, color_options)
        total_ways %= MOD
        
    return total_ways

MOD = 10**9 + 7

# Read input
N, K = map(int, input().split())
adj_list = defaultdict(list)

# Build adjacency list and initialize color options
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# Initialize color options
color_options = defaultdict(set)
for i in range(1, N+1):
    color_options[i] = set(range(1, K+1))

# Calculate number of ways to paint the tree
num_ways = dfs(1, 0, adj_list, color_options)

# Print result
print(num_ways)