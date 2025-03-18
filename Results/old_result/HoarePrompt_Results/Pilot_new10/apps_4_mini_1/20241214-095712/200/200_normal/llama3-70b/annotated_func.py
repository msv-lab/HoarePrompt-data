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
        
    #State of the program after the loop has been executed: `low` is equal to `high`, and both are less than the initial value of `min(v)`, while the final `total` value is the sum of `min(mid, x)` for each `x` in `v`, which does not exceed `s`.
    if (sum(min(low, x) for x in v) != s) :
        print(-1)
    else :
        print(low)
    #State of the program after the if-else block has been executed: *`low` is equal to `high`, and both are less than the initial value of `min(v)`. If the sum of the minimum of `low` and each element `x` in `v` is not equal to `s`, the output will be -1. Otherwise, the printed output will be the current value of `low`.
#Overall this is what the function does:The function accepts a positive integer `n`, a positive integer `s`, and a list `v` of `n` positive integers. It determines the largest volume that can be uniformly distributed among the kegs such that the total volume does not exceed `s`. If the exact total of `s` cannot be achieved with the kegs' volumes, it returns -1. If achieved, it returns the maximum possible volume `low` that still meets this constraint.

