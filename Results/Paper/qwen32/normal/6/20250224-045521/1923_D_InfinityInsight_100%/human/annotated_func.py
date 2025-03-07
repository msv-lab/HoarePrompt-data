#State of the program right berfore the function call: a is a list of integers, and x is an integer.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of integers, and x is an integer. x is greater than or equal to 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns `inx + 1`, where `inx` is the index of the integer `x` in the list `a`.
    #State: `a` is a list of integers, `x` is an integer greater than or equal to 0, `inx` holds the result of `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which holds the result of `bl(a, x)`. Given that `a[inx]` is not equal to `x`, `inx` is an index in the list `a` that does not point to the value `x`.
#Overall this is what the function does:The function accepts a list of integers `a` and an integer `x`. It returns `-1` if `x` is less than 0. If `x` is found in the list `a`, it returns the index of `x` in the list plus one. Otherwise, it returns an index from the list `a` where the value is not equal to `x`, as determined by the function `bl(a, x)`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and n is an integer representing the number of slimes such that n = len(a) and 1 <= n <= 3 * 10^5. Each element in a satisfies 1 <= a_i <= 10^9.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is an integer representing the number of slimes such that `n = len(a)`, `left` is a list containing a single element `0`, `ans` is a list of `-1` repeated `n` times, and `last` is a list of length `n` where each element after the first is either the index `i` where a change was observed or the last index where a change was observed.
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is the length of `a`, `left` is a list of cumulative sums starting with `0` and ending with the sum of all elements in `a`, `ans` is a list of `-1` repeated `n` times, and `last` is a list of length `n` where each element after the first is either the index `i` where a change was observed or the last index where a change was observed.
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
        
    #State: `a` is a list of integers representing the sizes of slimes, `n` is the length of `a`, `left` is a list of cumulative sums starting with `0` and ending with the sum of all elements in `a`, `ans` is a list where each element at index `i` (for `i` from `1` to `n-1`) is either `1` if `a[i] < a[i-1]` or `i + 1 - inx` where `inx` is determined by `func_1(left, x)` and `last[i-1]`, and `last` is a list where each element after the first is either the index `i` where a change was observed or the last index where a change was observed.
    return ans
    #The program returns the list `ans` where each element at index `i` (for `i` from `1` to `n-1`) is either `1` if `a[i] < a[i-1]` or `i + 1 - inx` where `inx` is determined by `func_1(left, x)` and `last[i-1]`.
#Overall this is what the function does:The function `func_2` takes a list `a` of integers representing the sizes of slimes and an integer `n` representing the number of slimes. It returns a list `ans` where each element at index `i` (for `i` from `1` to `n-1`) is `1` if the size of the slime at index `i` is less than the size of the slime at index `i-1`, or `i + 1 - inx` where `inx` is determined by a helper function `func_1` and the last index where a change in slime size was observed.

