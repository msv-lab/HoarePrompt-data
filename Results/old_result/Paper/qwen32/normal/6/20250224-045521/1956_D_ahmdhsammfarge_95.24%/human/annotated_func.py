#State of the program right berfore the function call: lst is a list of non-negative integers, r and l are integers that will be used to store the indices of the subarray to be modified in the main function, over_sum is a variable used to keep track of the maximum sum calculated during the execution of the function.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `r` and `l` are the indices `[i, j]` that maximize `sm`, and `over_sum` is the maximum `sm` found.
    return r, l
    #The program returns the indices `[i, j]` that maximize `sm`, where `r` is `i` and `l` is `j`. The maximum `sm` found is `over_sum`.
#Overall this is what the function does:The function takes a list of non-negative integers and returns a tuple of indices `[i, j]` that define a subarray. The subarray is chosen such that the sum of the elements outside the subarray plus the square of the length of the subarray is maximized.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r < n, and ops is a list that will store the operations performed.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing.
    #State: r and l are integers such that 0 <= l <= r < n, and ops is a list that will store the operations performed. Additionally, r is not equal to l
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` takes three parameters: `r` and `l`, which are integers satisfying 0 <= l <= r < n, and `ops`, which is a list that stores operations performed. It modifies the list `ops` by appending operations in a specific pattern based on the values of `r` and `l`. The function does not return anything.

#State of the program right berfore the function call: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of non-negative integers, and ops is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: `r` and `l` are integers such that 0 <= r <= l < len(lst), `lst` is a list of non-negative integers, and `ops` is a list that will store the operations performed. If the minimum value in the sublist `lst[r:l + 1]` is 0, the new operation `[r + 1, l + 1]` is appended to `ops`.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the elements from index `r` to `l` are all equal to `n`, and `n` is `l - r + 1`.
#Overall this is what the function does:The function modifies a list `lst` by setting all elements in the range from index `r` to `l` (inclusive) to the value `n`, where `n` is the length of the range (`l - r + 1`). It also records operations in the list `ops`. The function returns the modified list `lst`.

