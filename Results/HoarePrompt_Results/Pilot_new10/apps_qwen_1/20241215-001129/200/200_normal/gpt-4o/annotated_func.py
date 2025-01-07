#State of the program right berfore the function call: $n$ is an integer such that $1 \le n \le 10^3$, $s$ is an integer such that $1 \le s \le 10^{12}$, and $v_i$ is an integer such that $1 \le v_i \le 10^9$ for all $i$ in the range $1 \le i \le n$.
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
            
        #State of the program after the  for loop has been executed: `n` must be greater than 0, `s` is an integer such that \(1 \le s \le 10^{12}\), `volumes` is a list of integers such that \(1 \le v_i \le 10^9\) for all \(i\) in the range \(1 \le i \le n\) and `volumes` is sorted in ascending order; `total_volume` is the sum of the elements in the `volumes` list and is greater than or equal to `s`; `min_keg_volume` is the first element in the `volumes` list; `i` is the index of the first volume in `volumes` that is greater than `min_keg_volume`, or `n` if no such volume exists; `remaining_kvass` is 0 if all the required kvass was taken or the remaining amount of kvass needed if not.
        if (remaining_kvass > 0) :
            min_keg_volume -= (remaining_kvass + n - 1) // n
        #State of the program after the if block has been executed: *`n` is greater than 0, `s` is an integer such that \(1 \le s \le 10^{12}\), `volumes` is a list of integers such that \(1 \le v_i \le 10^9\) for all \(i\) in the range \(1 \le i \le n\) and `volumes` is sorted in ascending order; `total_volume` is the sum of the elements in the `volumes` list and is greater than or equal to `s`; `min_keg_volume` is decreased by \(\left(\frac{remaining\_kvass + n - 1}{n}\right)\); `i` is the index of the first volume in `volumes` that is greater than `min_keg_volume`, or `n` if no such volume exists; `remaining_kvass` is either 0 (if all required kvass has been taken) or reduced according to the specified formula if kvass still needs to be taken.
        print(min_keg_volume)
    #State of the program after the if-else block has been executed: `n` is an integer such that \(1 \le n \le 10^3\), `s` is an integer such that \(1 \le s \le 10^{12}\), `volumes` is a list of integers such that \(1 \le v_i \le 10^9\) for all \(i\) in the range \(1 \le i \le n\) and `volumes` is sorted in ascending order; `total_volume` is the sum of the elements in the `volumes` list. If `total_volume` is less than `s`, -1 is printed. Otherwise, `min_keg_volume` is decreased by \(\left(\frac{remaining\_kvass + n - 1}{n}\right)\), `i` is the index of the first volume in `volumes` that is greater than `min_keg_volume`, or `n` if no such volume exists, `remaining_kvass` is either 0 or reduced accordingly, and `min_keg_volume` is printed.
#Overall this is what the function does:The function accepts two integers `n` and `s`, and a list of integers `volumes` where `1 ≤ n ≤ 10^3`, `1 ≤ s ≤ 10^12`, and `1 ≤ v_i ≤ 10^9` for all `i` in the range `1 ≤ i ≤ n`. The function first sorts the `volumes` list and calculates the total volume. If the total volume is less than `s`, it prints `-1`. Otherwise, it iterates through the sorted `volumes` list to find the minimum keg volume that can satisfy the required `s` amount of kvass, considering the remaining kvass needed. If there is still some kvass required after the iteration, it adjusts the `min_keg_volume` by reducing it proportionally. Finally, it prints the adjusted `min_keg_volume`.

