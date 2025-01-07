#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, s is a positive integer such that 1 <= s <= 10^12, and v is a list of n integers where each integer v[i] satisfies 1 <= v[i] <= 10^9.
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
        
    #State of the program after the loop has been executed: `low` is equal to `high`, which is the largest value for which the sum of the minimum between that value and each `x` in `v` is less than or equal to `s`. `s` is the input positive integer, `n` is the input integer such that 1 <= `n` <= 1000, `v` is the sorted list of `n` integers, and all variables reflect their final values after all iterations of the loop. If `low` was initially less than `high`, then the loop executed based on conditions on the total in relation to `s`.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` is equal to `high`, which is the largest value for which the sum of the minimum between that value and each `x` in `v` is less than or equal to `s`. If the sum of minimum values does not equal `s`, -1 is printed. Otherwise, the value of `low` is printed, indicating that the sum of the minimum values is exactly equal to `s`.
#Overall this is what the function does:The function accepts two integers, `n` and `s`, and a list of `n` integers `v`. It sorts the list `v` and then determines the largest integer `low` such that the sum of the minimum of `low` and each element in `v` is less than or equal to `s`. If the sum of the minimums equals `s`, it outputs `low`. If the sum does not equal `s`, it prints `-1`. Additionally, it implicitly assumes that the input constraints are met, and does not handle cases where `n` is zero or lists contain invalid integers, although such cases wouldn't occur given the specified input constraints.

