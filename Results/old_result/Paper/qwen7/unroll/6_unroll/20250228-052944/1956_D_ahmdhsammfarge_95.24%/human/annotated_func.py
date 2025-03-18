#State of the program right berfore the function call: lst is a list of integers, where the length of lst is n (1 ≤ n ≤ 18), and each element in lst is an integer (0 ≤ a_i ≤ 10^7).
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: Output State: `r` is the index `i` and `l` is the index `j` that maximize the value of `sm`, where `sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2`, and `over_sum` is the maximum value of `sm` found during the loop.
    return r, l
    #The program returns the indices `r` and `l` that maximize the value of `sm`, where `sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)
#Overall this is what the function does:The function accepts a list of integers and returns two indices, `r` and `l`, that maximize the value of `sm`. Here, `sm` is defined as the sum of elements before index `i` plus the sum of elements after index `j` plus the squared distance between the two indices `(j - i + 1)^2`.

#State of the program right berfore the function call: r and l are integers such that 0 <= l <= r < n, and ops is a list that will store the operations performed.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns a list containing [r + 1, l + 1]
    #State: `r` and `l` are integers such that 0 <= `l` <= `r` < `n`, and `ops` is a list that will store the operations performed. The value of `r` is not equal to `l`.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts two integers `r` and `l` and a list `ops`. It appends the operation `[r + 1, l + 1]` to the list `ops` under certain conditions. If `r` equals `l`, it directly appends `[r + 1, l + 1]` to `ops` and returns. Otherwise, it recursively calls itself with `l - 1` and then appends `[r + 1, l + 1]` to `ops` twice before returning. The function ultimately returns a list containing the operation `[r + 1, l + 1]`.

#State of the program right berfore the function call: `r` and `l` are integers such that `0 <= l <= r < len(lst)` and `lst` is a list of non-negative integers. `ops` is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: Postcondition: `ops` is a list containing `[r + 1, l + 1]` and `[r + 1, l + 1]`, `r` is an integer such that `0 <= r < len(lst)`, `l` is an integer such that `0 <= l <= r < len(lst)`, and `lst` is a list of non-negative integers. If the minimum value in the sublist `lst[l:r + 1]` is 0, the function does not change the value of `ops`. There is no else part in the code, so the value of `ops` remains unchanged regardless of whether the condition is met or not.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns a list containing [n, n], [n, r + 1], [n, n], and [n, r + 1]
#Overall this is what the function does:The function `func_3` accepts four parameters: `r`, `l`, `lst` (a list of non-negative integers), and `ops` (a list for storing operations). It appends specific lists to `ops`, calls another function `func_2`, modifies `lst` by replacing the sublist from index `r` to `l` with a list of the same length filled with the value `l - r + 1`, and returns the modified `lst`. The final state of `ops` includes specific lists appended during the function's execution, and the returned list `lst` contains a series of identical values based on the length of the specified sublist.

