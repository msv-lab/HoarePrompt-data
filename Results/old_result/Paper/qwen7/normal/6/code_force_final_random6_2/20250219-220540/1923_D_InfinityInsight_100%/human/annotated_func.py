#State of the program right berfore the function call: t is a positive integer representing the number of test cases, n is a positive integer representing the number of slimes, and a is a list of positive integers where each element a_i represents the size of the i-th slime.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index of the first occurrence of x in the list a plus 1
    #State: Postcondition: `inx` is the index of the first occurrence of `x` in the list `a`, `t` is a positive integer representing the number of test cases, `n` is a positive integer representing the number of slimes, and `a` is a list of positive integers where each element `a_i` represents the size of the i-th slime. Additionally, `a[inx]` is not equal to `x`.
    return inx
    #The program returns the index of the first occurrence of x in the list a.
#Overall this is what the function does:The function accepts a list `a` and an integer `x`. It searches for the first occurrence of `x` in the list `a`. If `x` is not found, it returns -1. If `x` is found, it returns the index of the first occurrence of `x` in the list `a` plus 1.

#State of the program right berfore the function call: a is a list of n non-negative integers representing the sizes of the slimes, and n is a positive integer such that 1 <= n <= 3 * 10^5.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: Output State: `left` is a list containing either 0 or 2, `last` is a list containing -1, -1, 5, ..., up to the final index which is `n-1`, `ans` is a list of length `n` containing -1, `i` is `n`, `n` must be greater than 1.
    #
    #Explanation: After the loop has executed all its iterations, `i` will be equal to `n`. The `last` list will contain `-1` repeated until the final index, which will be `n-1`, because each time `a[i]` is not equal to `a[i - 1]`, `last` appends the current index `i`. The `left` list remains unchanged as it only gets updated under specific conditions that are not met here. The `ans` list remains a list of length `n` filled with -1, and `n` must be greater than 1 for the loop to run through all iterations.
    for i in a:
        left.append(left[-1] + i)
        
    #State: Output State: `left` is a list containing the sum of all elements in `a` starting from the first element, `last` is a list containing -1, -1, 5, ..., up to the final index which is `n-1`, `ans` is a list of length `n` containing -1, `i` is 0 (since `i` will be set to 0 after the loop ends), `a` must be a non-empty list, `n` must be greater than 1, and `left` is updated by appending the value of the last element of `left` plus `i` for each iteration.
    #
    #Explanation: After all iterations of the loop, `i` will be set to 0 since it starts from `n` and decreases by 1 in each iteration until it reaches 0. The `left` list will contain the cumulative sum of all elements in `a` starting from the first element because the loop appends the sum of the last element of `left` and the current element `i` in each iteration. The `last` list will still contain `-1` repeated until the final index which is `n-1`, and `ans` will remain a list of length `n` filled with -1.
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
        
    #State: Output State: `ans` is a list of length `n` containing -1, except for `ans[2]` which is 1, `ans[3]` which is `4 - inx2`, and `ans[4]` which is 1; `i` is 0; `left` contains the cumulative sum of all elements in `a` starting from the first element; `last` still contains `-1` repeated until the final index which is `n-1`; `a` is a non-empty list; `n` is greater than 1; `inx` remains unchanged.
    #
    #Explanation: After all iterations of the loop, `i` will be set to 0 since it starts from `n` and decreases by 1 in each iteration until it reaches 0. The `left` list will contain the cumulative sum of all elements in `a` starting from the first element because the loop appends the sum of the last element of `left` and the current element `i` for each iteration. The `last` list will still contain `-1` repeated until the final index which is `n-1`, and `ans` will remain a list of length `n` filled with -1, except for specific indices as described.
    return ans
    #`ans` is a list of length `n` containing -1, except for `ans[2]` which is 1, `ans[3]` which is `4 - inx2`, and `ans[4]` which is 1; `i` is 0; `left` contains the cumulative sum of all elements in `a` starting from the first element; `last` still contains `-1` repeated until the final index which is `n-1`; `a` is a non-empty list; `n` is greater than 1; `inx` remains unchanged.
#Overall this is what the function does:The function `func_2` accepts a list `a` of non-negative integers and an integer `n`. It returns a list `ans` of length `n` with specific values at indices 2, 3, and 4, sets `i` to 0, and calculates the cumulative sum of all elements in `a`. Additionally, it updates two auxiliary lists `left` and `last` to maintain certain states during the process. The original list `a` and integer `n` remain unchanged.

