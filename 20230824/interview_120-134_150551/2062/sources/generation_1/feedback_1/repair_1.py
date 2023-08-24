def max_video_power(n, powers):
    powers.sort(reverse=True)
    total_power = 0
    
    for i in range(n):
        divisible = False
        for j in range(i + 1, n):
            if powers[j] % powers[i] == 0:
                total_power += powers[j]
                divisible = True
                break
        if not divisible:
            total_power += powers[i]
            
    return total_power

n = int(input())
powers = list(map(int, input().split()))

result = max_video_power(n, powers)
print(result)