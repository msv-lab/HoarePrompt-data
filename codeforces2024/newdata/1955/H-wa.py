def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        grid = []
        for _ in range(n):
            grid.append(data[index])
            index += 1
        
        towers = []
        for _ in range(k):
            x = int(data[index]) - 1
            y = int(data[index + 1]) - 1
            p = int(data[index + 2])
            towers.append((x, y, p))
            index += 3
        
        # Find the path
        path = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    path.append((i, j))
        
        # Precompute damage for each tower at each path cell for different ranges
        max_range = 50  # max possible range to consider
        damage_at_path = [[0] * len(path) for _ in range(k)]
        
        for t_idx, (tx, ty, p) in enumerate(towers):
            for path_idx, (px, py) in enumerate(path):
                for r in range(max_range + 1):
                    if (px - tx) ** 2 + (py - ty) ** 2 <= r ** 2:
                        damage_at_path[t_idx][path_idx] = p
        
        # Function to check if a given base health h is possible
        def can_survive(h):
            # Try all combinations of ranges for towers
            from itertools import combinations
            
            # Calculate the health increase for each range
            health_increase = [3 ** r for r in range(max_range + 1)]
            
            # Try all combinations of ranges for the towers
            for ranges in combinations(range(1, max_range + 1), k):
                total_health = h + sum(health_increase[r] for r in ranges)
                
                # Calculate total damage
                total_damage = 0
                for path_idx in range(len(path)):
                    damage = 0
                    for t_idx in range(k):
                        r = ranges[t_idx]
                        if (path[path_idx][0] - towers[t_idx][0]) ** 2 + (path[path_idx][1] - towers[t_idx][1]) ** 2 <= r ** 2:
                            damage += towers[t_idx][2]
                    total_damage += damage
                
                if total_damage >= total_health:
                    return True
            
            return False
        
        # Binary search for the maximum base health h
        low, high = 0, 10**9
        answer = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_survive(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(answer)
    
    for result in results:
        print(result)