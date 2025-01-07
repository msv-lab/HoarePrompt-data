#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000), s is a positive integer (1 <= s <= 10^12), and v is a list of n positive integers (1 <= v[i] <= 10^9) representing the volume of kvass in each keg.
def func():
    n, s = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort()
    low, high = 0, min(v)
    while low < high:
        mid = (low + high + 1) // 2
        
        total = sum(min(mid, x) for x in v)
        
        if total < s:
            low = mid
        else:
            high = mid - 1
        
    #State of the program after the loop has been executed: `low` is equal to `high`, `high` is equal to `min(v)`, and `total` is the sum of `min(low, x)` for each `x` in `v` such that this sum is the last computed total before the loop exited. If the loop has executed at least once, then the original value of `high` was greater than `low` and the final value of `low` is the last `mid` calculated where the sum was less than `s`. If `total` was always greater than or equal to `s`, `high` would have been adjusted downwards accordingly. The loop will terminate with `low` and `high` converging to a single point.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` is equal to `high`, and `high` is equal to `min(v)`. If the sum of `min(low, x)` for each `x` in `v` is not equal to `s`, then the current value of `low` is the last `mid` calculated where the sum was less than `s`, and `-1` is printed. Otherwise, if the sum equals `s`, then the output is `low`. The loop will terminate with `low` and `high` converging to a single point.
#Overall this is what the function does:The function accepts two positive integers `n` and `s`, and a list `v` of `n` positive integers representing the volume of kvass in each keg. It determines the maximum volume of kvass that can be uniformly distributed from the kegs such that the total volume is exactly equal to `s`. If it is not possible to achieve exactly `s`, the function prints `-1`. If it is possible, it prints the maximum uniform volume.

