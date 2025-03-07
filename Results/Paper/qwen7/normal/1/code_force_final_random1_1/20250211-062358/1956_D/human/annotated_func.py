#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18, and each element a[i] satisfies 0 <= a[i] <= 10^7. ops is an empty list that will store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of non-negative integers of length n, where 1 <= n <= 18, and each element `a[i]` for i != l remains the same. If `a[l]` is not 0, the length of `a` is n and each element `a[i]` for i != l is the same as before.
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: a is a list of non-negative integers of length n, where 1 <= n <= 18, and each element a[i] satisfies 0 <= a[i] <= 10^7. ops is an empty list that will store the operations performed. l and r are indices such that l is not equal to r
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `ops` is now `['(l, r)']`, `l` must be less than or equal to `r`, `i` is `r + 1`, `a[i]` is still `0` (since `i` exceeds the loop range and no further assignment occurs).
        #
        #Explanation: After the loop completes all its iterations, the variable `i` will be set to `r + 1` because the loop increments `i` from `l` to `r`. Since the loop condition `i <= r` is no longer satisfied when `i` becomes `r + 1`, the loop terminates. Therefore, none of the elements in the list `a` are modified beyond the index `r`, and the rest of the elements, including `a[r+1]`, remain unchanged at their initial values, which are `0` if they were not initialized otherwise.
        func_1(a, l + 1, r, ops)
    #State: Postcondition: `ops` is an empty list, `a` is a list of non-negative integers, `l` is less than or equal to `r`, `i` is `r + 1`, `a[i]` is `0`, and if `a[l]` is not equal to `r - l + 1`, then `ops` is updated to `['(l, r)']`.
#Overall this is what the function does:The function processes a list `a` of non-negative integers and updates it based on the indices `l` and `r`. It appends operations to the list `ops` that describe the changes made. Specifically, if `a[l]` is not zero and within the range `[l, r]`, it sets `a[l]` to zero and records the operation. If `a[l]` is not equal to `r - l + 1`, it updates all elements from `l` to `r` to `r - l + 1` and records the operation. The function recursively processes the subarray defined by `l + 1` to `r`.

#State of the program right berfore the function call: `a` is a list of non-negative integers of length `n`, where `1 <= n <= 18` and `0 <= a_i <= 10^7`.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops' which is currently 0, and an empty list 'ops'
#Overall this is what the function does:The function accepts a list of non-negative integers `a` and processes it by calling a recursive function `recursive_maximize_sum`. After processing, it returns the sum of all elements in the list `a`, the length of a list `ops` which is initialized to 0, and an empty list `ops`.

#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18, and 0 <= a_i <= 10^7 for all 1 <= i <= n. ops is a list used to store the operations performed during the process.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The variable `i` will be `r + 1`, `l` remains the first element of `ops`, `r` remains the second element of `ops`, and `a[i]` is `r - l + 1`.
        #
        #In natural language: After the loop has executed all its iterations, the variable `i` will have reached the next index after `r` (which is `r + 1`), while `l` and `r` remain unchanged as they were in the initial state. All elements from index `l` to index `r` in list `a` will be set to the value `r - l + 1`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: Postcondition: `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `l`, the function `recursive_maximize_sum(l, pos - 1)` is called.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
    #State: `s` is the sum of elements from index `l` to index `r` inclusive in list `a`. If `s` is less than or equal to `(r - l + 1) * (r - l + 1)`, then `i` will be `r + 1`, `l` and `r` remain unchanged, and all elements from index `l` to index `r` in list `a` will be set to the value `r - l + 1`. Otherwise, `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`, and if `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
#Overall this is what the function does:The function `recursive_maximize_sum` takes a list `a` and updates it to maximize the sum of any subarray defined by indices `l` and `r`. If the sum of the current subarray is less than or equal to the square of its length, it sets all elements within the subarray to the subarray's length. Otherwise, it finds the maximum element in the subarray and recursively processes the subarrays before and after this maximum element. The function does not return a value but modifies the input list `a` in place.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 18, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (the sum of elements in list a), m (the maximum element in list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: `ops` is a list that contains exactly the number of tuples equal to the number of iterations the loop has executed, which is the same as the initial value of `n`.
    #
    #Natural Language Explanation: After the loop has executed all its iterations, the `ops` list will contain exactly `n` tuples. Each tuple represents a pair of indices `(l, r)` that were printed during each iteration of the loop. Since the loop runs `n` times based on the initial state where `n` is the length of the list `a`, the `ops` list will have `n` elements, each being a tuple that was printed during the corresponding iteration.
#Overall this is what the function does:The function processes a list `a` of integers and prints the sum and maximum value of the list. It also generates and prints a series of index pairs `(l, r)` that represent operations performed on the list. The function does not accept any parameters and does not return any value; instead, it modifies and prints the output based on the input list `a`.

