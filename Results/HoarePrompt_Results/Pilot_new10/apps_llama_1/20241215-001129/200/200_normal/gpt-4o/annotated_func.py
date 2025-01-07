#State of the program right berfore the function call: n is a non-negative integer such that 1 <= n <= 10^3, s is a non-negative integer such that 1 <= s <= 10^12, and v_i is a list of n non-negative integers such that 1 <= v_i <= 10^9 for each i.
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
            
        #State of the program after the  for loop has been executed: `n` is an input integer, `s` is an input integer, `v_i` is a list of n non-negative integers, `volumes` is a sorted list of input integers in ascending order, `total_volume` is equal to the sum of all elements in `volumes`, `total_volume` is greater than or equal to the original value of `s`, `min_keg_volume` is equal to `volumes[0]`, `i` is `n-1` if `n` is greater than 0, `remaining_kvass` is between 0 and the original value of `s` (inclusive), depending on how much kvass was distributed.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an input integer, `s` is an input integer, `v_i` is a list of n non-negative integers, `volumes` is a sorted list of input integers in ascending order, `total_volume` equals the sum of all elements in `volumes` and is greater than or equal to `s`, `min_keg_volume` equals `volumes[0]` if `remaining_kvass` is 0, otherwise `min_keg_volume` equals `volumes[0] - (remaining_kvass + n - 1) // n`, `i` is `n-1` if `n` is greater than 0, and `remaining_kvass` is between 0 and the original value of `s` (inclusive).
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: `n` is an input integer, `s` is an input integer, `v_i` is a list of n non-negative integers such that 1 <= v_i <= 10^9 for each i, `volumes` is a sorted list of input integers in ascending order, and `total_volume` is equal to the sum of all elements in `volumes`. If `total_volume` is less than `s`, then -1 has been printed. Otherwise, `min_keg_volume` equals `volumes[0]` if `remaining_kvass` is 0, otherwise `min_keg_volume` equals `volumes[0] - (remaining_kvass + n - 1) // n`, `i` is `n-1` if `n` is greater than 0, `remaining_kvass` is between 0 and the original value of `s` (inclusive), and `min_keg_volume` has been printed.
#Overall this is what the function does:The function accepts parameters n and s, and a list v_i, calculates the total volume of all kegs, and if the total volume is less than s, prints -1; otherwise, it calculates the minimum keg volume that can be used to fill n kegs with a total volume of at least s, considering the case where there is remaining kvass after filling all kegs, and prints this minimum keg volume.

