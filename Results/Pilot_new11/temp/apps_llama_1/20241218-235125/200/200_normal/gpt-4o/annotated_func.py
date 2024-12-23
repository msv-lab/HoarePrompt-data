#State of the program right berfore the function call: n is a positive integer, s is a positive integer, and there is a list of n positive integers v_i such that 1 <= n <= 10^3, 1 <= s <= 10^12, and 1 <= v_i <= 10^9 for all i.
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
            
        #State of the program after the  for loop has been executed: `n` is an input integer, `s` is the original input integer, `volumes` is a sorted list of input integers in ascending order, `total_volume` is the sum of the integers in `volumes` and is larger than or equal to `s`, `min_keg_volume` is equal to `volumes[0]`, `i` is the last index that was processed, and `remaining_kvass` is the remaining value after the loop execution, which is either 0 or the remaining value after `n` iterations or the break condition.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an input integer, `s` is the original input integer, `volumes` is a sorted list of input integers in ascending order, `total_volume` is the sum of the integers in `volumes` and is larger than or equal to `s`. If `remaining_kvass` is greater than 0, then `min_keg_volume` is equal to `volumes[0] - (remaining_kvass + n - 1) // n`, and `i` is the last index that was processed. Otherwise, the state of the variables remains unchanged as there is no else part to modify them.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an input integer, `s` is an input integer, `volumes` is a sorted list of input integers in ascending order, and `total_volume` is the sum of the integers in `volumes`. If `total_volume` is less than `s`, the value -1 has been printed and returned. Otherwise, `total_volume` is larger than or equal to `s`, and the value of `min_keg_volume` has been calculated as `volumes[0] - (remaining_kvass + n - 1) // n` if `remaining_kvass` is greater than 0, and this value has been printed and returned, with `i` being the last index that was processed if `remaining_kvass` is greater than 0.
#Overall this is what the function does:Functionality: The function calculates the minimum possible keg volume that can hold a certain amount of kvass, given a list of kegs with different volumes. The function takes as input the number of kegs `n`, the total amount of kvass `s`, and a list of `n` positive integers representing the volumes of the kegs. It returns the minimum keg volume if the total volume of the kegs is greater than or equal to the amount of kvass, or -1 if the total volume is less than the amount of kvass. The function iterates through the sorted list of keg volumes, and for each keg, it calculates the amount of kvass that can be poured into it without overflowing. If there is still kvass remaining after filling all kegs, it reduces the minimum keg volume by the amount of remaining kvass divided by the number of kegs, rounded down to the nearest whole number. The function handles potential edge cases, such as an empty list of kegs or a total volume that is less than the amount of kvass, and returns the correct result in these cases. The state of the program after execution includes the calculated minimum keg volume, or -1 if the total volume is insufficient, and the remaining amount of kvass if not all of it can be poured into the kegs.

