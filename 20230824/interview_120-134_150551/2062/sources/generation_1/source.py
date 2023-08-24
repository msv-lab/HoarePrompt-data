def max_video_power(n, powers):
    powers.sort(reverse=True)
    max_power = powers[0]
    total_power = max_power
    
    for power in powers[1:]:
        if power % max_power == 0:
            total_power += power
            break
            
    return total_power

n = int(input())
powers = list(map(int, input().split()))

result = max_video_power(n, powers)
print(result)