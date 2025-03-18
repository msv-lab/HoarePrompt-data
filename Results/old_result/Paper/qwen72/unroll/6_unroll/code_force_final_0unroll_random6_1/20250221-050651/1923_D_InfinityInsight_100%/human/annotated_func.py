#State of the program right berfore the function call: a is a list of integers, and x is an integer such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1.
    #State: a is a list of integers, and x is an integer such that 1 <= x <= 10^9. x is not less than 0.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index of `x` in the list `a` plus 1.
    #State: `a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, `inx` is the result of the function `bl(a, x)`, and `a[inx]` is not equal to `x`.
    return inx
    #The program returns `inx`, which is the index returned by the function `bl(a, x)` where `a[inx]` is not equal to `x`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x` (1 <= x <= 10^9). It returns -1 if `x` is less than 0. If `x` is found in the list `a`, it returns the index of `x` plus 1. If `x` is not found in `a`, it returns the index `inx` returned by the function `bl(a, x)`, where `a[inx]` is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers where 1 <= len(a) <= 3 * 10^5, and each element a_i satisfies 1 <= a_i <= 10^9. n is an integer such that 1 <= n <= len(a).
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: The list `last` will contain the indices of the last occurrence of each unique element in the list `a` up to the current index `i` for each `i` in the range `[0, n-1]`. The list `ans` will remain unchanged, with all elements set to -1.
    for i in a:
        left.append(left[-1] + i)
        
    #State: The list `left` will contain the cumulative sum of the elements in the list `a` up to each index `i` for each `i` in the range `[0, n-1]`. The list `ans` will remain unchanged, with all elements set to -1.
    for i in range(1, n):
        if a[i] < a[i - 1]:
            ans[i] = 1
            continue
        
        x = left[i] - a[i] - 1
        
        inx = func_1(left, x)
        
        inx2 = last[i - 1]
        
        if inx2 < inx:
            inx = inx2
        
        if inx < 0:
            continue
        
        ans[i] = i + 1 - inx
        
    #State: The list `left` will still contain the cumulative sum of the elements in the list `a` up to each index `i` for each `i` in the range `[0, n-1]`. The list `ans` will be updated such that for each index `i` in the range `[1, n-1]`, if `a[i] < a[i - 1]`, `ans[i]` will be set to 1. Otherwise, `ans[i]` will be set to `i + 1 - inx`, where `inx` is the result of `func_1(left, x)` and `x = left[i] - a[i] - 1`, but only if `inx` is non-negative and greater than or equal to `last[i - 1]`. If `inx` is negative or less than `last[i - 1]`, `ans[i]` will remain -1.
    return ans
    #The program returns the list `ans` which has been updated based on the conditions specified. For each index `i` in the range `[1, n-1]`, if `a[i] < a[i - 1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the result of `func_1(left, x)` with `x = left[i] - a[i] - 1`, but only if `inx` is non-negative and greater than or equal to `last[i - 1]`. If `inx` is negative or less than `last[i - 1]`, `ans[i]` remains -1.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and an integer `n`. It returns a list `ans` of the same length as `a`, where each element `ans[i]` (for `i` in the range `[1, n-1]`) is set to 1 if `a[i]` is less than `a[i - 1]`. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the result of `func_1(left, x)` with `x = left[i] - a[i] - 1`, but only if `inx` is non-negative and greater than or equal to the last occurrence index of `a[i-1]` (stored in `last[i - 1]`). If `inx` is negative or less than `last[i - 1]`, `ans[i]` remains -1. The first element of `ans` is always -1.

