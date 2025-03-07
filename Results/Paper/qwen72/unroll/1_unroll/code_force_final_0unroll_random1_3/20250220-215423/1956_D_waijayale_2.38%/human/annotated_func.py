#State of the program right berfore the function call: a is a list of integers, l and r are integers such that 0 <= l <= r < len(a), and ops is a list that will store tuples of integers representing the operations.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *`a` is a list of integers, `l` and `r` are integers such that 0 <= l <= r < len(a), and `l` is equal to `r`. If `a[l]` is not 0, then `a[l]` is set to 0, and `ops` is a list that now contains the tuple (l, l). If `a[l]` is 0, then `a[l]` remains unchanged and `ops` remains the same.
        return
        #The program returns without any value. The list `a` has its element at index `l` set to 0 if it was not already 0, and `ops` contains the tuple (l, l) if the element at `l` was changed. If `a[l]` was 0, then `a` and `ops` remain unchanged.
    #State: a is a list of integers, l and r are integers such that 0 <= l <= r < len(a), and ops is a list that will store tuples of integers representing the operations. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: a is a list of integers where all elements from index l to index r (inclusive) have been set to the value `r - l + 1`. The list `ops` contains the tuple `(l, r)`. The values of `l` and `r` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers, and `l` and `r` are integers such that 0 <= l <= r < len(a). If `a[l]` is not equal to `r - l + 1`, then all elements from index `l + 1` to index `r` (inclusive) in `a` have been set to the value `r - (l + 1) + 1`, and the list `ops` contains the tuples `(l, r)` and `(l + 1, r)`. The values of `l` and `r` remain unchanged. If `a[l]` is equal to `r - l + 1`, then no changes are made to `a` or `ops`.
#Overall this is what the function does:The function `func_1` modifies a list `a` and a list `ops` based on the indices `l` and `r`. If `l` equals `r`, it sets `a[l]` to 0 if `a[l]` is not already 0 and appends the tuple `(l, l)` to `ops` if the change was made. If `l` is not equal to `r`, it recursively processes the sublist from `l + 1` to `r`. If `a[l]` is not equal to `r - l + 1`, it sets all elements from index `l` to `r` in `a` to `r - l + 1` and appends the tuple `(l, r)` to `ops`. The function returns without any value, and the final state of `a` and `ops` depends on the initial values and the recursive calls.

#State of the program right berfore the function call: a is a list of integers such that 1 <= len(a) <= 18 and 0 <= a_i <= 10^7 for all i.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all integers in list `a`, the length of list `ops`, and the list `ops` itself, which may have been modified by the function `recursive_maximize_sum(0, n - 1)`.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and returns a tuple containing three elements: the sum of all integers in `a`, the length of the list `ops`, and the list `ops` itself. The list `ops` may have been modified by the internal function `recursive_maximize_sum`, which is called with the initial indices of the list `a`. The function does not alter the input list `a`.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), where a is a list of integers.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: The list `a` has been updated such that all elements from index `l` to index `r` inclusive are set to the value `r - l + 1`. The variable `s` is the sum of the elements in the list `a` from index `l` to index `r` inclusive, which is now equal to `(r - l + 1) * (r - l + 1)`. The tuple `(l, r)` has been appended to the list `ops`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `s` is the sum of the elements in the list `a` from index `l` to index `r` inclusive, `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `l`, the function `recursive_maximize_sum` has been called with arguments `l` and `pos - 1`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `s` is the sum of the elements in the list `a` from index `l` to index `r` inclusive, `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`. If `pos` is not equal to `l`, the function `recursive_maximize_sum` has been called with arguments `l` and `pos - 1`.
    #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `s` is the sum of the elements in the list `a` from index `l` to index `r` inclusive. If `s` <= `(r - l + 1) * (r - l + 1)`, the list `a` has been updated such that all elements from index `l` to index `r` inclusive are set to the value `r - l + 1`, `s` is now equal to `(r - l + 1) * (r - l + 1)`, and the tuple `(l, r)` has been appended to the list `ops`. If `s` > `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`. If `pos` is not equal to `l`, the function `recursive_maximize_sum` has been called with arguments `l` and `pos - 1`.
#Overall this is what the function does:The function `recursive_maximize_sum` accepts two parameters `l` and `r`, which are non-negative integers such that 0 <= l <= r < len(a), where `a` is a list of integers. It modifies the list `a` and the list `ops` in the following ways: If the sum of the elements in the sublist `a[l:r + 1]` is less than or equal to the square of the length of this sublist, it updates all elements in this sublist to the length of the sublist and appends the tuple `(l, r)` to the list `ops`. If the sum is greater, it recursively applies the same logic to the sublists before and after the maximum element in `a[l:r + 1]`. The function does not return any value. After the function concludes, the list `a` will have been modified according to the rules described, and the list `ops` will contain tuples representing the ranges of sublists that were updated.

#State of the program right berfore the function call: No variables are passed to the function `func_3`. The function reads an integer `n` from the input, which represents the length of the array `a`. The array `a` is then read from the input as a list of `n` integers.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s is the sum of some elements in the list `a` and m is the maximum or minimum value of some elements in the list `a`)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: The values of `n`, `a`, `s`, and `m` remain unchanged. The loop prints the values of `l + 1` and `r + 1` for each pair `(l, r)` in `ops`.
#Overall this is what the function does:The function `func_3` reads an integer `n` from the input, which represents the length of an array `a`. It then reads `a` as a list of `n` integers from the input. The function calls another function `func_2` with the array `a` and receives three values: `s`, `m`, and `ops`. It prints `s` and `m`, where `s` is the sum of some elements in `a` and `m` is the maximum or minimum value of some elements in `a`. Additionally, it prints the values of `l + 1` and `r + 1` for each pair `(l, r)` in `ops`. The function does not return any values. The original values of `n`, `a`, `s`, and `m` remain unchanged after the function concludes.

