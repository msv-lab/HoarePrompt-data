#State of the program right berfore the function call: lst is a list of non-negative integers, and the length of lst is n (1 ≤ n ≤ 18).
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: Output State: `r` is an index from the list `lst`, `l` is an index from the list `lst`, both indices satisfy the condition that the sum of the elements before `i` and after `j` plus `(j - i + 1) ** 2` is greater than `over_sum`. All other variables remain unchanged.
    return r, l
    #The program returns two indices `r` and `l` from the list `lst`, where the sum of the elements before `r` and after `l` plus `(l - r + 1)
#Overall this is what the function does:The function accepts a list `lst` of non-negative integers and returns two indices `r` and `l` from the list, where the sum of the elements before index `r` and after index `l` plus `(l - r + 1)` is maximized.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r < n, and ops is a list used to store the operations.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns a list containing [r + 1, l + 1]
    #State: r and l are integers such that 0 <= l <= r < n, and ops is a list used to store the operations. r is not equal to l
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts three parameters: `r`, `l`, and `ops`. `r` and `l` are integers where `0 <= l <= r < n`, and `ops` is a list used to store operations. If `r` equals `l`, the function appends `[r + 1, l + 1]` to `ops` and returns. Otherwise, it recursively calls itself twice with `l - 1`, appending `[r + 1, l + 1]` to `ops` each time. The function ultimately returns a list containing `[r + 1, l + 1]`.

#State of the program right berfore the function call: `r` and `l` are integers such that `0 <= l <= r < len(lst)` and `lst` is a list of non-negative integers. `ops` is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: `r` is an integer such that `0 <= r < len(lst)`, `l` is an integer such that `0 <= l <= r < len(lst)`, `lst` is a list of non-negative integers, `ops` is a list that includes `[r + 1, l + 1, [r + 1, l + 1]]`. If the minimum value in the sublist `lst[l:r + 1]` is 0, then `ops` is updated to include `[r + 1, l + 1, [r + 1, l + 1], 0]`. Otherwise, `ops` remains as `[r + 1, l + 1, [r + 1, l + 1]]`.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the sublist from index `r + 1` to `l + 1` (inclusive) is replaced by `n` copies of `n`.
#Overall this is what the function does:The function `func_3` takes four parameters: `r`, `l`, `lst`, and `ops`. It updates the list `lst` by replacing the sublist from index `r + 1` to `l + 1` (inclusive) with `n` copies of `n`, where `n` is the length of the specified sublist. Additionally, it appends certain operations to the `ops` list, including the indices `r + 1` and `l + 1`, and possibly the value `0` based on the presence of zero in the sublist. The function ultimately returns the modified list `lst`.

