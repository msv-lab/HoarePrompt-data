#State of the program right berfore the function call: a is a list of integers where each integer is in the range 0 to 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples representing the operations performed on the array a.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of integers where each integer is in the range 0 to 10^7, `l` and `r` are integers such that 1 <= l <= r <= len(a), and `ops` is a list that will store tuples representing the operations performed on the array `a`. Additionally, `l` is equal to `r`. If `a[l]` is not 0, no changes are made to `a` or `ops`. If `a[l]` is 0, `ops` contains one tuple `(l, l)`.
        return
        #The program returns nothing.
    #State: a is a list of integers where each integer is in the range 0 to 10^7, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list that will store tuples representing the operations performed on the array a. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where each integer in the range from index `l` to `r` (inclusive) has been set to the value `r - l + 1`. All other elements of `a` remain unchanged. `l` and `r` are integers such that 1 <= l <= r <= len(a), and `l` is not equal to `r`. `ops` is a list that contains the tuple `(l, r)`.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers where each integer in the range from index `l` to `r` is set to `r - l + 1` if `a[l] != r - l + 1`, otherwise `a` remains unchanged. All other elements of `a` remain unchanged. `l` and `r` are integers such that `1 <= l <= r <= len(a)`, and `l` is not equal to `r`. `ops` is a list that contains the tuple `(l, r)` if `a[l] != r - l + 1`.
#Overall this is what the function does:The function `func_1` modifies a list of integers `a` by setting elements in the range from index `l` to `r` to the value `r - l + 1` if the element at index `l` is not already equal to that value. It records these modifications in the list `ops` as tuples `(l, r)`. The function does not return any value.

#State of the program right berfore the function call: a is a list of integers where 0 <= a_i <= 10^7 for all i, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of the list 'a', the length of the list 'ops', and the list 'ops' itself.
#Overall this is what the function does:The function `func_2` takes a list of integers `a` as input, where each integer is between 0 and 10^7 inclusive, and the length of the list is between 1 and 18. It returns a tuple containing the sum of the list `a`, the length of an operations list `ops`, and the operations list `ops` itself.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < n, where n is the length of the array a.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are integers such that 0 <= l <= r < n, where n is the length of the array `a`. `s` is the sum of the elements in the array `a` from index `l` to `r` inclusive, and `s` is less than or equal to (r - l + 1) * (r - l + 1). `ops` is a list that now includes the tuple `(l, r)` as its last element. The elements of `a` from index `l` to `r` are all set to `r - l + 1`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are integers such that 0 <= l <= r < n, where n is the length of the array `a`. `s` is the sum of the elements in the array `a` from index `l` to `r` inclusive, and `s` is greater than (r - l + 1) * (r - l + 1). `mx` is the maximum value in the subarray `a[l:r + 1]`. `pos` is the index of `mx` in the array `a`. If `pos` is not equal to `l`, then the current value of `pos` remains the index of the maximum value in the subarray `a[l:r + 1]`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: `l` and `r` are integers such that 0 <= l <= r < n, where n is the length of the array `a`. `s` is the sum of the elements in the array `a` from index `l` to `r` inclusive, and `s` is greater than (r - l + 1) * (r - l + 1). `mx` is the maximum value in the subarray `a[l:r + 1]`. `pos` is the index of `mx` in the array `a`. If `pos` is not equal to `r`, then the function `recursive_maximize_sum(pos + 1, r)` has been executed, and `pos` remains the index of the maximum value in the subarray `a[l:r + 1]`. If `pos` is equal to `r`, then no further action is taken.
    #State: `l` and `r` are integers such that 0 <= l <= r < n, where n is the length of the array `a`. If `s` (the sum of the elements in the array `a` from index `l` to `r` inclusive) is less than or equal to (r - l + 1) * (r - l + 1), then `ops` is a list that includes the tuple `(l, r)` as its last element and the elements of `a` from index `l` to `r` are all set to `r - l + 1`. Otherwise, `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the subarray `a[l:r + 1]`, and `pos` is the index of `mx` in the array `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been executed, and `pos` remains the index of the maximum value in the subarray `a[l:r + 1]`. If `pos` is equal to `r`, no further action is taken.
#Overall this is what the function does:The function `recursive_maximize_sum` modifies a given array `a` by setting the elements within a specified range `[l, r]` to a uniform value if their sum is less than or equal to the square of the range's length. If the sum is greater, it recursively processes subarrays divided by the maximum element's position within the range. The function also records operations performed in the list `ops`.

#State of the program right berfore the function call: a is a list of integers of length n, where 1 <= n <= 18 and 0 <= a_i <= 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s is the sum of all elements in the list `a` and m is the maximum value in the list `a`)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: The values of `a`, `n`, `s`, and `m` remain unchanged. The output consists of printed pairs `(l + 1, r + 1)` for each `(l, r)` in `ops`.
#Overall this is what the function does:The function `func_3` reads an integer `n` and a list `a` of `n` integers from the input, calculates the sum `s` and the maximum `m` of the list `a`, prints `s` and `m`, and then prints pairs of indices (1-based) representing some operations. The list `a` and the integer `n` remain unchanged.

