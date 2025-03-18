from collections import deque

def puzzle_to_string(puzzle):
    return puzzle[0] + puzzle[1]

def bfs(start):
    queue = deque([start])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    while queue:
        current = queue.popleft()
        empty_pos = current.index('X')
        empty_row, empty_col = divmod(empty_pos, 2)
        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 2:
                new_pos = new_row * 2 + new_col
                new_state = list(current)
                new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
                new_state_str = ''.join(new_state)
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append(new_state_str)
    return visited

# Read input
bessie_puzzle = [input().strip() for _ in range(2)]
elsie_puzzle = [input().strip() for _ in range(2)]

# Convert puzzles to string representation
bessie_start = puzzle_to_string(bessie_puzzle)
elsie_start = puzzle_to_string(elsie_puzzle)

# Perform BFS for both puzzles
bessie_reachable = bfs(bessie_start)
elsie_reachable = bfs(elsie_start)

# Check if there is any common state
if bessie_reachable & elsie_reachable:
    print("YES")
else:
    print("NO")
