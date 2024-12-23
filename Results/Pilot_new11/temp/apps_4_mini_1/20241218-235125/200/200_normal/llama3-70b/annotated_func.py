#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, s is a non-negative integer such that 1 <= s <= 10^12, and v is a list of integers representing the volume of each keg where each value v_i satisfies 1 <= v_i <= 10^9.
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
        
    #State of the program after the loop has been executed: `low` is equal to `high`, which is the largest integer `mid` such that the sum of `min(mid, x)` for each `x` in `v` is less than or equal to `s`. If the initial values of `s` and the elements in `v` allow for multiple iterations, then the final values of `low` and `high` converge to the point where no further valid `mid` can be calculated that satisfies the condition, while the value of `total` is the sum of `min(low, x)` for each `x` in `v`. Any adjustments to `low` and `high` during the loop have ensured that `low` is now equal to `high` without exceeding the limits defined by the relationships to `s` and `v`.`
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` is equal to `high`, which is the largest integer `mid` such that the sum of `min(mid, x)` for each `x` in `v` is less than or equal to `s`. If the sum of `min(low, x)` for each `x` in `v` does not equal `s`, -1 is printed. Otherwise, if the sum is equal to `s`, the value of `low` has been printed.
#Overall this is what the function does:The function accepts an integer `n` representing the number of kegs, a non-negative integer `s` representing a target sum, and a list of integers `v` representing the volumes of each keg. It calculates the largest integer `mid` (referred to as `low` in the final state) such that the total sum of the minimum between `mid` and each keg volume does not exceed `s`. If this total equals `s`, it prints the value of `low`. If the total does not equal `s`, it prints -1. It effectively performs a binary search to find this value while handling edge cases, such as potentially returning -1 when it is not possible to achieve the exact total sum `s` through the available keg volumes. The function ensures that `low` equals `high` after the binary search concludes, positioned at the largest possible keg volume allowed under the sum constraint. The overall outcome is based strictly on the relationship between the keg volumes and the target sum, confirming whether the desired total is achievable.

