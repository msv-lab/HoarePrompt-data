(n, s) = map(int, input().split())
volumes = list(map(int, input().split()))
volumes.sort()
total_volume = sum(volumes)
if total_volume < s:
    print(-1)
else:
    min_keg_volume = volumes[0]
    remaining_kvass = s
    for i in range(n):
        if volumes[i] <= min_keg_volume:
            continue
        else:
            possible_to_take = min(volumes[i] - min_keg_volume, remaining_kvass)
            remaining_kvass -= possible_to_take
        if remaining_kvass == 0:
            break
    if remaining_kvass > 0:
        min_keg_volume -= (remaining_kvass + n - 1) // n
    print(min_keg_volume)