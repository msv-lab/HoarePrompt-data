#State of the program right berfore the function call: lst is a list of integers, r and l are integers initialized to 0, over_sum is the sum of all elements in lst.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: r is 0, l is 3, over_sum is 16.
    return r, l
    #The program returns (0, 3)
#Overall this is what the function does:The function accepts a list of integers and returns a tuple of two integers. The specific values returned are determined by the internal logic of the function, which evaluates various sums and differences, but for the provided example, it returns `(0, 3)`.

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
#Overall this is what the function does:The function `func_2` takes three parameters: `r` and `l`, which are integers satisfying 0 <= l <= r < n, and `ops`, a list that stores operations performed. It recursively modifies the `ops` list by appending pairs of integers derived from `r` and `l`. The function does not return any value.

#State of the program right berfore the function call: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of integers, and ops is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: `r` and `l` are integers such that 0 <= r <= l < len(lst), lst is a list of integers, and ops is a list that will store the operations performed. If the minimum value in the sublist `lst[r:l + 1]` is 0, the new operation `[r + 1, l + 1]` is appended to `ops`. Otherwise, `ops` remains unchanged.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where elements from index `r` to `l` are all `n` (with `n` = `l - r + 1`).
#Overall this is what the function does:The function modifies a list `lst` by setting all elements from index `r` to `l` to the value `n` (where `n` is the length of the sublist from `r` to `l` inclusive) and returns the modified list.

