#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^3, s is an integer such that 1 <= s <= 10^12, and v_i is a list of n integers such that 1 <= v_i <= 10^9 for all i.
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
            
        #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 10^3, `s` is an input integer between 1 and 10^12, `v_i` is a list of n integers such that 1 <= v_i <= 10^9 for all i, `volumes` is a sorted list of input integers, `total_volume` equals `sum(volumes)` and is greater than or equal to the original value of `s`, `min_keg_volume` equals the smallest integer in `volumes`, and `remaining_kvass` is either 0 (indicating the target volume `s` was met or exceeded) or a value greater than 0 (indicating the target volume `s` could not be fully met due to volume constraints).
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an input integer between 1 and 10^3, `s` is an input integer between 1 and 10^12, `v_i` is a list of n integers such that 1 <= v_i <= 10^9 for all i, `volumes` is a sorted list of input integers, `total_volume` equals `sum(volumes)` and is greater than or equal to the original value of `s`. If `remaining_kvass` is greater than 0, then `min_keg_volume` equals `min_keg_volume - (remaining_kvass + n - 1) // n` and `remaining_kvass` is greater than 0. Otherwise, the state of the variables remains unchanged as there is no else part in the code.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an input integer between 1 and 10^3, `s` is an input integer between 1 and 10^12, `v_i` is a list of n integers such that 1 <= v_i <= 10^9 for all i, `volumes` is a sorted list of input integers, and `total_volume` equals the sum of all elements in `volumes`. If `total_volume` is less than `s`, then the value -1 has been printed and returned at the output state. Otherwise, `total_volume` is greater than or equal to the original value of `s`, `min_keg_volume` has been printed, and if `remaining_kvass` is greater than 0, then `min_keg_volume` equals `min_keg_volume - (remaining_kvass + n - 1) // n` and the value of `min_keg_volume` has been returned at the output state.
#Overall this is what the function does:The function calculates and returns the minimum keg volume required to distribute a target volume of kvass `s` among `n` kegs with different volumes `v_i`, where `n` is an integer between 1 and 10^3, `s` is an integer between 1 and 10^12, and `v_i` is a list of `n` integers between 1 and 10^9. If the total volume of all kegs is less than the target volume `s`, the function returns -1. Otherwise, it attempts to distribute the target volume `s` among the kegs, starting from the smallest keg, and returns the minimum keg volume required to meet or exceed the target volume. If the target volume cannot be fully met due to volume constraints, the function adjusts the minimum keg volume by subtracting the remaining volume divided among the kegs. The function performs input validation implicitly by handling cases where the total volume is less than the target volume, and it handles edge cases where the target volume is greater than the total volume of all kegs. The function returns an integer value representing the minimum keg volume required to distribute the target volume of kvass.

