#State of the program right berfore the function call: a is a list of positive integers representing the sizes of the slimes, and x is a non-negative integer representing a target size.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of positive integers representing the sizes of the slimes, and x is a non-negative integer representing a target size, and x is greater than or equal to 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns inx + 1, where inx is the index of the first slime in the list `a` that is greater than or equal to `x`
    #State: `a` is a list of positive integers representing the sizes of the slimes, `x` is a non-negative integer representing a target size, and `inx` is the index of the first slime in the list `a` that is greater than or equal to `x`. The first slime in the list at index `inx` is greater than `x`.
    return inx
    #The program returns the index of the first slime in the list `a` that is greater than or equal to `x`
#Overall this is what the function does:The function accepts a list of positive integers `a` and a non-negative integer `x`. It searches for the smallest index of a slime in the list `a` that is greater than or equal to `x`. If such a slime exists, it returns either the index of the first slime that meets the condition (Case_3) or `inx + 1` where `inx` is the index of the first slime that meets the condition (Case_2). If no slime in the list meets the condition, it returns -1 (Case_1).

#State of the program right berfore the function call: a is a list of n integers representing the sizes of the slimes, and n is a positive integer such that 1 <= n <= 3 * 10^5. Each integer in the list a is between 1 and 10^9 inclusive.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: Output State: `left` is a list containing 0; `last` is a list where each element is the index of the last occurrence of the respective element in the array `a`; `ans` is a list of length `n` containing -1.
    #
    #To explain further, the `last` list keeps track of the most recent index at which each value in the array `a` appears. The `left` list remains unchanged as it only contains the initial value of 0. The `ans` list is not affected by the loop and retains its initial state of all elements being -1.
    for i in a:
        left.append(left[-1] + i)
        
    #State: Output State: `left` is a list containing the cumulative sum of all elements in `a` from the first element to the last; `last` is a list where each element is the index of the last occurrence of the respective element in the array `a`; `ans` is a list of length `n` containing -1.
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
        
    #State: Output State: `left` is a list containing the cumulative sum of all elements in `a` from the first element to the last; `last` is a list where each element is the index of the last occurrence of the respective element in the array `a`; `ans` is a list of length `n` where each element is calculated based on the conditions inside the loop, potentially updated to `i + 1 - inx` if certain conditions are met during each iteration.
    return ans
    #The program returns a list `ans` of length `n`, where each element is calculated based on the conditions inside the loop, potentially updated to `i + 1 - last[a[i]]` if certain conditions are met during each iteration.
#Overall this is what the function does:The function accepts a list `a` of integers representing the sizes of slimes and an integer `n` indicating the length of the list. It returns a list `ans` of the same length `n`, where each element in `ans` is calculated based on specific conditions encountered during the iteration, potentially updating to `i + 1 - last[a[i]]` if certain conditions are met during each iteration. The function constructs two auxiliary lists `left` and `last` to keep track of cumulative sums and the last occurrence indices, respectively, and uses these to determine the values in the output list `ans`.

