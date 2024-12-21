#State of the program right berfore the function call: n is an integer in the range 1 to 1000, s is a non-negative integer in the range 1 to 10^12, and v is a list of n integers where each integer is in the range 1 to 10^9.
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
            
        #State of the program after the  for loop has been executed: `remaining_kvass` is 0, `total_volume` remains greater than or equal to `s`, `n` is an integer in the range 1 to 1000, `i` is less than or equal to `n`, `volumes` contains the utilized volumes based on the condition of the loop.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *If `remaining_kvass` is greater than 0, then `min_keg_volume` is decreased by `(remaining_kvass + n - 1) // n`. The conditions `total_volume` is greater than or equal to `s`, `n` is an integer in the range 1 to 1000, `i` is less than or equal to `n`, and `volumes` contains the utilized volumes based on the condition of the loop remain satisfied.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an integer in the range 1 to 1000, `s` is a non-negative integer in the range 1 to 10^12, `v` is a list of `n` integers in the range 1 to 10^9, `volumes` is a sorted list of `n` integers, `total_volume` is the sum of elements in `volumes`. If `total_volume` is less than `s`, the output is -1. Otherwise, if `remaining_kvass` is greater than 0, `min_keg_volume` is decreased by `(remaining_kvass + n - 1) // n`, and the value of `min_keg_volume` is printed, ensuring that `total_volume` is greater than or equal to `s`, `n` remains in the range 1 to 1000, `i` is less than or equal to `n`, and `volumes` contains the utilized volumes based on the condition of the loop.
#Overall this is what the function does:The function takes no parameters and reads two integers, `n` and `s`, followed by a list of `n` integers representing volumes. It calculates the total volume of the kegs. If the total volume is less than `s`, it prints `-1`. If the total volume is sufficient, it attempts to reduce the volume of the smallest keg (the minimum keg volume) by distributing the excess needed volume (`remaining_kvass`) across the other kegs. The final printed result is either the adjusted minimum keg volume or remains unchanged if no adjustment was necessary. The function ensures that after execution, the total volume remains sufficient to meet or exceed `s`, while also considering the possible adjustments based on the remaining kvass volume. The function does not have an explicit return value but produces output based on conditions within the code.

