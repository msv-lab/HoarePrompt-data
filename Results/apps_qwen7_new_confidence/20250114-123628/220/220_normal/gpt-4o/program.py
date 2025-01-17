def can_reach_finish(n, m, s, d, obstacles):
    obstacles.sort()
    
    # Check if the athlete can make it to the finish line
    if obstacles[0] < s:
        return "IMPOSSIBLE"
    
    result = []
    current_position = 0
    
    for i in range(n):
        if (obstacles[i] - current_position) < s:
            return "IMPOSSIBLE"
        
        # Run to the obstacle - s
        run_length = obstacles[i] - s - current_position
        if run_length > 0:
            result.append(f"RUN {run_length}")
            current_position += run_length
        
        # Find the furthest obstacle we can jump over
        jump_end = obstacles[i]
        while i + 1 < n and obstacles[i + 1] <= jump_end + d:
            jump_end = obstacles[i + 1]
            i += 1
        
        # Check if the jump is within the permissible distance
        jump_length = jump_end - current_position
        if jump_length > d:
            return "IMPOSSIBLE"
        
        result.append(f"JUMP {jump_length}")
        current_position += jump_length
        
        if current_position >= m:
            return "IMPOSSIBLE"
    
    if current_position < m:
        result.append(f"RUN {m - current_position}")
    
    return "\n".join(result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = int(data[2])
    d = int(data[3])
    obstacles = list(map(int, data[4:]))
    
    result = can_reach_finish(n, m, s, d, obstacles)
    print(result)
