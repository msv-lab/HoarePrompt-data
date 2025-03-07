#State of the program right berfore the function call: lst is a list of integers, and r and l are integers that will be used to represent the indices of the subarray to be modified in the main function.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `lst` is a list of integers, `r` and `l` are the indices of the pair `(i, j)` that maximize `sm`, `over_sum` is the maximum value of `sm` found during the iterations, `i` is `len(lst) - 1`, and `j` has completed all possible iterations for the last `i`.
    return r, l
    #The program returns the indices `(r, l)` which represent the pair `(i, j)` that maximize `sm` from the list `lst`.
#Overall this is what the function does:The function accepts a list of integers `lst` and returns a tuple `(r, l)` representing the indices `(i, j)` that maximize the calculated sum `sm`, which is defined as the sum of elements before index `i`, the sum of elements after index `j`, plus the square of the length of the subarray from `i` to `j` inclusive.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r < n, where n is the length of the array a. ops is a list that will store the operations performed.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program does not return any value.
    #State: r and l are integers such that 0 <= l <= r < n, where n is the length of the array a. Additionally, r is not equal to l. ops is a list that will store the operations performed.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` modifies the list `ops` by appending pairs of integers `[r + 1, l + 1]` in a recursive manner based on the initial values of `r` and `l`. The function does not return any value.

#State of the program right berfore the function call: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of non-negative integers, and ops is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: `r` and `l` are integers such that 0 <= r <= l < len(lst), `lst` is a list of non-negative integers, and `ops` is a list that will store the operations performed. The operation `[r + 1, l + 1]` is added to `ops`. If the minimum value in the sublist `lst[r:l + 1]` is 0, the operation `[r + 1, l + 1]` is added to `ops` a second time.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the elements from index `r` to `l` (inclusive) have been replaced by `n` elements, each equal to `n`.
#Overall this is what the function does:The function modifies the list `lst` by replacing the elements from index `r` to `l` (inclusive) with `n` elements, each equal to `n`, where `n` is the length of the sublist from `r` to `l`. It also records operations in the list `ops`.

