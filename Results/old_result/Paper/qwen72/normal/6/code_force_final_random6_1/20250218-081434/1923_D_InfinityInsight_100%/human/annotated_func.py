#State of the program right berfore the function call: a is a list of integers, and x is an integer such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index `inx` of the element `x` in the list `a` plus 1.
    #State: *`a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, `inx` is the result of `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which is the result of `bl(a, x)`, and `a[inx]` is not equal to `x`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x` (1 <= x <= 10^9). It returns -1 if `x` is less than 0. If `x` is found in the list `a`, it returns the index of `x` plus 1. If `x` is not found in `a`, it returns the result of `bl(a, x)`, which is an index `inx` such that `a[inx]` is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers where 1 <= len(a) <= 3 * 10^5, and each element a_i satisfies 1 <= a_i <= 10^9. n is a non-negative integer such that n = len(a).
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: `a` is a list of integers where \(1 \leq \text{len}(a) \leq 3 \times 10^5\) and each element \(a_i\) satisfies \(1 \leq a_i \leq 10^9\), `n` is a non-negative integer such that \(n = \text{len}(a)\), `left` is a list containing the integer 0, `last` is a list of length \(n\) where the first element is -1 and subsequent elements are the indices of the last occurrence of each distinct element in `a` up to that point, `ans` is a list of length \(n\), where each element is -1, and `i` is \(n-1\).
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` is a list of integers where \(1 \leq \text{len}(a) \leq 3 \times 10^5\) and each element \(a_i\) satisfies \(1 \leq a_i \leq 10^9\), `n` is a non-negative integer such that \(n = \text{len}(a)\), `left` is a list containing the integer 0 followed by the cumulative sums of all elements in `a`, `last` is a list of length \(n\) where the first element is -1 and subsequent elements are the indices of the last occurrence of each distinct element in `a` up to that point, `ans` is a list of length \(n\), where each element is -1, and `i` has been set to each element of `a` during the loop.
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
        
    #State: The loop has completed all iterations. `i` is `n-1`, `n` remains the length of the list `a`. The elements of `ans` have been updated based on the conditions within the loop. For each index `i` in the range from 1 to `n-1`, if `a[i]` is less than `a[i-1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of `func_1(left, x)` and `last[i-1]`, and `x` is `left[i] - a[i] - 1`. If `inx` is less than 0, `ans[i]` remains unchanged. The values of `left` and `last` remain as they were initialized or updated within the loop.
    return ans
    #The program returns the list `ans` which has been updated based on the conditions within the loop. For each index `i` from 1 to `n-1` in the list `a`, if `a[i]` is less than `a[i-1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of `func_1(left, x)` and `last[i-1]`, and `x` is `left[i] - a[i] - 1`. If `inx` is less than 0, `ans[i]` remains unchanged. The length of `ans` is `n`, and `n` is the length of the list `a`.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and an integer `n` representing the length of `a`. It returns a list `ans` of the same length `n`. For each index `i` from 1 to `n-1` in the list `a`:
- If `a[i]` is less than `a[i-1]`, `ans[i]` is set to 1.
- Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of the index returned by `func_1(left, x)` and `last[i-1]`, and `x` is `left[i] - a[i] - 1`.
- If `inx` is less than 0, `ans[i]` remains unchanged.
The first element of `ans` remains -1. The function does not modify the input list `a` or the integer `n`.

