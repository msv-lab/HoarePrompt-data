#State of the program right berfore the function call: a is a list of integers where 0 <= a[i] <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where 0 <= a[i] <= 10^7 for all i, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `ops` is a list that will store tuples of integers representing the operations performed. If `a[l]` is not 0, no changes are made to `a`, `l`, `r`, or `ops`. If `a[l]` is 0, then `a[l]` is set to 0 (which is already the case), and `ops` is updated to contain the tuple `(l, l)`.
        return
        #The program returns nothing.
    #State: `a` is a list of integers where 0 <= a[i] <= 10^7, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `ops` is a list that will store tuples of integers representing the operations performed. Additionally, `l` is not equal to `r`.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where the elements from index `l` to `r` (inclusive) are all set to the value `r - l + 1`. All other elements of `a` remain unchanged. `l` and `r` are integers such that 1 <= l <= r <= len(a), and `l` is not equal to `r`. `ops` includes the additional tuple `(l, r)`.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where, if `a[l]` was not equal to `r - l + 1`, the elements from index `l` to `r` (inclusive) are set to the value `r - l + 1`. All other elements of `a` remain unchanged. `l` and `r` are integers such that 1 <= l <= r <= len(a), and `l` is not equal to `r`. `ops` includes the additional tuple `(l, r)` if the if condition was true. The function `func_1` is called with arguments `a`, `l + 1`, `r`, and `ops`. If `a[l]` was equal to `r - l + 1`, no changes are made to `a` or `ops`.
#Overall this is what the function does:The function `func_1` modifies a list of integers `a` by setting elements within a specified range `[l, r]` to a specific value if certain conditions are met. It also records these modifications in the `ops` list. The function does not return any value.

#State of the program right berfore the function call: a is a list of integers where each integer satisfies 0 <= a[i] <= 10^7, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all integers in the list `a`, the length of the list `ops`, and the list `ops` itself.
#Overall this is what the function does:The function takes a list of integers `a` as input, where each integer is between 0 and 10^7, and the length of the list is between 1 and 18. It returns a tuple containing the sum of all integers in the list `a`, the length of the list `ops`, and the list `ops` itself. The purpose of the function is to compute the sum of the list and return it along with the length and contents of `ops`, which is modified by the recursive_maximize_sum function.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < len(a).
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of `a[l:r + 1]`. The current value of `s` is (r - l + 1) * (r - l + 1). The list `ops` now includes the tuple `(l, r)`. All elements in the list `a` from index `l` to index `r` (inclusive) are now set to the value (r - l + 1).
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of `a[l:r + 1]` and is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `l`, then the current value of `pos` is not equal to `l`. Otherwise, no further changes are made to `l`, `r`, `s`, `mx`, or `pos`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of `a[l:r + 1]` and is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called. If `pos` is equal to `r`, no further changes are made to `l`, `r`, `s`, `mx`, or `pos`.
    #State: `l` and `r` are integers such that 0 <= l <= r < len(a); `s` is the sum of `a[l:r + 1]`. If `s` is less than or equal to (r - l + 1) * (r - l + 1), `s` is updated to (r - l + 1) * (r - l + 1) and all elements in the list `a` from index `l` to index `r` (inclusive) are set to the value (r - l + 1), and the tuple `(l, r)` is added to the list `ops`. If `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the sublist `a[l:r + 1]`, and `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called. If `pos` is equal to `r`, no further changes are made to `l`, `r`, `s`, `mx`, or `pos`.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies the list `a` by setting elements within the range from index `l` to `r` to a specific value if a certain condition is met, and recursively processes subarrays otherwise. It also appends operations to the list `ops`. The final state of the program is that the elements in `a` from index `l` to `r` may be modified, and `ops` contains tuples representing the ranges that have been processed.

#State of the program right berfore the function call: a is a list of integers where 0 <= len(a) <= 18 and 0 <= a[i] <= 10^7 for each i in the range of the length of a.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s and m are values returned by the function `func_2(a)`)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `a` is a list of integers derived from the input, `n` is an input integer, `s`, `m`, and `ops` are the values returned by `func_2(a)`. The loop prints pairs of integers `(l + 1, r + 1)` for each `(l, r)` in `ops`.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list of integers `a` from the input, processes the list using the function `func_2`, and prints two values `s` and `m` returned by `func_2`. It also prints pairs of integers derived from the operations list `ops` returned by `func_2`.

