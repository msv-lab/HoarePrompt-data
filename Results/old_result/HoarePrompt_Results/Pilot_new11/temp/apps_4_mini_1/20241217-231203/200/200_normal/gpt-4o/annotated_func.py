#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000), s is a non-negative integer (1 <= s <= 10^12), and v is a list of n integers where each integer v_i represents the volume of the i-th keg (1 <= v_i <= 10^9).
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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer (1 <= n <= 1000), `i` is less than `n`, `remaining_kvass` is the amount of kvass that was not taken from the available volumes; if all `remaining_kvass` was taken, it will be 0, if not it will be greater than 0. `volumes` is a sorted list of `n` integers, `total_volume` is equal to `sum(volumes)` and greater than or equal to `s`.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is a positive integer (1 <= n <= 1000) and `i` is less than `n`. If `remaining_kvass` is greater than 0, `min_keg_volume` is updated to `min_keg_volume - (remaining_kvass + n - 1) // n`. If `remaining_kvass` is 0, no changes are made. The `volumes` is a sorted list of `n` integers, and `total_volume` is equal to `sum(volumes)` and greater than or equal to `s.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 <= n <= 1000), `s` is a non-negative integer (1 <= s <= 10^12), `v` is a list of `n` integers, `volumes` is a sorted list of `n` integers, and `total_volume` is equal to `sum(volumes)`. If `total_volume` is less than `s`, -1 is printed. Otherwise, if `total_volume` is greater than or equal to `s`, `min_keg_volume` is updated by subtracting `(remaining_kvass + n - 1) // n` and `min_keg_volume` is printed.
#Overall this is what the function does:The function takes an integer `n`, an integer `s`, and a list of integers `volumes`. It checks if the total volume of the kegs is at least `s`. If it is not, the function prints `-1`. If it is, the function calculates the minimum volume that can be obtained from the kegs after attempting to reduce the `remaining_kvass` amount by taking volumes from kegs that exceed the minimum keg volume. If any `remaining_kvass` remains after processing all eligible kegs, it adjusts the minimum keg volume downwards based on the amount of remaining kvass and the number of kegs. The final result printed is either the updated minimum keg volume or, if all `remaining_kvass` was taken, the original minimum keg volume. The function directly interacts with user input and output, returning no values but printing results instead.

