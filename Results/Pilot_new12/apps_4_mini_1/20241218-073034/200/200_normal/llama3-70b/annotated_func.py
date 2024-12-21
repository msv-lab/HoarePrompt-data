#State of the program right berfore the function call: n is a positive integer where 1 <= n <= 1000, s is a positive integer where 1 <= s <= 10^12, and v is a list of n integers where each v[i] (1 <= v[i] <= 10^9) represents the volume of kvass in the i-th keg.
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
        
    #State of the program after the loop has been executed: `low` is equal to `high`, representing the largest integer such that the sum of min(`low`, x) for each x in `v` is less than `s`. The loop will have terminated since `low` is no longer less than `high`. The values of `n` and `s` remain unchanged as the original user inputs. `total` is at least less than or equal to `s` at the last comparison, and the specific values of `total`, `low`, and `high` depend on all iterations made of the loop restrictions that were in effect during execution.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` is equal to `high`, representing the largest integer such that the sum of min(`low`, `x`) for each `x` in `v` is less than or equal to `s`; if the sum is not equal to `s`, the code prints -1. Otherwise, it prints the value of `low`, which is equal to `high`, while the values of `n` and `s` remain unchanged, and `total` is less than or equal to `s`.
#Overall this is what the function does:The function processes two integers, `n` (the number of kegs) and `s` (the total volume of kvass needed), along with a list `v` of `n` integers representing the volume of kvass in each keg. It determines the largest integer `low` such that the sum of the minimum between `low` and each keg's volume in `v` is less than or equal to `s`. If no such `low` exists where the sum equals `s`, the function outputs -1. If a valid `low` is found, the function outputs this value. The input values of `n` and `s` remain unchanged throughout the function's execution. Edge cases include situations where the total volume in `v` is less than `s` and cases where the volumes in `v` do not allow for a perfect match to `s`, in which case -1 is printed.

