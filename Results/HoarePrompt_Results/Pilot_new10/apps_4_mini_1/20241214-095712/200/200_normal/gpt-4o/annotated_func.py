#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, s is a non-negative integer such that 1 <= s <= 10^12, and v is a list of n integers where each integer v_i (1 <= v_i <= 10^9) represents the volume of the i-th keg.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer in the range 1 to 1000, `remaining_kvass` is either 0 (if sufficient kvass was taken) or is reduced from the original value of `s` by the minimum of the effective volumes taken, `i` is equal to the count of valid `volumes` processed before remaining_kvass becomes 0 or all iterations complete, and all unprocessed kegs were less than or equal to `min_keg_volume`.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an integer in the range 1 to 1000. If `remaining_kvass` is greater than 0, `min_keg_volume` is updated by subtracting `(remaining_kvass + n - 1) // n` from its previous value, and `i` is equal to the count of valid `volumes` processed before `remaining_kvass` becomes 0 or all iterations complete.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an integer (1 <= n <= 1000), `s` is a non-negative integer (1 <= s <= 10^12), `volumes` is a sorted list of integers, and `total_volume` is the sum of the elements in the `volumes` list. If the `total_volume` is less than `s`, the function outputs -1. Otherwise, `min_keg_volume` is updated based on `remaining_kvass`, and `i` equals the count of valid `volumes` processed before `remaining_kvass` becomes 0 or all iterations complete, followed by printing the value of `min_keg_volume`.
#Overall this is what the function does:The function accepts an integer `n` (1 <= n <= 1000), a non-negative integer `s` (1 <= s <= 10^12), and a list of `n` integer volumes (1 <= volume_i <= 10^9). It calculates the total volume of the kegs and checks if it is less than `s`. If the total volume is less than `s`, it outputs -1, indicating insufficient kvass. If the total volume is sufficient, it determines the minimum volume of kvass that can be retained from the kegs after taking enough to satisfy `s` and prints this adjusted minimum volume. If too much kvass was required, it adjusts the minimum by subtracting an average amount based on the remaining kvass divided by `n`. The function does not return any values but prints relevant outputs based on the calculations.

