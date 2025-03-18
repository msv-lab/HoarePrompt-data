#State of the program right berfore the function call: a is a list of integers, and x is an integer.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of integers, and x is an integer. x is greater than or equal to 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the value of `inx` plus 1, where `inx` is the index of the element `x` in the list `a`.
    #State: `a` is a list of integers, `x` is a non-negative integer, `inx` is the result of `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which is the result of `bl(a, x)` and is an index in the list `a` where `a[inx]` is not equal to `x`.
#Overall this is what the function does:The function accepts a list of integers `a` and an integer `x`. If `x` is negative, it returns -1. If `x` is found in the list `a`, it returns the index of `x` in the list `a` plus 1. If `x` is not found in the list `a`, it returns the result of `bl(a, x)`, which is an index in the list `a`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and n is an integer representing the number of slimes such that n = len(a) and 1 <= n <= 3 * 10^5. Each element in a satisfies 1 <= a[i] <= 10^9.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: - `a` remains unchanged as a list of integers representing the sizes of slimes.
    #- `n` remains unchanged as the length of the list `a`.
    #- `left` remains unchanged as a list with a single element `[0]`.
    #- `ans` remains unchanged as a list of integers, initially all elements are `-1`.
    #- `last` will be a list of indices where the slime sizes change, with the first element being `-1` and subsequent elements indicating the last index of a change.
    #
    #In natural language, after all iterations, the `last` list will contain `-1` as its first element, followed by indices that indicate where the slime sizes change. The `ans` list and `left` list remain unchanged from their initial states, and `a` and `n` retain their initial values.
    #
    #Output State:
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` is unchanged, `n` is unchanged, `left` is `[0, a[0], a[0] + a[1], ..., sum(a)]`, `ans` is unchanged, `last` is unchanged.
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
        
    #State: `a` is unchanged, `n` is unchanged, `left` is unchanged, `ans` is modified based on the loop conditions, `last` is unchanged.
    return ans
    #The program returns the value of `ans` which is modified based on the loop conditions.
#Overall this is what the function does:The function `func_2` takes a list `a` of integers representing the sizes of slimes and an integer `n` representing the number of slimes. It returns a list `ans` where each element at index `i` (for `i` from 1 to `n-1`) indicates a specific value based on the conditions applied to the elements of `a`. The list `a` and the integer `n` remain unchanged throughout the function's execution.

