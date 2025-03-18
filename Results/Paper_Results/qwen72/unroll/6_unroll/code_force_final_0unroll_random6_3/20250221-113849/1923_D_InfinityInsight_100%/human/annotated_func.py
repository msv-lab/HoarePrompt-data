#State of the program right berfore the function call: a is a list of integers, and x is an integer such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1.
    #State: a is a list of integers, and x is an integer such that 1 <= x <= 10^9, and x is not less than 0.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index `inx` of the element `x` in the list `a` plus 1.
    #State: *`a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, `inx` is the result of `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which is the index returned by the function `bl(a, x)`, where `a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, and `a[inx]` is not equal to `x`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x` (1 <= x <= 10^9). It returns -1 if `x` is less than 0. If `x` is found in the list `a`, it returns the index of the first occurrence of `x` plus 1. If `x` is not found in `a`, it returns the index `inx` returned by the function `bl(a, x)`, where `a[inx]` is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers where 1 <= a[i] <= 10^9, and n is a non-negative integer such that 1 <= n <= 3 * 10^5.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: `a` remains unchanged, `n` remains unchanged, `left` remains a list containing the integer 0, `last` is a list of length `n` where each element is the index of the last occurrence of the value `a[i]` before a different value appears, `ans` remains a list of length `n` where each element is -1.
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` remains unchanged, `n` remains unchanged, `left` is a list where each element is the cumulative sum of the elements in `a` up to the current index, `last` remains a list of length `n` where each element is the index of the last occurrence of the value `a[i]` before a different value appears, `ans` remains a list of length `n` where each element is -1.
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
        
    #State: `a` remains unchanged, `n` remains unchanged, `left` remains unchanged, `last` remains unchanged, `ans` is updated such that for each `i` where `a[i] < a[i - 1]`, `ans[i]` is 1, and for each `i` where `a[i] >= a[i - 1]`, `ans[i]` is `i + 1 - inx` where `inx` is the minimum of `func_1(left, x)` and `last[i - 1]`, and `inx` is non-negative.
    return ans
    #The program returns the list `ans` which is updated based on the conditions: for each index `i` where `a[i] < a[i - 1]`, `ans[i]` is set to 1; for each index `i` where `a[i] >= a[i - 1]`, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of `func_1(left, x)` and `last[i - 1]`, and `inx` is non-negative.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and a non-negative integer `n`. It returns a list `ans` of the same length as `a`, where each element `ans[i]` is determined as follows: If `a[i]` is less than `a[i - 1]`, then `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of the index returned by `func_1(left, x)` and the last occurrence index of `a[i - 1]` before a different value appears in `a`. If `inx` is negative, `ans[i]` remains -1. The function does not modify the input list `a` or the integer `n`.

