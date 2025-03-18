#State of the program right berfore the function call: a is a list of integers where 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where 0 <= a_i <= 10^7, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `ops` is a list that will store tuples of integers representing the operations performed. Currently, `l` equals `r`. If `a[l]` is not 0, no changes are made to `a`, `l`, `r`, or `ops`. If `a[l]` is 0, `ops` now contains one tuple `(l, l)`.
        return
        #The program does not return any value.
    #State: a is a list of integers where 0 <= a_i <= 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples of integers representing the operations performed. Additionally, l is not equal to r
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where elements from index `l-1` to `r-1` are set to `r - l + 1`, and all other elements remain unchanged; `l` and `r` are integers such that \(1 \leq l < r \leq \text{len}(a)\); `ops` is a list that stores tuples of integers representing the operations performed, and now includes the tuple `(l, r)`; `i` is `r`.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where, if `a[l]` was not equal to `r - l + 1`, the elements from index `l-1` to `r-1` are set to `r - l + 1`, and all other elements remain unchanged. `l` and `r` are integers such that \(1 \leq l < r \leq \text{len}(a)\). `ops` is a list that stores tuples of integers representing the operations performed, and now includes the tuple `(l, r)` if the condition `a[l] != r - l + 1` was true. `i` is set to `r` if the condition was true. `func_1` is called with arguments `a`, `l + 1`, `r`, `ops` if the condition was true.
#Overall this is what the function does:The function modifies the list `a` by setting certain subarrays to a specific value based on conditions, and records these modifications in the list `ops`. It does not return any value.

#State of the program right berfore the function call: a is a list of integers where each integer is between 0 and 10^7 inclusive, and n is the length of the list a, which satisfies 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of the integers in list `a`, the length of the empty list `ops`, and the empty list `ops` itself.
#Overall this is what the function does:The function takes a list of integers `a` as input and returns the sum of the integers in the list, along with the length of an empty list and the empty list itself.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < len(a), where a is a list of integers.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`, `i` is `r + 1`, `a[i]` for `i` in the range `[l, r]` is `r - l + 1`, `s` is `(r - l + 1) * (r - l + 1)`, `ops` includes the tuple `(l, r)`
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`. `s` is the sum of elements `a[l]` to `a[r]` and `s` is greater than `(r - l + 1) * (r - l + 1)`. `mx` is the maximum value in the sublist `a[l:r + 1]`. `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`. Additionally, `pos` is not equal to `l`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`. `s` is the sum of elements `a[l]` to `a[r]` and `s` is greater than `(r - l + 1) * (r - l + 1)`. `mx` is the maximum value in the sublist `a[l:r + 1]`. `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`. Additionally, `pos` is not equal to `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
    #State: `l` and `r` are integers such that `0 <= l <= r < len(a)`. If `s` is less than or equal to `(r - l + 1) * (r - l + 1)`, then `i` is `r + 1`, `a[i]` for `i` in the range `[l, r]` is `r - l + 1`, `s` is `(r - l + 1) * (r - l + 1)`, and `ops` includes the tuple `(l, r)`. Otherwise, `s` is the sum of elements `a[l]` to `a[r]` and `s` is greater than `(r - l + 1) * (r - l + 1)`. `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`, and `pos` is not equal to `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies a list `a` by potentially replacing elements within a specified range `[l, r]` with a uniform value if a certain condition is met. It also records operations performed in a list `ops`. The final state of the program results in the sublist `a[l:r+1]` being transformed such that all its elements are equal to `r - l + 1` if the sum of the sublist is less than or equal to `(r - l + 1) * (r - l + 1)`. Otherwise, it recursively processes sublists around the maximum element in the current sublist.

#State of the program right berfore the function call: a is a list of integers where each integer is in the range 0 to 10^7, and n is an integer representing the length of the list a such that 1 <= n <= 18.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s is the first return value of func_2 and m is the second return value of func_2)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `a` is a list of integers derived from the input, `n` is the integer value provided by the input, `s` is the first return value of `func_2`, `m` is the second return value of `func_2`, `ops` is an empty list.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list `a` of `n` integers from the input. It then calls another function `func_2` with the list `a`. The function prints the first two return values of `func_2` (denoted as `s` and `m`) and subsequently prints pairs of indices (incremented by 1) from the third return value of `func_2` (denoted as `ops`).

