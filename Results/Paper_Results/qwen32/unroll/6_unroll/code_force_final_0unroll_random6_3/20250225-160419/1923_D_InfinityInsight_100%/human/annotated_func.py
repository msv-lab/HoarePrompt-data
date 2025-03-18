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
    #State: `a` is a list of integers, `x` is an integer greater than or equal to 0, `inx` holds the value returned by `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which is the value returned by `bl(a, x)`, and `a[inx]` is not equal to `x`
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `x`. It returns `-1` if `x` is less than 0. If `x` is found in the list `a`, it returns the index of `x` in `a` plus one. Otherwise, it returns the value returned by the function `bl(a, x)`, provided that the element at the index returned by `bl(a, x)` in `a` is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and n is an integer representing the number of slimes such that 1 <= n <= 3 * 10^5 and len(a) == n.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= 3 * 10^5 and len(a) == n, left is a list containing the integer 0, last is a list where each element at index i is the index of the last different element in a up to i, ans is a list of length n with all elements initialized to -1
    for i in a:
        left.append(left[-1] + i)
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= 3 * 10^5 and len(a) == n, left is a list containing the cumulative sums of the elements in a starting from 0, last is a list where each element at index i is the index of the last different element in a up to i, ans is a list of length n with all elements initialized to -1
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
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= 3 * 10^5 and len(a) == n, left is a list containing the cumulative sums of the elements in a starting from 0, last is a list where each element at index i is the index of the last different element in a up to i, ans is a list of length n with elements updated based on the loop conditions.
    return ans
    #The program returns the list `ans` which is a list of length `n` with elements updated based on the loop conditions.
#Overall this is what the function does:The function `func_2` takes a list `a` of integers representing the sizes of slimes and an integer `n` representing the number of slimes. It returns a list `ans` of the same length `n`, where each element is calculated based on specific conditions related to the sizes of the slimes and their cumulative sums.

