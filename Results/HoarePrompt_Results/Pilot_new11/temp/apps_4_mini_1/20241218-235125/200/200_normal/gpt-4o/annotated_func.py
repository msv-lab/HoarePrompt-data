#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, s is a non-negative integer such that 1 <= s <= 10^12, and v is a list of n integers where each integer v[i] satisfies 1 <= v[i] <= 10^9.
def func():
    n, s = map(int, input().split())
    volumes = list(map(int, input().split()))
    volumes.sort()
    total_volume = sum(volumes)
    if (total_volume < s) :
        print(-1)
    else :
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
            
        #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 1000; `remaining_kvass` equals the initial `s` minus the total kvass taken from eligible volumes; `possible_to_take` is the last value taken from the eligible volumes, or remains undefined if no volumes were eligible; `i` is `n`, representing all volumes attempted.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an integer such that 1 <= `n` <= 1000; if `remaining_kvass` is greater than 0, `min_keg_volume` is decreased by `(remaining_kvass + n - 1) // n`. If `remaining_kvass` is not greater than 0, no changes are made to `min_keg_volume`.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 <= `n` <= 1000; `s` is a non-negative integer satisfying 1 <= `s` <= 10^12; `volumes` is a sorted list of `n` integers; `total_volume` is the sum of integers in `volumes`. If `total_volume` is less than `s`, the function maintains the current values of `n`, `s`, and `volumes`, and `total_volume` remains less than `s`. If `total_volume` is greater than or equal to `s`, and `remaining_kvass` > 0, then `min_keg_volume` is adjusted by subtracting `(remaining_kvass + n - 1) // n`; otherwise, `min_keg_volume` remains unchanged.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 1000), a non-negative integer `s` (1 ≤ s ≤ 10^12), and a list of `n` integers `v` (1 ≤ v[i] ≤ 10^9). It first reads and processes these inputs, then computes the total volume of kvass represented by `v`. If the total volume is less than `s`, it outputs -1, indicating that the required amount cannot be met. If the total volume is sufficient, the function attempts to find and potentially adjust the minimum volume of kvass (`min_keg_volume`) needed to fulfill the requirement `s`. This is done by attempting to calculate how much kvass can be taken from volumes greater than the minimum and adjusting `min_keg_volume` accordingly. Finally, it prints the resulting `min_keg_volume`. The edge cases include handling the scenario where the total volume of kvass is exactly equal to `s`, which does not require any adjustments. Additionally, it also handles cases where no eligible volumes are greater than `min_keg_volume`. In these cases, `min_keg_volume` may be adjusted downward if there is remaining kvass that could not be taken from available volumes.

