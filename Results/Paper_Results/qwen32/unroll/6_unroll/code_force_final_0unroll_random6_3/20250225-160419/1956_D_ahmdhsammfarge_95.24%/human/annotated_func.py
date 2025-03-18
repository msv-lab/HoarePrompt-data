#State of the program right berfore the function call: lst is a list of non-negative integers, r and l are integers that will be used to store the start and end indices of a subarray within lst.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: lst is a list of non-negative integers, r is the starting index of the subarray, l is the ending index of the subarray, over_sum is the maximum calculated sum.
    return r, l
    #The program returns a tuple containing the starting index `r` and the ending index `l` of the subarray.
#Overall this is what the function does:The function takes a list of non-negative integers and returns a tuple containing the starting and ending indices of a subarray. The subarray is chosen such that a specific calculated sum involving the subarray is maximized.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r, and ops is a list that will store the operations performed.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing.
    #State: r and l are integers such that 0 <= l < r, and ops is a list that will store the operations performed.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function modifies the list `ops` by appending operations in the form of pairs `[r + 1, l + 1]` based on the initial values of `r` and `l` and recursively reduces `l` until `l` equals `r`. The function does not return any value.

#State of the program right berfore the function call: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of integers, and ops is a list that will store operations as lists of two integers.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: r and l are integers such that 0 <= r <= l < len(lst), lst is a list of integers, and ops is a list that will store operations as lists of two integers; ops now contains an additional element [r + 1, l + 1]. If the minimum value in the sublist lst[r:l + 1] is 0, then this condition is identified.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the sublist from index `r` to `l` has been replaced with `[n for _ in range(n)]`, and `n` is equal to `l - r + 1`.
#Overall this is what the function does:The function modifies the input list `lst` by replacing the sublist from index `r` to `l` with a new sublist containing `n` elements, each equal to `n`, where `n` is the length of the original sublist (`l - r + 1`). It also appends several operations to the `ops` list.

