#State of the program right berfore the function call: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed. If a[l] is not 0, then ops is now [('l', 'l')], l is equal to r, and a[l] is 0. If a[l] is 0, then the conditions remain unchanged.
        return
        #The program does not return any value since there is no return statement in the given code.
    #State: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed. l is not equal to r
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `i` is `r + 1`, `l` is `l`, `r` is `r`, `a` is a list of non-negative integers where all elements from index `l` to index `r` are set to `r - l + 1`, and `ops` is a list containing the tuple `(l, r)` used to store the operations.
        #
        #This means that after the loop has executed all its iterations, the variable `i` will be one more than the final value of `r` (i.e., `r + 1`), since `i` starts at `l` and increments by 1 in each iteration until it exceeds `r`. The variable `l` remains unchanged at its initial value, and `r` also remains unchanged. All elements in the list `a` from index `l` to index `r` will be set to the value `r - l + 1`, as the loop updates these elements in each iteration. The `ops` list will contain the single tuple `(l, r)` representing the operation performed on the slice of the list `a` from index `l` to index `r`.
        func_1(a, l + 1, r, ops)
    #State: Postcondition: `a` is a list of non-negative integers, `l` is `l + 1`, `r` is `r`, and `ops` is a list used to store the operations performed including the operation `func_1(a, l + 1, r, ops)`. If `a[l]` is not equal to `r - l + 1`, then `i` is set to `r + 1`, `l` remains `l`, `r` remains `r`, and all elements from index `l` to index `r` in `a` are set to `r - l + 1`, with the tuple `(l, r)` added to `ops`. If `a[l]` equals `r - l + 1`, no changes are made to `a`, `l`, `r`, or `ops`.
#Overall this is what the function does:The function processes a list of non-negative integers `a` by performing operations on its sublists defined by indices `l` and `r`. If `l` equals `r` and `a[l]` is not zero, it sets `a[l]` to zero and records the operation. Otherwise, it recursively ensures that all elements from `l` to `r` are set to `r - l + 1`, records the operation, and continues processing the sublist starting from `l + 1` to `r`. No value is returned.

#State of the program right berfore the function call: a is a list of non-negative integers, where the length of the list n satisfies 1 <= n <= 18, and each element a_i in the list satisfies 0 <= a_i <= 10^7.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops', and the empty list 'ops' itself.
#Overall this is what the function does:The function accepts a list of non-negative integers and returns three values: the sum of all elements in the list, the length of a list named 'ops' (which is initially empty), and the empty list 'ops' itself.

#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18, and 0 <= a_i <= 10^7 for all 1 <= i <= n. ops is a list used to store the operations performed.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `i` is equal to `r + 1`, `l` is the same as the original value, `r` is the same as the original value, and every element in the list `a` from index `l` to index `r` is set to `r - l + 1`.
        #
        #In this final state, the loop has completed all its iterations, meaning `i` has reached `r + 1`. All elements in the sublist of `a` from index `l` to `r` have been updated to the value `r - l + 1`. The variables `l` and `r` remain unchanged from their initial values.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: Postcondition: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`, and either `pos` is decremented by 1 and the function `recursive_maximize_sum` is called with arguments `l` and `pos - 1`, or `pos` is still equal to `l`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `r`, `pos` is decremented by 1 and the function `recursive_maximize_sum` is called with arguments `pos + 1` and `r`. If `pos` is equal to `r`, no further changes are made to `pos`.
    #State: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive. If `s` is less than or equal to `(r - l + 1) * (r - l + 1)`, then all elements in the sublist of `a` from index `l` to `r` are set to `r - l + 1`, and `i` is set to `r + 1`. Otherwise, `s` remains unchanged, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist plus `l`, and if `pos` is not equal to `r`, `pos` is decremented by 1 and the function `recursive_maximize_sum` is called with arguments `pos + 1` and `r`. If `pos` is equal to `r`, no further changes are made to `pos`.
#Overall this is what the function does:The function `recursive_maximize_sum` takes two parameters, `l` and `r`, which define a sublist within the list `a`. It aims to maximize the sum of the elements in this sublist by performing certain operations. If the sum of the elements in the sublist from index `l` to `r` is less than or equal to \((r - l + 1)^2\), it sets all elements in this sublist to \(r - l + 1\). Otherwise, it finds the maximum element in the sublist, updates the sublist to ensure the sum is maximized by recursively calling itself on the left and right parts of the sublist excluding the position of the maximum element, until the condition is met. The function does not return any value; instead, it modifies the list `a` in place and updates the `ops` list with the operations performed.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 18, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: the sum of all elements in the list `a` and the maximum value in the list `a`
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: `n` is an input integer, `a` is a list of `n` integers where each integer `a_i` satisfies \(0 \leq a_i \leq 10^7\), `s`, `m`, and `ops` are the results of the function `func_2(a)`, and `ops` contains exactly three tuples `(l, r)`. The first tuple has `l` as the first element and `r` as the second element of the first tuple, the second tuple has `l` as the first element and `r` as the second element of the second tuple, and the third tuple has `l` as the first element and `r` as the second element of the third tuple.
    #
    #In simpler terms, after the loop executes all its iterations, `ops` will contain exactly three operations, each specified by a tuple `(l, r)`, and these tuples will be printed out by the loop.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers from the user. It then calls another function `func_2` with the list `a` and receives the sum `s` of all elements in `a`, the maximum value `m` in `a`, and a list of operations `ops`. It prints the sum `s` and the maximum value `m`. After that, it prints three specific operations specified by the tuples `(l, r)` contained in `ops`. The function does not return any value but modifies the output by printing the required information.

