#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, s is a positive integer such that 1 <= s <= 10^12, and v is a list of integers where each integer v_i (1 <= v_i <= 10^9) represents the volume of the i-th keg.
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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer in the range [1, 1000]; `s` is a positive integer in the range [1, 10^12]; `v` is a list of integers representing the keg volumes; `volumes` is a sorted list of integers in ascending order; `total_volume` is the sum of `volumes` and is greater than or equal to `s`; `min_keg_volume` is equal to `volumes[0]`; `remaining_kvass` is the remaining amount of kvass that was not taken from the kegs; `i` is equal to the number of iterations completed, which can be at most `n`. After all iterations, if `remaining_kvass` is greater than 0, it indicates that not enough kvass was collected from the available kegs. If `remaining_kvass` is 0, it indicates that the total amount of kvass needed has been collected.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: Postcondition: ***`n` is a positive integer in the range [1, 1000]; `s` is a positive integer in the range [1, 10^12]; `v` is a list of integers representing the keg volumes; `volumes` is a sorted list of integers in ascending order; `total_volume` is the sum of `volumes` and is greater than or equal to `s`; if `remaining_kvass` is greater than 0, then `min_keg_volume` is less than its previous value, indicating that not enough kvass was collected from the available kegs, and `i` is equal to the number of iterations completed, which can be at most `n`.*
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is a positive integer equal to the input value in the range [1, 1000]; `s` is a positive integer equal to the input value in the range [1, 10^12]; `v` is a list of integers representing the keg volumes; `volumes` is a sorted list of integers in ascending order; `total_volume` is the sum of `volumes`. If `total_volume` is less than `s`, -1 is printed. Otherwise, if `total_volume` is greater than or equal to `s`, and if `remaining_kvass` is greater than 0, then `min_keg_volume` is less than its previous value, indicating that not enough kvass was collected from the available kegs; `i` is equal to the number of iterations completed, which can be at most `n`, and the value of `min_keg_volume` is printed.
#Overall this is what the function does:The function accepts two positive integers `n` (the number of kegs) and `s` (the target amount of kvass), followed by a list `v` of positive integers representing the volumes of the kegs. It checks the total volume of the kegs; if the total is less than `s`, it prints `-1`. If sufficient kvass is available, it calculates the minimum keg volume that can be maintained after attempting to collect `s` amount of kvass from the kegs. If it cannot meet the `s` requirement, it adjusts the minimum keg volume accordingly and prints that value. If all the kvass is collected successfully, it prints the original minimum keg volume. The function handles edge cases where the total volume is less than `s` and when the remaining kvass is greater than zero after processing all kegs.

