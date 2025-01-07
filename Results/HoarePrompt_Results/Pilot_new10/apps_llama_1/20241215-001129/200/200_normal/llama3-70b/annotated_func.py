#State of the program right berfore the function call: n is a positive integer, s is a positive integer, and there is a list of n integers v where each v_i is a positive integer and 1 <= n <= 10^3, 1 <= s <= 10^12, and 1 <= v_i <= 10^9.
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
        
    #State of the program after the loop has been executed: `n` is unchanged, `s` is unchanged, `v` is unchanged, `low` and `high` have converged such that `low` is the minimum value where the sum of the minimum between `low` and each element in `v` is greater than or equal to `s`, or the closest value to this condition without exceeding `s` if such an exact value does not exist, with `low` being equal to or one more than `high` at termination.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`n` is unchanged, `s` is unchanged, `v` is unchanged, `low` and `high` have converged such that `low` is the minimum value where the sum of the minimum between `low` and each element in `v` is greater than or equal to `s`, or the closest value to this condition without exceeding `s` if such an exact value does not exist, with `low` being equal to or one more than `high` at termination. If the sum of the minimum between `low` and each element in `v` is equal to `s`, then `low` has been returned and printed at the output. Otherwise, -1 has been printed because the sum of the minimum between `low` and each element in `v` is not equal to `s`.
#Overall this is what the function does:The function finds the minimum value such that the sum of the minimum between this value and each element in the input list is greater than or equal to the target sum, and prints this value if the sum is equal to the target sum, or prints -1 otherwise, handling edge cases where the input list is empty, the target sum is less than the sum of the minimum values of the list, or the target sum is greater than the sum of all elements in the list

