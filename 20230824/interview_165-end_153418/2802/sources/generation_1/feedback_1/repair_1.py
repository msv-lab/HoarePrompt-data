def solve_puzzle(times, target_score):
    n = 5
    times.sort()
    min_score = sum(times[0:n-1]) / (n - 1)  # Average of the best 3 times
    
    if min_score >= target_score:
        return "infinite"  # Claire can win regardless of her last solve time
    
    max_score = sum(times[1:n]) / (n - 1)  # Average of the worst 3 times
    
    if max_score <= target_score:
        return "impossible"  # Claire cannot win no matter what
    
    # Calculate worst time for Claire's last solve
    last_solve_time = (n * target_score) - sum(times[0:n-1])
    return "{:.2f}".format(last_solve_time)


times = list(map(float, input().split()))
target_score = float(input())

result = solve_puzzle(times, target_score)
print(result)