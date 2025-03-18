#State of the program right berfore the function call: a is a list of integers, and x is an integer.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of integers, and x is an integer. x is greater than or equal to 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the value of `inx` plus 1, where `inx` is the index of the integer `x` in the list `a`.
    #State: `a` is a list of integers, `x` is an integer greater than or equal to 0, `inx` holds the value returned by `bl(a, x)`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns `inx`, which holds the value returned by `bl(a, x)`. Given that `a[inx]` is not equal to `x`, `inx` represents an index in the list `a` that does not correspond to the value `x`.
#Overall this is what the function does:The function `func_1` takes a list of integers `a` and an integer `x` as input. It returns -1 if `x` is less than 0. If `x` is non-negative, it returns the index of `x` in the list `a` plus one if `x` is found in the list. If `x` is not found, it returns an index from the function `bl(a, x)`, which does not correspond to the value `x`.

#State of the program right berfore the function call: a is a list of integers representing the sizes of the slimes, and n is an integer representing the number of slimes such that n == len(a) and n >= 1.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: a is a list of integers representing the sizes of the slimes, n is an integer representing the number of slimes such that n == len(a) and n >= 1, left is a list containing a single element, 0, last is a list containing the indices of the last occurrence of a different slime size up to that point, and ans is a list of -1 repeated n times.
    for i in a:
        left.append(left[-1] + i)
        
    #State: a is a list of integers representing the sizes of the slimes, n is an integer representing the number of slimes such that n == len(a) and n >= 1, left is a list containing the cumulative sums of the elements in a starting with 0, last is a list containing the indices of the last occurrence of a different slime size up to that point, and ans is a list of -1 repeated n times.
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
        
    #State: a is a list of integers representing the sizes of the slimes, n is an integer representing the number of slimes such that n == len(a) and n >= 1, left is a list containing the cumulative sums of the elements in a starting with 0, last is a list containing the indices of the last occurrence of a different slime size up to that point, and ans is [-1, 1, 3, 2, 3].
    return ans
    #The program returns [-1, 1, 3, 2, 3]
#Overall this is what the function does:The function accepts a list of integers `a` representing the sizes of slimes and an integer `n` representing the number of slimes, where `n` is equal to the length of the list `a` and `n` is at least 1. The function returns a list `ans` of the same length as `a`, where each element in `ans` is determined based on specific conditions related to the sizes of the slimes. The return value for the provided example input is `[-1, 1, 3, 2, 3]`.

