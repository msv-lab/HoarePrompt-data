#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, s is a non-negative integer such that 1 <= s <= 10^12, and v is a list of n integers where each integer v_i satisfies 1 <= v_i <= 10^9.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer (1 <= n <= 1000), `s` is a non-negative integer (1 <= s <= 10^12), `volumes` is a sorted list of `n` integers (1 <= v_i <= 10^9), `total_volume` is equal to `sum(volumes)` and is greater than or equal to `s`, `min_keg_volume` is equal to `volumes[0]`, `remaining_kvass` is equal to 0 if enough volumes were available, or greater than 0 if not all kvass could be taken, `i` is equal to `n` after the loop execution.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an integer (1 <= n <= 1000), `s` is a non-negative integer (1 <= s <= 10^12), `volumes` is a sorted list of `n` integers (1 <= v_i <= 10^9), `total_volume` is equal to `sum(volumes)` and is greater than or equal to `s`, `min_keg_volume` is updated to `min_keg_volume - (remaining_kvass + n - 1) // n` if `remaining_kvass` is greater than 0, `remaining_kvass` is greater than 0, and `i` is equal to `n`. If `remaining_kvass` is 0 or less, then `min_keg_volume` remains unchanged, `remaining_kvass` remains unchanged, and `i` is equal to `n`.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an integer (1 <= n <= 1000), `s` is a non-negative integer (1 <= s <= 10^12), `volumes` is a sorted list of `n` integers (1 <= v_i <= 10^9), and `total_volume` is equal to `sum(volumes)`. If `total_volume` is less than `s`, value `-1` has been printed. Otherwise, `total_volume` is greater than or equal to `s`, `min_keg_volume` is unchanged, `remaining_kvass` is unchanged, and `i` is equal to `n`.
#Overall this is what the function does:The function accepts two integers, `n` (1 <= n <= 1000) and `s` (1 <= s <= 10^12), followed by a list of `n` integers (1 <= v_i <= 10^9). It calculates the total volume of the list. If the total volume is less than `s`, it outputs `-1`. If the total volume is sufficient, it determines the minimum possible volume of the smallest keg after allocating kvass from the larger kegs to meet the required `s` and prints that minimum volume. If not enough kvass can be taken from the larger kegs to meet `s`, it adjusts the minimum keg volume accordingly.

