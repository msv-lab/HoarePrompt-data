#State of the program right berfore the function call: a is a list of integers where 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where 0 <= a_i <= 10^7, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `l` equals `r`. If `a[l]` is not 0, no changes are made to `a` or `ops`. If `a[l]` is 0, `ops` now contains the tuple `(l, l)` as its last element.
        return
        #The program returns None
    #State: a is a list of integers where 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing the operations performed. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where `a[i]` is `r - l + 1` for `l-1 <= i <= r-1`, and `a[j]` retains its original value for all other indices `j`; `l` and `r` are integers such that 1 <= l < r <= len(a); `ops` is a list that stores tuples of integers representing the operations performed, and now includes the tuple `(l, r)`
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where 0 <= a_i <= 10^7, `l` and `r` retain their original values, and `ops` is a list that stores tuples of integers representing the operations performed. If `a[l]` is not equal to `r - l + 1`, `a` may be modified by calling `func_1(a, l + 1, r, ops)` and the tuple `(l, r)` is added to `ops`.
#Overall this is what the function does:The function modifies the list `a` by setting certain subarrays to a specific value based on the condition that the sum of the subarray should match the length of the subarray. It records these modifications in the list `ops` as tuples indicating the start and end indices of the modified subarrays. The function does not return any value.

#State of the program right berfore the function call: a is a list of integers where each integer is in the range 0 to 10^7, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all integers in the list `a`, the length of the list `ops`, and the list `ops` itself.
#Overall this is what the function does:The function takes a list of integers `a` as input, computes the sum of all integers in the list, and returns a tuple containing this sum, the length of an operations list `ops`, and the `ops` list itself. The operations list `ops` is not modified or used within the provided code snippet, so its length will be zero and it will be empty.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < len(a), where a is a list of integers.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `a` is a list of integers where `a[i]` is `r - l + 1` for all `i` in `[l, r]`; `s` is the sum of the elements from index `l` to `r` (inclusive) in the list `a`, adjusted for the new value of `a[i]` for all `i` in `[l, r]`; `result` is returned; `ops` contains an additional tuple `(l, r)`; `i` is `r`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of the elements from index `l` to `r` (inclusive) in the list `a` and is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the list `a`. If `pos` was not equal to `l` initially, `pos` may have changed based on the function's logic.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of the elements from index `l` to `r` (inclusive) in the list `a` and is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
    #State: `l` and `r` are integers such that 0 <= l <= r < len(a). If `s` is less than or equal to (r - l + 1) * (r - l + 1), then `a[i]` is `r - l + 1` for all `i` in `[l, r]`, `s` is adjusted accordingly, `result` is returned, and `ops` contains an additional tuple `(l, r)`. Otherwise, `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the sublist `a[l:r + 1]`, and `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies a list `a` by potentially changing the values within a specified range `[l, r]` based on certain conditions. It appends operations to a list `ops` and ensures that if the sum of the elements in the range `[l, r]` is less than or equal to the square of the length of the range, all elements in that range are set to the length of the range. Otherwise, it recursively processes subranges around the maximum element in the range.

#State of the program right berfore the function call: a is a list of integers where 1 <= len(a) <= 18 and 0 <= a[i] <= 10^7 for each element a[i] in a.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (where s is the sum of all elements in the list `a`), m (where m is the maximum value in the list `a`)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `a` is a list of integers obtained from the input, where 1 <= len(a) <= 18 and 0 <= a[i] <= 10^7 for each element a[i] in a; `n` is an input integer; `s`, `m`, and `ops` are the values returned by `func_2(a)`, where all tuples in `ops` have been printed.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list `a` of integers from the input, computes the sum and maximum of the list, prints these values, and then prints a series of operations (if any) returned by another function `func_2`. The final state includes the printed sum and maximum of the list, along with any additional operations.

