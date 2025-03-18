#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and x is an integer representing a size to be searched for in the list a. x can be any integer, but the function specifically handles the case where x is less than 0 by returning -1.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of integers representing the sizes of slimes, and x is an integer representing a size to be searched for in the list a. x is greater than or equal to 0.
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index of the first occurrence of `x` in the list `a` plus 1.
    #State: `a` is a list of integers representing the sizes of slimes, `x` is an integer representing a size to be searched for in the list `a` and `x` is greater than or equal to 0; `inx` is `bl(a, x)`. The element at index `inx` in the list `a` is not equal to `x`.
    return inx
    #The program returns `inx`, which is the result of `bl(a, x)`. The element at index `inx` in the list `a` is not equal to `x`.
#Overall this is what the function does:The function accepts a list `a` of integers and an integer `x`. If `x` is less than 0, it returns -1. If `x` is found in the list `a`, it returns the index of the first occurrence of `x` in the list `a` plus 1. Otherwise, it returns the result of `bl(a, x)`, which is an index where the element is not equal to `x`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of slimes, and n is an integer representing the number of slimes such that 1 <= n <= len(a).
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= len(a), left is a list containing the integer 0, last is a list of indices where a change in slime size was first encountered, ans is a list of n integers, all set to -1.
    for i in a:
        left.append(left[-1] + i)
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= len(a), left is a list containing the prefix sums of a, last is a list of indices where a change in slime size was first encountered, ans is a list of n integers, all set to -1.
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
        
    #State: a is a list of integers representing the sizes of slimes, n is an integer representing the number of slimes such that 1 <= n <= len(a), left is a list containing the prefix sums of a, last is a list of indices where a change in slime size was first encountered, ans is a list of n integers [-1, 1, 2, 1, 3].
    return ans
    #The program returns the list [-1, 1, 2, 1, 3]
#Overall this is what the function does:The function accepts a list `a` of integers representing the sizes of slimes and an integer `n` representing the number of slimes such that 1 <= n <= len(a). It returns a list `ans` of length `n` where each element is determined based on the sizes of the slimes and their relative positions. The specific values in the returned list are calculated through a series of operations involving prefix sums and indices of changes in slime sizes.

