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
        k = int(data[index + 1])
        P_B = int(data[index + 2]) - 1
        P_S = int(data[index + 3]) - 1
        index += 4
        
        p = [int(data[index + i]) - 1 for i in range(n)]
        index += n
        
        a = [int(data[index + i]) for i in range(n)]
        index += n
        
        # Find cycles in the permutation
        visited = [False] * n
        cycles = []
        
        for i in range(n):
            if not visited[i]:
                cycle = []
                x = i
                while not visited[x]:
                    visited[x] = True
                    cycle.append(x)
                    x = p[x]
                cycles.append(cycle)
        
        def max_score(start, k):
            # Find the cycle containing the start position
            for cycle in cycles:
                if start in cycle:
                    break
            
            cycle_length = len(cycle)
            cycle_sum = sum(a[x] for x in cycle)
            
            # Find the best score starting from `start` within the cycle
            max_score = 0
            current_score = 0
            current_position = start
            for _ in range(min(k, cycle_length)):
                current_score += a[current_position]
                max_score = max(max_score, current_score)
                current_position = p[current_position]
            
            if k >= cycle_length:
                # Calculate full cycle contribution
                full_cycles = k // cycle_length
                remaining_moves = k % cycle_length
                
                max_score = max(max_score, current_score + full_cycles * cycle_sum)
                
                # Check remaining moves
                for _ in range(remaining_moves):
                    current_score += a[current_position]
                    max_score = max(max_score, current_score + full_cycles * cycle_sum)
                    current_position = p[current_position]
            
            return max_score
        
        score_B = max_score(P_B, k)
        score_S = max_score(P_S, k)
        
        if score_B > score_S:
            results.append("Bodya")
        elif score_S > score_B:
            results.append("Sasha")
        else:
            results.append("Draw")
    
    sys.stdout.write("\n".join(results) + "\n")