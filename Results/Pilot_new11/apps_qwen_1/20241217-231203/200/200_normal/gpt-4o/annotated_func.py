#State of the program right berfore the function call: $n$ is an integer between $1$ and $10^3$, inclusive, $s$ is an integer between $1$ and $10^{12}$, inclusive, and $v_i$ is an integer between $1$ and $10^9$, inclusive for each $i$ where $1 \le i \le n$.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and \(10^3\), `s` is an integer between 1 and \(10^{12}\), `volumes` is a list of `n` integers sorted in non-decreasing order, `total_volume` is the sum of all elements in `volumes`, `min_keg_volume` is equal to `volumes[0]`, `remaining_kvass` is 0, and `i` is `n`, since `remaining_kvass` equals 0, the program breaks out of the loop after processing all elements in `volumes`.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is an integer between 1 and \(10^3\), `s` is an integer between 1 and \(10^{12}\), `volumes` is a list of `n` integers sorted in non-decreasing order, `total_volume` is the sum of all elements in `volumes`, `min_keg_volume` is equal to `volumes[0] - ((remaining_kvass + n - 1) // n)` if `remaining_kvass > 0`. If `remaining_kvass` is not greater than 0, the values of `min_keg_volume`, `remaining_kvass`, and `i` remain unchanged as they were before the if-else block.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and \(10^3\); `s` is an integer between 1 and \(10^{12}\); `volumes` is a list of `n` integers sorted in non-decreasing order; `total_volume` is the sum of all elements in `volumes`. If `total_volume` is less than `s`, -1 is printed to the console. Otherwise, `total_volume` is greater than or equal to `s`, and `min_keg_volume` is calculated as `volumes[0] - ((remaining_kvass + n - 1) // n)` if `remaining_kvass > 0`, otherwise `min_keg_volume` remains unchanged.
#Overall this is what the function does:The function reads two integers \( n \) and \( s \) from standard input, followed by a list of \( n \) integers representing the volumes \( v_i \). It then sorts the volumes in non-decreasing order. The function calculates the minimum keg volume required to hold at least \( s \) units of kvass, considering the available volumes. If the total volume is less than \( s \), it prints \(-1\). Otherwise, it adjusts the minimum keg volume based on the remaining kvass that cannot be accommodated by the current volumes and prints the adjusted minimum keg volume. Potential edge cases include when the total volume is exactly \( s \) or when the remaining kvass cannot be evenly distributed among the kegs.

