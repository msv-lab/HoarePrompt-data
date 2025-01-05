#State of the program right berfore the function call: n is an integer with 1 ≤ n ≤ 100, t is an integer with 1 ≤ t ≤ 10^6, and a is a list of n integers where each integer ai satisfies 0 ≤ ai ≤ 86400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is updated to the final value after subtracting the total of all `86400 - int(a[j])` for j from 0 to `i-1` where `i` is the number of elements processed, `i` is the count of elements in `a` that were processed, and `n` is an integer with 1 ≤ `n` ≤ 100.
    print(i)
#Overall this is what the function does:The function reads two integers, `n` and `t`, and a list of `n` integers representing values `a[i]`. It then calculates how many elements from the list can be processed before the value of `t` becomes non-positive by repeatedly subtracting `86400 - a[i]` from `t`. The function returns the count of processed elements (stored in `i`), which is printed as output. If `t` is reduced to zero or below before processing all elements in `a`, the function will stop processing further elements and return the count of those processed so far. The function does not handle cases where `t` is initially too small to allow for any processing, nor does it specify behavior for cases where `a` contains invalid values.

