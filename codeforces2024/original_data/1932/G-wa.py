from collections import deque

def min_steps_to_reach_platform_n(n, m, H, levels, changes, passages):
    # Create a graph to represent the connections between platforms
    graph = [[] for _ in range(n)]
    for u, v in passages:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    # Initialize the queue for BFS
    queue = deque([(0, 0)])  # (current platform, number of steps)
    visited = set([(0, levels[0])])  # Set to keep track of visited states (platform, level)
    
    while queue:
        current_platform, steps = queue.popleft()
        
        # If we reached the target platform, return the number of steps
        if current_platform == n - 1:
            return steps
        
        # Explore all possible moves from the current platform
        for next_platform in graph[current_platform]:
            # Check if the levels are the same and the state has not been visited
            if levels[current_platform] == levels[next_platform]:
                next_state = (next_platform, (levels[next_platform] + changes[next_platform]) % H)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_platform, steps + 1))
        
        # Update the level of the current platform
        levels[current_platform] = (levels[current_platform] + changes[current_platform]) % H
    
    # If it is impossible to reach platform n, return -1
    return -1

# Read input
t = int(input())
for _ in range(t):
    n, m, H = map(int, input().split())
    levels = list(map(int, input().split()))
    changes = list(map(int, input().split()))
    passages = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Calculate and print the result
    result = min_steps_to_reach_platform_n(n, m, H, levels, changes, passages)
    print(result)