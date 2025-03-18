#State of the program right berfore the function call: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: a is a list of non-negative integers, l is equal to r, and if the element at index l in a is not 0, then ops is a list containing the tuple (l, l). If the element at index l in a is 0, then no change is made to ops.
        return
        #The program returns None
    #State: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed. l is not equal to r
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list where each element from index `l` to index `r` is set to `r - l + 1`, `l` is `l + 1`, `r` is `r`, `ops` is a list containing the tuple `(l, r)`.
        func_1(a, l + 1, r, ops)
    #State: Postcondition: `a` is a list of non-negative integers, `l` is `l + 2`, `r` is `r`, and `ops` is a list containing the tuple `(l + 1, r)`. If the element at index `l` in list `a` is not equal to `r - l + 1`, then each element from index `l + 1` to index `r` in list `a` is set to `1`.
#Overall this is what the function does:The function processes a list `a` of non-negative integers within a specified range `[l, r]`. It ensures that all elements in this range are either zero or equal to `r - l + 1`. If any element is not zero and not equal to `r - l + 1`, it is set to `r - l + 1`, and the operation is recorded in the `ops` list. The function recursively processes the range starting from `l + 1` to `r` after making changes. The final state of the list `a` and the `ops` list reflect these operations.

#State of the program right berfore the function call: a is a list of non-negative integers, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops', and the contents of list 'ops' itself.
#Overall this is what the function does:The function `func_2` accepts a list `a` containing non-negative integers and returns three values: the sum of all elements in the list `a`, the length of the list `ops` (which is modified within the function), and the contents of the list `ops`.

#State of the program right berfore the function call: a is a list of n integers where 1 <= n <= 18 and 0 <= a_i <= 10^7; l and r are non-negative integers such that 1 <= l <= r <= n; ops is a list that will store the operations performed.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list of n integers where for each index i in the range [l-1, r-1], `a[i]` equals `r - l + 1`, and for all other indices, `a[i]` remains unchanged. The value of `s` is `(r - l + 1) * (r - l + 2) / 2` if `l <= i <= r`, otherwise `s` remains unchanged. `l` and `r` retain their original values.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `a` is a list of n integers where 1 <= n <= 18 and 0 <= a_i <= 10^7; `l` and `r` are non-negative integers such that 1 <= l <= r <= n; `ops` is a list that will store the operations performed; `s` is the sum of elements from index `l` to index `r` (inclusive); `s` is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist a[l:r + 1]; if `pos` is not equal to `l`, the function `recursive_maximize_sum` is called with arguments `l` and `pos - 1`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `a` is a list of n integers where 1 <= n <= 18 and 0 <= a_i <= 10^7; `l` and `r` are non-negative integers such that 1 <= l <= r <= n; `ops` is a list that will store the operations performed; `s` is the sum of elements from index `l` to index `r` (inclusive); `s` is greater than (r - l + 1) * (r - l + 1); `mx` is the maximum value in the sublist a[l:r + 1]; if `pos` is not equal to `r`, `pos` is incremented by 1 and the function `recursive_maximize_sum(pos + 1, r)` is called.
    #State: `a` is a list of n integers where 1 <= n <= 18 and 0 <= a_i <= 10^7; `l` and `r` are non-negative integers such that 1 <= l <= r <= n; `ops` is a list that will store the operations performed; `s` is the sum of elements from index `l` to index `r` (inclusive). If `s` is less than or equal to `(r - l + 1) * (r - l + 1)`, then for each index i in the range [l-1, r-1], `a[i]` equals `r - l + 1`, and for all other indices, `a[i]` remains unchanged. The value of `s` is `(r - l + 1) * (r - l + 2) / 2` if `l <= i <= r`, otherwise `s` remains unchanged. `l` and `r` retain their original values. If `s` is greater than `(r - l + 1) * (r - l + 1)`, then `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, and if `pos` is not equal to `r`, `pos` is incremented by 1 and the function `recursive_maximize_sum(pos + 1, r)` is called.
#Overall this is what the function does:The function `recursive_maximize_sum` takes two parameters, `l` and `r`, which define a sublist of the input list `a`. It modifies the sublist to maximize the sum of its elements under certain conditions. Specifically, if the sum of the sublist is less than or equal to \((r - l + 1)^2\), it sets all elements in the sublist to \(r - l + 1\) and records the operation. Otherwise, it finds the maximum element in the sublist and recursively calls itself on the left and right parts of the sublist excluding the position of the maximum element. The function returns the maximum sum achievable by these operations.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 18, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (the result of func_2(a)), m (the result of func_2(a))
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: The loop prints the pairs (l+1, r+1) for each (l, r) in ops. The final output state will consist of multiple lines, each containing two integers separated by a space, representing the printed pairs.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers from the user. It then calls another function `func_2` to compute values `s` and `m`, and a list `ops`. It prints `s` and `m`, and subsequently prints each pair `(l+1, r+1)` for every `(l, r)` in `ops`. The final output consists of multiple lines, each containing two integers separated by a space.

