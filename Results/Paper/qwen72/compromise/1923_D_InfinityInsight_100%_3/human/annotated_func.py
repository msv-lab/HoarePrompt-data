#State of the program right berfore the function call: a is a list of integers, and x is an integer such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1.
    #State: *a is a list of integers, and x is an integer such that 1 <= x <= 10^9. Additionally, x is not less than 0.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index `inx` where the element in list `a` is equal to `x`, plus 1.
    #State: *`a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, `inx` is the result of `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns the index `inx` which is the result of `bl(a, x)`, where `a[inx]` is not equal to `x` and `1 <= x <= 10^9`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x` (where `1 <= x <= 10^9`). It returns -1 if `x` is less than 0. If `x` is found in the list `a`, it returns the index of `x` plus 1. If `x` is not found in `a` but is within the valid range, it returns the index `inx` which is the result of `bl(a, x)`, where `a[inx]` is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers where 1 <= a[i] <= 10^9, and n is a positive integer such that 1 <= n <= 3 * 10^5.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: `i` is `n-1`, `last` is a list of length `n` where each element is the index of the last occurrence of the corresponding element in `a` up to that index, and `ans` remains a list of length `n` with all elements set to -1.
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` must be a non-empty list, `i` is the last element in `a`, `last` is a list of length `n` where each element is the index of the last occurrence of the corresponding element in `a` up to that index, `ans` remains a list of length `n` with all elements set to -1, `left` is a list with `len(a) + 1` elements, where each element is the cumulative sum of the elements in `a` up to the corresponding index.
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
        
    #State: `a` is a non-empty list, `i` is the last element in `a`, `last` is a list of length `n` where each element is the index of the last occurrence of the corresponding element in `a` up to that index, `ans` is a list of length `n` with elements set to `i + 1 - inx` for each index `i` where the loop condition `a[i] < a[i - 1]` is not met and `inx2 < inx`, otherwise elements remain -1, `left` is a list with `len(a) + 1` elements, where each element is the cumulative sum of the elements in `a` up to the corresponding index, `n` is the length of the list `a`.
    return ans
    #The program returns the list `ans` of length `n` where each element is set to `i + 1 - inx` for each index `i` where the loop condition `a[i] < a[i - 1]` is not met and `inx2 < inx`, otherwise elements remain -1.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and a positive integer `n`. It returns a list `ans` of length `n` where each element is either -1 or a value calculated based on the conditions within the function. Specifically, for each index `i` in the list `a` (starting from 1 to `n-1`), if `a[i]` is not less than `a[i-1]` and the index of the last occurrence of `a[i-1]` (stored in `last`) is less than the index found by a function `func_1` applied to the cumulative sum list `left` and a calculated value `x`, then `ans[i]` is set to `i + 1 - inx`. Otherwise, `ans[i]` remains -1.

