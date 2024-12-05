#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 1000), s is a positive integer (1 ≤ s ≤ 10^12), and v is a list of n positive integers (1 ≤ v[i] ≤ 10^9) representing the volume of kvass in each keg.
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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 1000), `s` is a positive integer (1 ≤ s ≤ 10^12), `v` is updated to the list of integers input by the user, `volumes` is a sorted list of integers from that input, `total_volume` is the sum of the elements in `volumes` and is greater than or equal to `s`, `min_keg_volume` is equal to `volumes[0]`, `remaining_kvass` is 0, and `i` is less than or equal to `n`.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 1000), `s` is a positive integer (1 ≤ s ≤ 10^12), `v` is updated to the list of integers input by the user, `volumes` is a sorted list of integers from that input, `total_volume` is the sum of the elements in `volumes` and is greater than or equal to `s`, `min_keg_volume` is updated to equal to `min_keg_volume - (remaining_kvass + n - 1) // n` if `remaining_kvass` is greater than 0, and `remaining_kvass` remains greater than 0, while `i` is less than or equal to `n`. If `remaining_kvass` is not greater than 0, the state of the variables remains unchanged.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 1000), `s` is a positive integer (1 ≤ s ≤ 10^12), `v` is updated to the list of integers input by the user, `volumes` is a sorted list of integers from that input, and `total_volume` is the sum of the elements in `volumes`. If `total_volume` is less than `s`, then no further changes are made to the variables. If `total_volume` is greater than or equal to `s`, then `min_keg_volume` is updated to equal `min_keg_volume - (remaining_kvass + n - 1) // n` (if `remaining_kvass` is greater than 0), `remaining_kvass` remains greater than 0 while `i` is less than or equal to `n`, and `min_keg_volume` is printed.
#Overall this is what the function does:The function accepts two positive integers `n` and `s`, and a list of `n` positive integers representing the volumes of kvass in each keg. It checks if the total volume of all kegs is less than `s`, in which case it outputs -1. If the total volume is sufficient, it calculates the maximum volume that can be left in the smallest keg after trying to fulfill the total desired volume `s` by potentially taking volume from other kegs. Finally, it prints the adjusted minimum keg volume. The function does not return any value; it only prints the result.

