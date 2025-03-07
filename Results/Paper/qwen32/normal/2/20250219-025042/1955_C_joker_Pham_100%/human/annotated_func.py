#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case n is an integer such that 1 ≤ n ≤ 2 · 10^5, k is an integer such that 1 ≤ k ≤ 10^15, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 · 10^5.
def func_1(n, k, a):
    l, r = 0, n - 1
    sunks = 0
    while l <= r:
        if k == 0:
            break
        
        if l == r:
            if k >= a[r]:
                sunks += 1
                break
            break
        
        if a[l] <= a[r]:
            if k >= a[l] * 2:
                k -= a[l] * 2
                a[r] -= a[l]
                if a[r] == 0:
                    sunks += 1
                    r -= 1
                sunks += 1
                l += 1
                continue
            elif a[l] * 2 - 1 == k:
                sunks += 1
                break
            else:
                break
        
        if k == 0:
            break
        
        if a[r] < a[l]:
            if k >= a[r] * 2:
                k -= a[r] * 2
                a[l] -= a[r]
                if a[l] == 0:
                    sunks += 1
                    l += 1
                sunks += 1
                r -= 1
                continue
            elif a[r] * 2 == k:
                sunks += 1
                break
            else:
                break
        
    #State: `t` is unchanged, `n` is unchanged, `k` is reduced to the smallest non-negative value possible, `a` is modified based on operations, `l` is incremented until it exceeds `r`, `r` is decremented until it is less than `l`, `sunks` counts the total number of successful operations.
    return sunks
    #The program returns the total number of successful operations, which is stored in the variable `sunks`.
#Overall this is what the function does:The function `func_1` takes an integer `n`, a large integer `k`, and a list `a` of `n` integers. It performs operations to reduce `k` by subtracting twice the smallest element in the list or a combination of elements, while also modifying the list `a`. The function returns the total count of successful operations performed.

