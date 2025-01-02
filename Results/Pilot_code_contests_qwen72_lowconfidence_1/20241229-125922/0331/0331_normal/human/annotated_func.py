#State of the program right berfore the function call: l and r are non-negative integers where l <= r.
def func_1(l, r):
    if (r != l) :
        ind = (r + l) // 2
        func_1(l, ind)
        func_1(ind + 1, r)
        func_2(l, ind, ind + 1, r)
    #State of the program after the if block has been executed: *`l` and `r` are non-negative integers where `l` <= `r`. If `r` is not equal to `l`, `ind` is set to `(r + l) // 2`, `func_1(ind + 1, r)` is called, and `func_2(l, ind, ind + 1, r)` is called.
#Overall this is what the function does:The function `func_1` is a recursive function that takes two non-negative integer parameters `l` and `r` where `l` ≤ `r`. It divides the range `[l, r]` into two halves and recursively calls itself on each half. After the recursive calls, it calls another function `func_2` with the parameters `l`, `ind`, `ind + 1`, and `r`, where `ind` is the midpoint of the current range. The function does not return any value explicitly. The final state of the program after the function concludes is that the function has divided the range `[l, r]` into smaller sub-ranges and performed operations (via `func_2`) on these sub-ranges. The exact nature of these operations is not specified within `func_1` but is left to `func_2`. Edge cases include when `l` equals `r`, in which case no further recursion occurs and `func_2` is not called.

#State of the program right berfore the function call: lf, rf, ls, and rs are non-negative integers where lf <= rf and ls <= rs, and queue is a list of integers.
def func_2(lf, rf, ls, rs):
    a = []
    ind1 = lf
    ind2 = ls
    while ind1 <= rf and ind2 <= rs:
        if queue[ind1] < queue[ind2]:
            a.append(queue[ind1])
            ind1 += 1
        else:
            a.append(queue[ind2])
            ind2 += 1
        
    #State of the program after the loop has been executed: `ind1` is either `rf + 1` or less than or equal to `rf`, `ind2` is either `rs + 1` or less than or equal to `rs`, `a` is a list containing elements from `queue` such that the elements are in non-decreasing order up to the point where either `ind1` exceeds `rf` or `ind2` exceeds `rs`. If `ind1` exceeds `rf`, all elements from `ind2` to `rs` are appended to `a`. If `ind2` exceeds `rs`, all elements from `ind1` to `rf` are appended to `a`.
    while ind1 <= rf:
        a.append(queue[ind1])
        
        ind1 += 1
        
    #State of the program after the loop has been executed: `ind1` is `rf + 1`, `ind2` is either `rs + 1` or less than or equal to `rs`, `a` is a list containing elements from `queue` such that the elements are in non-decreasing order up to the point where `ind1` exceeded `rf` or `ind2` exceeded `rs`. If `ind1` exceeded `rf`, all elements from `ind2` to `rs` are appended to `a`.
    while ind2 <= rs:
        a.append(queue[ind2])
        
        ind2 += 1
        
    #State of the program after the loop has been executed: `ind1` is `rf + 1`, `ind2` is `rs + 1`, `a` is a list containing elements from `queue` in non-decreasing order up to the point where `ind1` exceeded `rf` or `ind2` exceeded `rs`, and now includes all elements from `queue[rs + 1 - (rs - (rs + 1)) : rs + 1]` which simplifies to `queue[rs + 1 - (rs - ind2_initial) : rs + 1]` where `ind2_initial` is the initial value of `ind2`
    for i in range(lf, rs + 1):
        queue[i] = a[i - lf]
        
    #State of the program after the  for loop has been executed: `ind1` is `rf + 1`, `ind2` is `rs + 1`, `a` is a list containing elements from `queue` in non-decreasing order up to the point where `ind1` exceeded `rf` or `ind2` exceeded `rs`, and now includes all elements from `queue[rs + 1 - (rs - ind2_initial) : rs + 1]`, `lf` and `rs` remain unchanged, `queue` from index `lf` to `rs` is updated to the corresponding elements from the `a` list. If `lf > rs`, `queue` remains unchanged.
#Overall this is what the function does:The function `func_2` takes four non-negative integer parameters `lf`, `rf`, `ls`, and `rs` (with the constraints `lf <= rf` and `ls <= rs`) and a list of integers `queue`. It merges the sublists `queue[lf:rf+1]` and `queue[ls:rs+1]` into a single sorted sublist in non-decreasing order and places the result back into `queue[lf:rs+1]`. The function modifies the `queue` in place and does not return any value. If `lf > rs`, the function does nothing and `queue` remains unchanged.

