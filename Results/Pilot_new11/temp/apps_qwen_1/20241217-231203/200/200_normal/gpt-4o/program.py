# Read input values
n, s = map(int, input().split())
volumes = list(map(int, input().split()))

# Sort the volumes
volumes.sort()

# Calculate the total volume of all kegs
total_volume = sum(volumes)

# Check if we have enough kvass to pour s liters
if total_volume < s:
    print(-1)
else:
    # Calculate the maximum possible volume in the least filled keg
    min_keg_volume = volumes[0]
    remaining_kvass = s

    # Distribute remaining kvass to make each keg as even as possible
    for i in range(n):
        if volumes[i] <= min_keg_volume:
            continue
        else:
            possible_to_take = min(volumes[i] - min_keg_volume, remaining_kvass)
            remaining_kvass -= possible_to_take
        
        if remaining_kvass == 0:
            break
    
    # Calculate the final volume in the least filled keg
    if remaining_kvass > 0:
        min_keg_volume -= (remaining_kvass + n - 1) // n
    
    print(min_keg_volume)
