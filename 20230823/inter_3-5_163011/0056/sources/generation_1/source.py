n, t = map(int, input().split())

def glass_count(n, t):
    if t == 0:
        return 0
    
    if t == 1:
        return 1
    
    if t <= (n * (n + 1) // 2):
        return t
    
    total_glasses = (n * (n + 1) // 2)
    filled_glasses = total_glasses
    remaining_time = t - total_glasses
    
    level = 2
    
    while remaining_time >= level and filled_glasses < total_glasses * 2:
        remaining_time -= level
        filled_glasses += 1
        level += 1
    
    return filled_glasses

result = glass_count(n, t)
print(result)