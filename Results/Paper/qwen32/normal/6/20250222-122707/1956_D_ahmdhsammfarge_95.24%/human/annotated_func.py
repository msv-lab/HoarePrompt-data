#State of the program right berfore the function call: lst is a list of non-negative integers, r and l are integers that will be used to store the starting and ending indices of a subarray within lst.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `r` and `l` are the indices that maximize the sum expression `sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)^2`, and `over_sum` is the maximum value of this sum expression.
    return r, l
    #The program returns the tuple (r, l) where r and l are the indices that maximize the sum expression `sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)^2`, and `over_sum` is the maximum value of this sum expression.
#Overall this is what the function does:The function accepts a list of non-negative integers and returns a tuple of two indices (r, l) that maximize the sum expression `sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)^2` for all possible subarrays defined by indices i and j.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r, and ops is a list that will store pairs of integers representing operations.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing (None)
    #State: `r` and `l` are integers such that 0 <= l <= r, and `ops` is a list that will store pairs of integers representing operations. Additionally, `r` is not equal to `l`.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` modifies the list `ops` by appending pairs of integers based on the values of `r` and `l`. It does not return any value (returns None).

#State of the program right berfore the function call: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of integers, and ops is a list that will store operations as lists of two integers.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: `r` and `l` are integers such that 0 <= r <= l < len(lst), `lst` is a list of integers, and `ops` is a list that will store operations as lists of two integers, with the additional element `[r + 1, l + 1]` appended to it. If the minimum value in the sublist `lst[r:l + 1]` is 0, the list `ops` will have the element `[r + 1, l + 1]` appended to it. Otherwise, `ops` remains unchanged.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns a list `lst` where the sublist from index `r` to `l` (inclusive) consists of `n` elements, all of which are `n`.
#Overall this is what the function does:The function modifies a given list `lst` by setting all elements in the sublist from index `r` to `l` (inclusive) to the length `n` of that sublist (`n = l - r + 1`). It also appends specific operations to the list `ops` and returns the modified list `lst`.

