n, t = map(int, input().split())

def glass_count(n, t):
    if t == 0:
        return 0
    
    if t == 1:
        return 1

    total_glasses = sum(range(1, n+1))
    filled_glasses = min(t, total_glasses)
    remaining_time = t - total_glasses - 1
    
    level = 2
    
    while remaining_time >= level and filled_glasses <= total_glasses * 2:
        remaining_time -= level
        filled_glasses += level
        level += 1
    
    return filled_glasses

result = glass_count(n, t)
print(result)