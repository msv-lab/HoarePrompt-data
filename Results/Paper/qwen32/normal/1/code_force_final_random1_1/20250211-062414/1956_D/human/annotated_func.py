#State of the program right berfore the function call: a is a list of integers where each element satisfies 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing operations performed on the array a.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where each element satisfies 0 <= a_i <= 10^7, except `a[l]` which is now 0 if `a[l]` was not 0 initially; `l` and `r` are integers such that 1 <= l <= r <= len(a), and `l` is equal to `r`; `ops` is a list that stores tuples of integers representing operations performed on the array `a`, and `ops` now contains the tuple `(l, l)` if `a[l]` was not 0 initially.
        return
        #The program returns nothing (None)
    #State: a is a list of integers where each element satisfies 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing operations performed on the array a. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where each element satisfies `0 <= a_i <= 10^7`, except all elements from `a[l]` to `a[r]` (inclusive) which are now `r - l + 1`; `l` is an integer such that `2 <= l <= len(a)`, `r` is an integer such that `l <= r <= len(a)`, `i` is `r`, and `ops` is a list that will store tuples of integers representing operations performed on the array `a` with the additional element `(l, r)` appended to it.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where each element satisfies `0 <= a_i <= 10^7`. If `a[l]` was not equal to `r - l + 1`, then all elements from `a[l]` to `a[r]` (inclusive) are now `r - l + 1`, `l` is an integer such that `2 <= l <= len(a)`, `r` is an integer such that `l <= r <= len(a)`, `i` is `r`, and `ops` is a list that stores tuples of integers representing operations performed on the array `a` with the additional element `(l, r)` appended to it. Otherwise, no changes are made to `a`, `l`, `r`, or `ops`.
#Overall this is what the function does:The function `func_1` modifies a list of integers `a` by potentially setting certain subarrays to a specific value based on conditions, and records these modifications in a list `ops`. It does not return any value.

#State of the program right berfore the function call: a is a list of integers where each integer is between 0 and 10^7 inclusive, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all integers in the list `a`, the length of the list `ops`, and the list `ops` itself.
#Overall this is what the function does:The function accepts a list `a` of integers, each between 0 and 10^7 inclusive, and returns a tuple containing the sum of all integers in the list `a`, the length of the list `ops`, and the list `ops` itself.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < len(a), where a is a list of integers.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`; `s` is the sum of the elements from index `l` to `r` (inclusive) in the list `a`, and `s` is equal to `(r - l + 1) * (r - l + 1)`; `ops` now includes the tuple `(l, r)`; `a[i]` is `r - l + 1` for all `i` in the range `[l, r]`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a). `s` is the sum of the elements from index l to r (inclusive) in the list a, and s > (r - l + 1) * (r - l + 1). `mx` is the maximum value in the sublist a[l:r + 1]. `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `l`, the function `recursive_maximize_sum(l, pos - 1)` has been called.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a). `s` is the sum of the elements from index l to r (inclusive) in the list a, and s > (r - l + 1) * (r - l + 1). `mx` is the maximum value in the sublist a[l:r + 1]. `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `l`, the function `recursive_maximize_sum(l, pos - 1)` has been called. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
    #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`. `s` is the sum of the elements from index `l` to `r` (inclusive) in the list `a`. If `s` is equal to `(r - l + 1) * (r - l + 1)`, then `ops` includes the tuple `(l, r)` and all elements `a[i]` in the range `[l, r]` are set to `r - l + 1`. Otherwise, `s` is greater than `(r - l + 1) * (r - l + 1)`, and the maximum value `mx` in the sublist `a[l:r + 1]` has been identified at index `pos`. If `pos` is not equal to `l`, the function `recursive_maximize_sum(l, pos - 1)` has been called. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies a list `a` by potentially replacing segments of it with a constant value such that the sum of each segment equals the square of its length. It also records the operations performed in a list `ops`. The function does not return a value but alters the list `a` in place based on the conditions specified.

#State of the program right berfore the function call: a is a list of integers where 1 <= len(a) <= 18 and 0 <= a[i] <= 10^7 for all i in the range of the length of a.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s and m are the values returned by func_2(a))
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `a` is a list of integers, `n` is an input integer, `s`, `m`, and `ops` are the values returned by `func_2(a)`, and all tuples in `ops` have been printed.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list of integers `a` from the input, processes the list using `func_2`, and prints two values `s` and `m` followed by a series of operations. The final state includes the printed values `s`, `m`, and the operations derived from processing the list `a`.

