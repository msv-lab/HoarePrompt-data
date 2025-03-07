#State of the program right berfore the function call: a is a list of integers, and x is an integer such that x < len(a).
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of integers, and x is an integer such that x < len(a) and x is not less than 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns `inx + 1`, where `inx` is the index of the integer `x` in the list `a`.
    #State: `a` is a list of integers, `x` is an integer such that `x < len(a)` and `x` is not less than 0, `inx` is the value returned by `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which is the value returned by `bl(a, x)` and `a[inx]` is not equal to `x`
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x`. It returns -1 if `x` is less than 0. If `x` is a valid index in the list `a` and the element at index `x` is equal to `x`, it returns `inx + 1`, where `inx` is the index of `x` in `a`. Otherwise, it returns `inx`, which is the value returned by `bl(a, x)`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and n is an integer representing the number of slimes such that n == len(a) and n >= 1.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is an integer representing the number of slimes such that `n == len(a)` and `n >= 1`; `left` is a list containing the single element `0`; `ans` is a list of `n` elements, all initialized to `-1`; `last` is a list where the first element is `-1` and each subsequent element is either the index `i` where `a[i]` is different from `a[i-1]` or the last index of a change if `a[i]` is the same as `a[i-1]`.
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is the length of `a`, `left` is a list of cumulative sums starting with `0`, `ans` is a list of `n` elements all initialized to `-1`, and `last` is unchanged.
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
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is the length of `a`, `left` is a list of cumulative sums starting with `0`, `last` is unchanged, and `ans` is a list of `n` elements where each element is either `1` if `a[i] < a[i - 1]`, or `i + 1 - inx` where `inx` is determined by the conditions in the loop.
    return ans
    #The program returns a list `ans` of `n` elements where each element is either `1` if `a[i] < a[i - 1]`, or `i + 1 - inx` where `inx` is determined by the conditions in the loop.
#Overall this is what the function does:The function accepts a list `a` of integers representing the sizes of slimes and an integer `n` representing the number of slimes such that `n` equals the length of `a` and is at least 1. It returns a list `ans` of `n` elements where each element is `1` if the size of the current slime is less than the size of the previous slime, or `i + 1 - inx` where `inx` is determined by the conditions within the loop.

