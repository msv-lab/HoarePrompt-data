#State of the program right berfore the function call: lst is a list of integers with length n (1 ≤ n ≤ 18).
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: After the loop executes all iterations, `lst` remains a list of integers with length `n` (1 ≤ `n` ≤ 18). `i` is `n - 1`, `j` is `len(lst) - 1`, `over_sum` is the maximum value of `sm` found during the loop iterations, and `r` and `l` are set to the corresponding indices `[i, j]` where this maximum `sm` was found.
    return r, l
    #The program returns the indices `r` and `l` where `r` is `n - 1` and `l` is `len(lst) - 1`. These indices correspond to the positions in the list `lst` where the maximum value of `sm` was found during the loop iterations.
#Overall this is what the function does:The function `func_1` accepts a list of integers `lst` with length `n` (1 ≤ n ≤ 18) and returns two indices, `r` and `l`. These indices correspond to the positions in `lst` where the sum of the elements before `i`, the elements after `j`, and the square of the length of the subarray between `i` and `j` (inclusive) is maximized. The function does not modify the input list `lst`.

#State of the program right berfore the function call: r and l are integers such that 1 <= r <= l <= n, and ops is a list that will store the operations as pairs of integers [r + 1, l + 1].
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns nothing.
    #State: r and l are integers such that 1 <= r <= l <= n, and ops is a list that will store the operations as pairs of integers [r + 1, l + 1]. Additionally, r is not equal to l.
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts two integers `r` and `l` and a list `ops`. It ensures that `r` and `l` are within the range 1 to n. If `r` is equal to `l`, it appends the pair `[r + 1, l + 1]` to the list `ops` and returns. If `r` is not equal to `l`, it recursively calls itself twice with `l` decremented by 1, and appends the pair `[r + 1, l + 1]` to `ops` between the recursive calls. The function does not return any value, but modifies the `ops` list. After the function concludes, `ops` contains multiple pairs `[r + 1, l + 1]` for each recursive call where `r` is not equal to `l`.

#State of the program right berfore the function call: lst is a list of integers, r and l are non-negative integers such that 0 <= r <= l < len(lst), and ops is a list of lists where each inner list contains two integers representing the operation parameters.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: *`lst` is a list of integers, `r` and `l` are non-negative integers such that 0 <= r <= l < len(lst), `ops` is a list of lists where each inner list contains two integers representing the operation parameters, and `ops` now includes an additional list `[r + 1, l + 1]`. If the minimum value in the sublist `lst[r:l + 1]` is 0, the function operates accordingly. Otherwise, the function does not perform any additional operations.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns the updated list `lst` where the sublist `lst[r:l + 1]` consists of `n` elements, each equal to `n`. The variables `r`, `l`, and `ops` remain unchanged, and `n` is still equal to `l - r + 1`. If the minimum value in the original sublist `lst[r:l + 1]` was 0, the function may have performed some operation, but the exact changes are unknown. If the minimum value was not 0, no additional operations were performed.
#Overall this is what the function does:The function `func_3` accepts parameters `r`, `l`, `lst`, and `ops`, where `r` and `l` are non-negative integers such that `0 <= r <= l < len(lst)`, `lst` is a list of integers, and `ops` is a list of lists where each inner list contains two integers representing operation parameters. The function updates the sublist `lst[r:l + 1]` to consist of `n` elements, each equal to `n`, where `n` is `l - r + 1`. Additionally, the function appends several lists to `ops`, including `[r + 1, l + 1]`, `[r + 1, r + 1]`, and potentially `[r + 1, l + 1]` again if the minimum value in the original sublist `lst[r:l + 1]` is 0. The function returns the updated list `lst`. The variables `r`, `l`, and `n` remain unchanged.

