#State of the program right berfore the function call: lst is a list of non-negative integers of length n, where 1 <= n <= 18.
def func_1(lst):
    r = l = 0
    over_sum = sum(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sm = sum(lst[:i]) + sum(lst[j + 1:]) + (j - i + 1) ** 2
            if sm > over_sum:
                r, l = [i, j]
                over_sum = sm
        
    #State: `r` and `l` store the indices that maximize the value of `sm`, which is the sum of elements from the start of `lst` to index `i-1` plus the sum of elements from index `j+1` to the end of `lst` plus the square of `(j - i + 1)`. `over_sum` holds the maximum value of `sm` found during the loop's execution. `i` and `j` will be the last values they were set to before the loop terminated. `lst` remains unchanged from its initial state.
    return r, l
    #The program returns the indices `r` and `l` that maximize the value of `sm`, which is the sum of elements from the start of `lst` to index `i-1` plus the sum of elements from index `j+1` to the end of `lst` plus the square of `(j - i + 1)`. The variables `over_sum`, `i`, and `j` hold the maximum value of `sm` found during the loop's execution, and the last values they were set to before the loop terminated, respectively.
#Overall this is what the function does:The function accepts a list of non-negative integers (`lst`) and returns two indices (`r` and `l`) that maximize the value of `sm`. The value of `sm` is calculated as the sum of elements from the start of `lst` to index `i-1` plus the sum of elements from index `j+1` to the end of `lst` plus the square of `(j - i + 1)`. After the function executes, `lst` remains unchanged, and the returned indices correspond to the pair that yields the highest possible value of `sm`.

#State of the program right berfore the function call: r and l are non-negative integers such that 0 <= l <= r < n, and ops is a list that will store the operations performed.
def func_2(r, l, ops):
    if (r == l) :
        ops.append([r + 1, l + 1])
        return
        #The program returns None
    #State: r and l are non-negative integers such that 0 <= l <= r < n, and ops is a list that will store the operations performed. r is not equal to l
    func_2(r, l - 1, ops)
    ops.append([r + 1, l + 1])
    func_2(r, l - 1, ops)
#Overall this is what the function does:The function `func_2` accepts three parameters: `r`, `l`, and `ops`. It does not return any value. If `r` equals `l`, it appends `[r + 1, l + 1]` to the `ops` list and returns. Otherwise, it recursively calls itself twice with `l - 1`, appending `[r + 1, l + 1]` to the `ops` list after each call. The final state of the program is that the `ops` list contains specific operations based on the values of `r` and `l`.

#State of the program right berfore the function call: `r` and `l` are integers such that `0 <= l <= r < len(lst)` and `lst` is a list of non-negative integers. `ops` is a list that will store the operations performed.
def func_3(r, l, lst, ops):
    ops.append([r + 1, l + 1])
    if (min(lst[r:l + 1]) == 0) :
        ops.append([r + 1, l + 1])
    #State: Postcondition: `ops` is a list containing the sublist `[r + 1, l + 1]` appended with another sublist `[r + 1, l + 1]`, `r` is an integer such that `0 <= r < len(lst)`, `l` is an integer such that `0 <= l <= r < len(lst)`, and `lst` is a list of non-negative integers. If the minimum value in the sublist `lst[r:l + 1]` is 0, then `ops` contains an additional sublist `[r + 1, l + 1]`. There is no change in the else part.
    ops.append([r + 1, r + 1])
    func_2(r, l, ops)
    ops.append([r + 1, l + 1])
    n = l - r + 1
    lst[r:l + 1] = [n for _ in range(n)]
    return lst
    #The program returns a list 'lst' where the elements from index r to l (inclusive) are replaced by a list of n elements, each element being n, and the rest of the list remains unchanged.
#Overall this is what the function does:The function `func_3` accepts four parameters: `r`, `l`, `lst`, and `ops`. It replaces the elements in `lst` from index `r` to `l` (inclusive) with a list of `n` elements, each being `n`, where `n` is the length of the range from `l` to `r`. The rest of the list remains unchanged, and then returns the modified list `lst`. Additionally, it appends specific sublists to the `ops` list based on certain conditions.

