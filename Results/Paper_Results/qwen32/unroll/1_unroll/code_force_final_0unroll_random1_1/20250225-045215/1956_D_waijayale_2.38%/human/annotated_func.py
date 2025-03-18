#State of the program right berfore the function call: a is a list of integers where 0 <= a_i <= 10^7 for each element a_i in a, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing operations performed on the array a.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where 0 <= a_i <= 10^7 for each element a_i in a. If `a[l]` was not 0, then `a[l]` is now 0, `l` and `r` are integers such that 1 <= l <= r <= len(a), the element at index `r` in the list `a` is not 0 (unless l == r), and `ops` is a list that now includes the tuple `(l, l)`. If `a[l]` was 0, then no changes are made to `a`, `l`, `r`, or `ops`.
        return
        #The program returns nothing.
    #State: `a` is a list of integers where 0 <= a_i <= 10^7 for each element a_i in a, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `ops` is a list that will store tuples of integers representing operations performed on the array `a`. Additionally, `l` is not equal to `r`.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where all elements from index `l` to `r` (inclusive) are set to `r - l + 1`; `l` and `r` are unchanged integers such that 1 <= l <= r <= len(a); `ops` is a list that still includes the tuple `(l, r)` and no other changes have been made to it.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where elements from index `l + 1` to `r` may be modified if `a[l]` is not equal to `r - l + 1`. `l` and `r` are unchanged integers such that 1 <= l <= r <= len(a). `ops` is a list that includes the tuple `(l, r)` and no other changes have been made to it if `a[l]` is not equal to `r - l + 1`. If `a[l]` is equal to `r - l + 1`, no modifications are made to `a` or `ops`.
#Overall this is what the function does:The function modifies a list of integers `a` within a specified range from index `l` to `r` by setting elements to a specific value if they do not meet a condition. It also records these modifications in the list `ops`. The function does not return any value.

#State of the program right berfore the function call: a is a list of integers, where each integer is in the range 0 to 10^7 inclusive, and n is the length of the list a, such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple where the first element is the sum of all integers in the list `a`, the second element is the length of the list `ops` which is 0, and the third element is the list `ops` which is empty.
#Overall this is what the function does:The function accepts a list `a` of integers, where each integer is in the range 0 to 10^7 inclusive, and the length of the list `a` is between 1 and 18. It returns a tuple containing the sum of all integers in the list `a`, the integer 0, and an empty list.

#State of the program right berfore the function call: l and r are integers such that 1 <= l <= r <= n, where n is the length of the array a.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: The elements in the array `a` from index `l` to `r` are all set to the value `(r - l + 1)`. All other variables, including `l`, `r`, `s`, and `ops`, remain unchanged.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that 1 <= l <= r <= n, where n is the length of the array `a`. `s` is the sum of the elements in the array `a` from index `l` to `r` inclusive. The sum `s` is greater than (r - l + 1) * (r - l + 1). `mx` is the maximum value in the subarray `a[l:r + 1]`. `pos` is the index of `mx` in the subarray `a[l:r + 1]` plus `l`. Additionally, if `pos` is not equal to `l`, then `pos` is not equal to `l`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that 1 <= l <= r <= n, where n is the length of the array `a`. `s` is the sum of the elements in the array `a` from index `l` to `r` inclusive. The sum `s` is greater than (r - l + 1) * (r - l + 1). `mx` is the maximum value in the subarray `a[l:r + 1]`. `pos` is the index of `mx` in the subarray `a[l:r + 1]` plus `l`. Additionally, if `pos` is not equal to `l`, then `pos` is not equal to `l`. If `pos` is not equal to `r`, the current value of `pos` remains unchanged.
    #State: `l` and `r` are integers such that 1 <= l <= r <= n, where n is the length of the array `a`. If the sum `s` of the elements in the array `a` from index `l` to `r` is less than or equal to (r - l + 1) * (r - l + 1), the elements in the array `a` from index `l` to `r` are all set to the value (r - l + 1). Otherwise, `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the subarray `a[l:r + 1]`, and `pos` is the index of `mx` in the subarray `a[l:r + 1]` plus `l`. Additionally, if `pos` is not equal to `l`, then `pos` is not equal to `l`. If `pos` is not equal to `r`, the current value of `pos` remains unchanged. All other variables, including `l`, `r`, `s`, and `ops`, remain unchanged unless specified.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies the array `a` by setting elements within a specified subarray range `[l, r]` to a specific value based on a condition. If the sum of the elements in the subarray is less than or equal to the square of the subarray's length, all elements in that subarray are set to the length of the subarray. Otherwise, the function recursively processes subarrays divided by the maximum element's position within the current range. The function also appends operations to the list `ops` when modifying the array.

#State of the program right berfore the function call: a is a list of integers with length n where 1 <= n <= 18 and 0 <= a_i <= 10^7 for each element a_i in a.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s and m are the first and second return values of func_2(a), respectively)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `a` is the same list of integers, `n` is the same integer, `s` is the same first return value of `func_2(a)`, `m` is the same second return value of `func_2(a)`, `ops` is the same list of pairs.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list `a` of `n` integers from the input, processes the list using `func_2`, and prints the sum `s` and maximum `m` of the list, followed by a series of operations `ops`. The list `a` and the integer `n` remain unchanged after the function concludes.

