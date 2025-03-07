#State of the program right berfore the function call: a is a list of integers, and x is an integer such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1.
    #State: a is a list of integers, and x is an integer such that 1 <= x <= 10^9. Additionally, x is not less than 0.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index `inx` of the element `x` in the list `a` plus 1.
    #State: *`a` is a list of integers, `x` is an integer such that 1 <= x <= 10^9, `inx` is the result of the function `bl(a, x)` which is assumed to return an integer, and `a[inx]` is not equal to `x`.
    return inx
    #The program returns `inx`, which is the integer result of the function `bl(a, x)`. `inx` is an index in the list `a` where `a[inx]` is not equal to `x`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x` (1 <= x <= 10^9). It returns -1 if `x` is less than 0. If `x` is found in the list `a`, it returns the index of the first occurrence of `x` plus 1. If `x` is not found in the list `a`, it returns the integer result of the function `bl(a, x)`, which is an index in the list `a` where `a[inx]` is not equal to `x`.

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
        
    #State: `a` is a list of integers where \(1 \leq \text{len}(a) \leq 3 \times 10^5\), and each element \(a_i\) satisfies \(1 \leq a_i \leq 10^9\). `n` is a non-negative integer such that \(n = \text{len}(a)\) and \(n\) must be greater than 1. `left` is a list containing a single integer 0. `last` is a list of length \(n\) where each element is the index of the last occurrence of the same value before the current index, or -1 if the value has not been seen before. `ans` is a list of length \(n\) where each element is -1. `i` is \(n - 1\).
    for i in a:
        left.append(left[-1] + i)
        
    #State: `a` is a list of integers where \(1 \leq \text{len}(a) \leq 3 \times 10^5\) and each element \(a_i\) satisfies \(1 \leq a_i \leq 10^9\), `n` is a non-negative integer such that \(n = \text{len}(a)\) and \(n\) must be greater than 1, `left` is a list containing the cumulative sums of the elements in `a` starting from 0, `last` is a list of length \(n\) where each element is the index of the last occurrence of the same value before the current index, or -1 if the value has not been seen before, `ans` is a list of length \(n\) where each element is -1, `i` is the last element in `a`.
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
        
    #State: The list `a` remains unchanged, with elements satisfying \(1 \leq a_i \leq 10^9\) and \(1 \leq \text{len}(a) \leq 3 \times 10^5\). The integer `n` is the length of `a` and must be greater than 1. The list `left` remains unchanged, containing the cumulative sums of the elements in `a` starting from 0. The list `last` remains unchanged, with each element being the index of the last occurrence of the same value before the current index, or -1 if the value has not been seen before. The list `ans` is now updated for all indices from 1 to \(n-1\). For each index `i` in the range 1 to \(n-1\), if `a[i] < a[i-1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the index found by `func_1(left, x)` and `inx2` is `last[i-1]`. If `inx2 < inx`, `inx` is updated to `inx2`. If `inx < 0`, the update is skipped. The variable `i` is the last element in the list `a`.
    return ans
    #The program returns the list `ans` which has been updated for all indices from 1 to \(n-1\) based on the conditions specified. For each index `i` in the range 1 to \(n-1\), if `a[i]` is less than `a[i-1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the index found by `func_1(left, x)` and `inx2` is `last[i-1]`. If `inx2` is less than `inx`, `inx` is updated to `inx2`. If `inx` is less than 0, the update is skipped. The final value of `ans` depends on the specific values in `a`, `left`, and `last`.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and an integer `n` representing the length of `a`. It returns a list `ans` of the same length as `a`, where each element at index `i` (from 1 to \(n-1\)) is updated based on the following conditions: If `a[i]` is less than `a[i-1]`, `ans[i]` is set to 1. Otherwise, `ans[i]` is set to `i + 1 - inx`, where `inx` is the minimum of the index found by `func_1(left, x)` and `last[i-1]`. If `inx` is less than 0, `ans[i]` remains -1. The list `a` remains unchanged, and the final state of `ans` depends on the specific values in `a`, `left`, and `last`.

