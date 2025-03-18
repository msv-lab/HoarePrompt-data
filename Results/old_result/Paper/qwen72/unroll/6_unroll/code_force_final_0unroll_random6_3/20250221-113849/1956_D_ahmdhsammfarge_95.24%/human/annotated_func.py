#State of the program right berfore the function call: lst is a list of integers of length n, where 1 <= n <= 18.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `lst` is a list of integers of length n, where 1 <= n <= 18; `r` is the index i; `l` is the index j; `over_sum` is the maximum possible value of `sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)
    return r, l
    #The program returns the values of `r` and `l`, where `r` is the index `i` and `l` is the index `j`. These indices are part of the initial state and are used to calculate `over_sum` as the maximum possible value of `sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1)`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `lst` and returns two indices `r` and `l`. These indices are chosen such that the value of `sum(lst[:r]) + sum(lst[l + 1:]) + (l - r + 1)

#State of the program right berfore the function call: r and l are integers such that 1 <= r <= l <= n, and ops is a list that can store pairs of integers.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing.
    #State: r and l are integers such that 1 <= r <= l <= n, and ops is a list that can store pairs of integers. Additionally, r is not equal to l.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts two integers `r` and `l` within the range 1 to n, and a list `ops` that can store pairs of integers. It modifies the `ops` list by appending pairs of integers `[r + 1, l + 1]` in a recursive manner. The function does not return any value, but the final state of the `ops` list will contain multiple pairs of integers, each representing a modified version of the input `r` and `l` incremented by 1. The exact number of pairs and their values depend on the initial values of `r` and `l`.

#State of the program right berfore the function call: lst is a list of integers, r and l are non-negative integers such that 0 <= r <= l < len(lst), and ops is a list of lists where each inner list contains two integers representing the parameters of an operation.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: *`lst` is a list of integers, `r` and `l` are non-negative integers such that 0 <= r <= l < len(lst), `ops` is a list of lists where each inner list contains two integers representing the parameters of an operation, and the last element of `ops` is `[r + 1, l + 1]`. If the minimum value in the sublist `lst[r:l + 1]` is 0, the function performs the operation specified in the if part.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the list `lst` where the elements from index `r` to index `l` (inclusive) are all set to the value `n`, and `n` is equal to `l - r + 1`. The rest of the elements in `lst` remain unchanged.
#Overall this is what the function does:The function `func_3` accepts parameters `r`, `l`, `lst`, and `ops`. It modifies the list `ops` by appending several operations, and it returns the list `lst` with the elements from index `r` to index `l` (inclusive) set to the value `n`, where `n` is `l - r + 1`. The rest of the elements in `lst` remain unchanged. The function also ensures that if the minimum value in the sublist `lst[r:l + 1]` is 0, an additional operation is appended to `ops`.

