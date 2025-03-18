#State of the program right berfore the function call: lst is a list of integers such that 1 <= len(lst) <= 18 and 0 <= lst[i] <= 10^7 for all 0 <= i < len(lst).
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `r` and `l` are the indices that maximize the sum `sm`, and `over_sum` is the maximum value of `sm` found.
    return r, l
    #The program returns the indices `r` and `l` that maximize the sum `sm`.
#Overall this is what the function does:The function `func_1` accepts a list `lst` of integers and returns a tuple `(r, l)` representing the start and end indices of a sublist in `lst` such that the sum of the elements outside this sublist plus the square of the length of the sublist is maximized. The function ensures that `r` and `l` are the indices that achieve this maximum sum, and `over_sum` holds the maximum value of this sum.

#State of the program right berfore the function call: r and l are non-negative integers such that r <= l, and ops is a list that can hold sublists of two integers.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing.
    #State: r and l are non-negative integers such that r < l, and ops is a list that can hold sublists of two integers.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts two non-negative integers `r` and `l` where `r` is less than or equal to `l`, and a list `ops` that can contain sublists of two integers. It modifies the `ops` list by appending sublists of the form `[r + 1, l + 1]` multiple times, depending on the difference between `r` and `l`. The function does not return any value. After the function concludes, the `ops` list will contain a series of sublists, each of which is `[r + 1, l + 1]`, and the number of such sublists will be `2^(l - r)`. The original values of `r` and `l` remain unchanged.

#State of the program right berfore the function call: lst is a list of integers, r and l are non-negative integers such that 0 <= r <= l < len(lst), and ops is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: lst is a list of integers, r and l are non-negative integers such that 0 <= r <= l < len(lst), and ops is a list that contains the operations [r + 1, l + 1]. If the minimum value in the sublist lst[r:l + 1] is 0, then ops contains the operations [r + 1, l + 1] twice. Otherwise, ops contains the operations [r + 1, l + 1] once.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the elements from index `r` to index `l` are all equal to `n` (where `n = l - r + 1`), and the rest of the list remains unchanged.
#Overall this is what the function does:The function `func_3` accepts parameters `r`, `l`, `lst`, and `ops`. It modifies the list `lst` by setting the elements from index `r` to index `l` to the value `n` (where `n = l - r + 1`), and returns the modified list `lst`. Additionally, the function appends the operation `[r + 1, l + 1]` to the `ops` list at least twice, and if the minimum value in the sublist `lst[r:l + 1]` is 0, it appends this operation a third time. The rest of the list `lst` remains unchanged.

