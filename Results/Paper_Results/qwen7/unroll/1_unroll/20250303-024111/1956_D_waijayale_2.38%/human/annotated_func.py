#State of the program right berfore the function call: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: Postcondition: `a` is a list of non-negative integers, `l` and `r` are integers such that 1 <= l <= r <= len(a), and if the value of `a[l]` is not 0, then `a[l]` remains unchanged. If the value of `a[l]` is 0, then the value of `a[l]` remains 0.
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed. l is not equal to r
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list where all elements from index `l` to index `r` are set to `r - l + 1`, `l` is `l + 1`, `r` is `r`, `ops` is a list containing the tuples `(l, r)` as its last element.
        func_1(a, l + 1, r, ops)
    #State: Postcondition: `a` is a list of non-negative integers. If `a[l]` is not equal to `r - l + 1`, then all elements from index `l + 1` to index `r` are set to `r - (l + 1) + 1`, `l` is incremented by 2, `r` remains unchanged, and `ops` contains the tuple `(l + 1, r)` as its last element. If `a[l]` equals `r - l + 1`, then no changes are made to the list `a`, `l` remains unchanged, `r` remains unchanged, and `ops` remains unchanged.
#Overall this is what the function does:The function modifies a list `a` of non-negative integers by setting all elements from index `l` to index `r` to the value `r - l + 1`. It also records the operation performed on the list in the `ops` list. If `l` equals `r` and the value at index `l` is not zero, it sets the value at index `l` to zero and records the operation. If `a[l]` is already equal to `r - l + 1`, no changes are made. If `a[l]` is not equal to `r - l + 1`, it updates the list and records the operation. The function continues to recursively process sublists until all elements from `l` to `r` are set to the correct value.

#State of the program right berfore the function call: `a` is a list of non-negative integers, and `n` is the length of the list such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops', and the contents of list 'ops' itself.
#Overall this is what the function does:The function accepts a list of non-negative integers `a` and returns three values: the sum of all elements in `a`, the length of the list `ops` (which is generated during the execution), and the contents of `ops`.

#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18 and 0 <= a_i <= 10^7. l and r are integers such that 1 <= l <= r <= n. ops is a list that will store the sequence of operations performed.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `ops` is now a list containing the tuple `(l, r)`, `s` is the sum of the element `r - l + 1` repeated `r - l + 1` times, and `a` is a list where all elements from index `l` to index `r` are set to `r - l + 1`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `mx` remains the maximum value in the sublist `a[l:r + 1]`, `s` remains the sum of elements in list `a` from index `l` to index `r`, inclusive, `a` remains a list of non-negative integers of length `n`, where 1 <= n <= 18 and 0 <= a_i <= 10^7, `ops` includes the operation `s = sum(a[l:r + 1])`, and either `pos` is the index of the maximum value `mx` in the sublist `a[l:r + 1]` adjusted by `l` (if `pos != l` and `recursive_maximize_sum(l, pos - 1)` has been called), or `pos` remains unchanged (if `pos == l`).
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `mx` remains the maximum value in the sublist `a[l:r + 1]`, `s` remains the sum of elements in list `a` from index `l` to index `r`, inclusive, `a` remains a list of non-negative integers of length `n`, where 1 <= n <= 18 and 0 <= a_i <= 10^7, `ops` includes the operation `s = sum(a[l:r + 1])`, and if `pos != r`, `pos` is incremented by 1 and the function `recursive_maximize_sum` is called with the new position `pos + 1` and the end index `r`.
    #State: `ops` is a list containing the tuple `(l, r)`, `s` is the sum of the element `r - l + 1` repeated `r - l + 1` times, and `a` is a list where all elements from index `l` to index `r` are set to `r - l + 1` if `s <= (r - l + 1) * (r - l + 1)`. Otherwise, `mx` remains the maximum value in the sublist `a[l:r + 1]`, `s` remains the sum of elements in list `a` from index `l` to index `r`, inclusive, `a` remains a list of non-negative integers of length `n`, where 1 <= n <= 18 and 0 <= a_i <= 10^7, `ops` includes the operation `s = sum(a[l:r + 1])`, and if `pos != r`, `pos` is incremented by 1 and the function `recursive_maximize_sum` is called with the new position `pos + 1` and the end index `r`.
#Overall this is what the function does:The function `recursive_maximize_sum` takes two parameters `l` and `r`, which define a subarray of the list `a`. It modifies the subarray to maximize the sum of its elements under certain conditions. If the sum of the subarray is less than or equal to \((r - l + 1)^2\), it sets all elements in the subarray to \(r - l + 1\) and records the operation in the list `ops`. Otherwise, it finds the maximum element in the subarray, updates `ops` with the operation, and recursively calls itself on the left and right subarrays excluding the position of the maximum element, unless the maximum element is at the boundary of the current subarray. The function does not return a value but modifies the list `a` and populates the list `ops` with the operations performed.

#State of the program right berfore the function call: n is an integer such that 1 <= n <= 18, and a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (the sum of all elements in the list a), m (the maximum value in the list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: a is a list of n integers, s is the sum of the elements in a, m is the maximum value in a, and the console prints the pairs (l+1, r+1) for each operation in ops.
#Overall this is what the function does:The function reads a list of integers `a` of length `n` (where `1 <= n <= 18`) and calls another function `func_2` to compute the sum `s` of the elements in `a`, the maximum value `m` in `a`, and a list `ops` of operations. It then prints the sum `s` and the maximum value `m`, followed by the indices `(l+1, r+1)` for each operation in `ops`. The function does not return any value.

