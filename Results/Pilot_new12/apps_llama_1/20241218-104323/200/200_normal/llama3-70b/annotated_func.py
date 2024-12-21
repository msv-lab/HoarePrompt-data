#State of the program right berfore the function call: n is an integer between 1 and 10^3 (inclusive), s is an integer between 1 and 10^12 (inclusive), and v_i (1 <= i <= n) are integers between 1 and 10^9 (inclusive) representing the volumes of n kegs of kvass, with the goal of pouring s liters into a glass while maximizing the remaining volume in the keg with the least kvass.
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
        
    #State of the program after the loop has been executed: `low` equals `high`, `n` is the original number of elements in `v`, `s` is the original target sum, `v` is the original list of integers, and `mid` equals `low` (or `high`), which is the largest possible value such that the sum of `min(mid, x)` for all `x` in `v` is less than `s`.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` equals `high`, `n` is the original number of elements in `v`, `s` is the original target sum, `v` is the original list of integers, and `mid` equals `low` (or `high`). If the sum of `min(low, x)` for all `x` in `v` is not equal to `s`, the function returns and prints -1. Otherwise, `low` equals `high` has been printed, and the sum of `min(low, x)` for all `x` in `v` equals `s`.
#Overall this is what the function does:The function accepts parameters n, s, and a list of volumes v_i, and attempts to find the maximum remaining volume in the keg with the least kvass after pouring s liters into a glass. It checks if it is possible to pour exactly s liters by taking a portion of the volume from each keg, and returns the maximum remaining volume in the keg with the least kvass if possible. If it is not possible to pour exactly s liters, the function returns -1. The function assumes that the input values are valid, i.e., n is an integer between 1 and 10^3 (inclusive), s is an integer between 1 and 10^12 (inclusive), and v_i (1 <= i <= n) are integers between 1 and 10^9 (inclusive). The function handles cases where the sum of the volumes of all kegs is less than or equal to s, as well as cases where the sum of the volumes of all kegs is greater than s. The function does not handle cases where the input values are invalid or where the list of volumes is empty.

