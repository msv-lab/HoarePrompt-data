#State of the program right berfore the function call: a is a list of integers of length n (1 ≤ n ≤ 18), l and r are integers such that 0 ≤ l ≤ r < n, and ops is a list that will store tuples of integers representing the operations.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of integers of length n (1 ≤ n ≤ 18), l and r are integers such that 0 ≤ l ≤ r < n, and ops is a list. If a[l] is not 0, then ops contains the tuple (l, l) and the element at index l in the list a is 0. Otherwise, the element at index l in the list a remains 0 and ops is unchanged.
        return
        #The program returns `None`.
    #State: a is a list of integers of length n (1 ≤ n ≤ 18), l and r are integers such that 0 ≤ l ≤ r < n, and ops is a list that will store tuples of integers representing the operations. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers of length `n` where all elements from index `l` to index `r` (inclusive) are set to `r - l + 1`, `l` and `r` are integers such that 0 ≤ l ≤ r < n, and `ops` is a list that contains the tuple `(l, r)` and any other tuples that were appended by `func_1`.
        func_1(a, l + 1, r, ops)
    #State: `a` is a list of integers of length `n` (1 ≤ n ≤ 18), `l` and `r` are integers such that 0 ≤ l ≤ r < n, and `ops` is a list that will store tuples of integers representing the operations. If `a[l]` is not equal to `r - l + 1`, then all elements from index `l` to index `r` (inclusive) in `a` are set to `r - l + 1`, and all elements from index `l + 1` to index `r` (inclusive) are set to `r - (l + 1) + 1`. Additionally, `ops` contains the tuple `(l, r)` and the tuple `(l + 1, r)`, along with any other tuples appended by `func_1`. If `a[l]` is equal to `r - l + 1`, the list `a` and the list `ops` remain unchanged.
#Overall this is what the function does:The function `func_1` modifies a list `a` of integers of length `n` (1 ≤ n ≤ 18) and a list `ops` that stores tuples of integers representing operations. It ensures that for the subarray `a[l:r+1]`, if any element is not equal to `r - l + 1`, all elements in this subarray are set to `r - l + 1`, and the tuple `(l, r)` is appended to `ops`. If the subarray is already filled with `r - l + 1`, no modifications are made. The function does not return any value. After the function concludes, the list `a` may have some elements modified to `r - l + 1` within the specified range, and the list `ops` may contain new tuples representing these modifications.

#State of the program right berfore the function call: a is a list of integers such that 1 <= len(a) <= 18 and 0 <= a_i <= 10^7 for all i.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all integers in the list `a`, 0, and an empty list `ops`.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and returns a tuple containing the sum of all integers in the list `a`, the integer 0, and an empty list `ops`. The function does not modify the input list `a` or perform any operations that affect the program state outside of its scope.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), and a is a list of integers where 0 <= a[i] <= 10^7.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: The values of `a[l]` to `a[r]` inclusive are all set to `r - l + 1`, and `s` is the sum of these new values, which is `(r - l + 1) * (r - l + 1)`. The tuple `(l, r)` remains in the list `ops`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `l` and `r` are non-negative integers such that 0 <= `l` <= `r` < len(`a`), `a` is a list of integers where 0 <= `a[i]` <= 10^7, `s` is the sum of the integers from `a[l]` to `a[r]` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of the maximum value `mx` in the list `a` starting from `l`. If `pos` is not equal to `l`, the program retains all these conditions. If `pos` is equal to `l`, the program also retains all these conditions.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` and `r` are non-negative integers such that 0 <= `l` <= `r` < len(`a`), `a` is a list of integers where 0 <= `a[i]` <= 10^7, `s` is the sum of the integers from `a[l]` to `a[r]` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of the maximum value `mx` in the list `a` starting from `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` is called with arguments `pos + 1` and `r`. If `pos` is equal to `r`, the function retains all the initial conditions.
    #State: `l` and `r` are non-negative integers such that 0 <= `l` <= `r` < len(`a`), `a` is a list of integers where 0 <= `a[i]` <= 10^7. If `s` <= `(r - l + 1) * (r - l + 1)`, the values of `a[l]` to `a[r]` inclusive are all set to `r - l + 1`, and `s` is updated to `(r - l + 1) * (r - l + 1)`, with the tuple `(l, r)` remaining in the list `ops`. If `s` > `(r - l + 1) * (r - l + 1)`, `s` is the sum of the integers from `a[l]` to `a[r]` inclusive, `mx` is the maximum value in the sublist `a[l:r + 1]`, and `pos` is the index of the maximum value `mx` in the list `a` starting from `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` is called with arguments `pos + 1` and `r`. If `pos` is equal to `r`, the function retains all the initial conditions.
#Overall this is what the function does:The function `recursive_maximize_sum` accepts two non-negative integers `l` and `r`, and a list `a` of integers. It modifies the list `a` such that within the range `[l, r]`, if the sum of the elements in this range is less than or equal to the square of the range length, all elements in this range are set to the range length, and the tuple `(l, r)` is appended to the list `ops`. If the sum is greater, the function recursively processes the subranges to the left and right of the maximum element in the range `[l, r]`. The function does not return any value, but the final state of the list `a` and the list `ops` reflects the changes made according to the conditions described.

#State of the program right berfore the function call: No input variables are present in the function signature.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s is the first value returned by func_2(a) and m is the second value returned by func_2(a))
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: The values of `n`, `a`, `s`, and `m` remain unchanged. The loop iterates through each pair `(l, r)` in `ops` and prints `l + 1` and `r + 1` for each pair.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads an integer `n` from the user, followed by a list of `n` integers `a`. It then calls another function `func_2` with `a` as an argument, which returns three values: `s`, `m`, and `ops`. The function prints `s` and `m`, and then iterates over each pair `(l, r)` in `ops`, printing `l + 1` and `r + 1` for each pair. After the function concludes, the values of `n`, `a`, `s`, and `m` remain unchanged, and the pairs in `ops` have been printed in a modified form.

