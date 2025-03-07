#State of the program right berfore the function call: a is a list of positive integers representing the sizes of the slimes, and x is an integer representing a target size such that 1 <= x <= 10^9.
def func_1(a, x):
    if (x < 0) :
        return -1
        #The program returns -1
    #State: a is a list of positive integers representing the sizes of the slimes, and x is an integer representing a target size such that 1 <= x <= 10^9, and x is greater than or equal to 0
    inx = bl(a, x)
    if (a[inx] == x) :
        return inx + 1
        #The program returns the index of the element in list 'a' that is equal to 'x', plus 1.
    #State: `a` is a list of positive integers representing the sizes of the slimes, `x` is an integer representing a target size such that 1 <= x <= 10^9, and x is greater than or equal to 0, `inx` is the index of the element in list `a` that is greater than or equal to `x`, and `a[inx]` is not equal to `x`
    return inx
    #The program returns the index 'inx' of the element in list 'a' that is greater than or equal to 'x', where 'a[inx]' is not equal to 'x'.
#Overall this is what the function does:The function accepts a list `a` of positive integers and an integer `x` such that 1 ≤ x ≤ 10^9. It returns -1 if there is no element in `a` that matches `x`. If there is an element in `a` that exactly matches `x`, it returns the index of that element plus one. If no exact match is found, it returns the index of the smallest element in `a` that is greater than or equal to `x`, also plus one.

#State of the program right berfore the function call: a is a list of n integers representing the sizes of the slimes, and n is a positive integer such that 1 <= n <= 3 * 10^5. Each integer a_i in the list satisfies 1 <= a_i <= 10^9.
def func_2(a, n):
    left = [0]
    last = [-1]
    ans = [-1] * n
    for i in range(1, n):
        if a[i] != a[i - 1]:
            last.append(i)
        else:
            last.append(last[-1])
        
    #State: The list `last` will contain the indices of the first occurrence of each unique element in the list `a`, and `i` will be equal to `n`.
    for i in a:
        left.append(left[-1] + i)
        
    #State: Output State: The list `last` contains the indices of the first occurrence of each unique element in the list `a`. The variable `i` will be equal to the last element of the list `a`. The list `left` will have its last element increased by the sum of all elements in the list `a`.
    #
    #In more detail, the list `last` remains unchanged as it only records the first occurrences of unique elements and does not get updated inside the loop. The variable `i` will hold the value of the last element in the list `a` after the loop completes. The list `left` will have its last element updated to be the sum of all elements in the list `a`, as each iteration adds the current element `i` to the last element of `left`.
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
        
    #State: The loop has completed all iterations, with `i` now equal to `n`. The list `a` remains unchanged. The list `ans` is updated such that for each index `i` from 1 to `n-1`, `ans[i]` is calculated based on the logic within the loop. Specifically, `ans[i]` is set to `2 - inx` if `inx` is less than or equal to 0, otherwise it is set to `i + 1 - inx`. The variable `inx` is determined by comparing `inx2` (which is `last[i - 1]`) and `inx` (calculated using `func_1(left, x)`), and `inx` is adjusted to be 0 if it is negative. The list `left` is updated such that its last element is the sum of all elements in the list `a`.
    return ans
    #The program returns a list `ans` where each element `ans[i]` (for i from 1 to n-1) is calculated as follows: if `inx` (determined by the logic inside the loop) is less than or equal to 0, then `ans[i] = 2 - inx`; otherwise, `ans[i] = i + 1 - inx`. The last element of the list `left` is the sum of all elements in the list `a`.
#Overall this is what the function does:The function accepts a list `a` of n integers representing the sizes of the slimes, and an integer `n` indicating the length of the list. It returns a list `ans` where each element `ans[i]` (for i from 1 to n-1) is calculated based on the value of `inx` determined by the logic inside the loop: if `inx` is less than or equal to 0, then `ans[i] = 2 - inx`; otherwise, `ans[i] = i + 1 - inx`. Additionally, the last element of the list `left` is updated to be the sum of all elements in the list `a`.

